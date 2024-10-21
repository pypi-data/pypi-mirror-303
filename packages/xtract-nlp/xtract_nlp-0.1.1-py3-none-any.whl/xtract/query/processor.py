import torch
import math
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from nltk.corpus import stopwords
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
from xtract import utils
from xtract.embedding import EmbeddingModel, PoolingType, visualize_embeddings, plot_similarity_heatmap
from typing import List, Dict


class QueryProcessor:

    def __init__(self, model: EmbeddingModel, code_chunks: List[str], code_embeddings: torch.Tensor):
        """
        Initialize the QueryProcessor with the embedding model and precomputed code embeddings.
        """
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        self.model = model
        self.code_chunks = code_chunks
        self.code_embeddings = code_embeddings.to(self.device)

        qem, trc = "google/flan-t5-large", True
        self.query_expansion_model = AutoModelForSeq2SeqLM.from_pretrained(
            qem, trust_remote_code=trc).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(
            qem, trust_remote_code=trc)

        self._bm25_precompute()

    def query(self, _input: str, count: int = 5, pooling: PoolingType = "mean", preprocess: bool = True, visualize: bool = False):
        """
        Process a query and return the 'count' relevant code snippets.
        """
        # _input = self.expand_query(_input)
        if preprocess:
            _input = self.extract_keywords(_input)
        valid_indices = self.keyword_search(_input)
        if not valid_indices:
            return []
        embeddings = self.code_embeddings[valid_indices]
        query = self.model.generate_embeddings(
            code_chunks=[_input],
            pooling=pooling
        ).to(self.device)
        similarities = cosine_similarity(
            query.cpu(), embeddings.cpu())
        indices = similarities.argsort()[0][::-1]
        # indices = self.keyword_density_rerank(_input, indices)
        indices = self.bm25_rerank(_input, indices)
        snippets = [self.code_chunks[i] for i in indices[:count]]
        if visualize:
            visualize_embeddings(embeddings, method="tsne")
            plot_similarity_heatmap(
                embeddings, title="Cosine Similarity (Between Code Embeddings)")
            combined_embeddings = torch.cat(
                [embeddings, query], dim=0)
            plot_similarity_heatmap(
                combined_embeddings, title="Cosine Similarity (Query vs Code Embeddings)")
        return snippets

    def keyword_search(self, query: str) -> List[int]:
        """
        Filter out code chunks that don't contain any keywords.
        """
        keywords = [utils.clean_token(keyword) for keyword in query.split()]
        indices = []
        for i, chunk in enumerate(self.code_chunks):
            if any(keyword.lower() in chunk.lower() for keyword in keywords):
                indices.append(i)
        return indices

    def bm25_rerank(
        self,
        query: str,
        indices: List[int],
        k1: float = 1.5,
        b: float = 0.75
    ) -> List[int]:
        """
        Rerank the indices based on BM25 scoring.
        """
        # https://www.researchgate.net/publication/220613776_The_Probabilistic_Relevance_Framework_BM25_and_Beyond
        # BM25(d, q) = sum_{t in q} IDF(t) * ((f(t, d) * (k1 + 1)) / (f(t, d) + k1 * (1 - b + b * (|d| / avgdl))))
        # where:
        # - BM25(d, q) is the relevance score of document 'd' for query 'q'
        # - IDF(t) is the inverse document frequency of term 't': IDF(t) = log((N - n_t + 0.5) / (n_t + 0.5))
        #   - N is the total number of documents
        #   - n_t is the number of documents containing the term 't'
        # - f(t, d) is the frequency of term 't' in document 'd'
        # - |d| is the length of document 'd' (in terms of words)
        # - avgdl is the average document length across the entire corpus
        # - k1 and b are parameters that control term frequency saturation and document length normalization
        query_terms = query.split()
        scores: Dict[int, float] = {i: 0 for i in indices}
        N = len(self.code_chunks)
        for term in query_terms:
            if term in self.doc_freqs:
                idf = math.log(
                    (N - self.doc_freqs[term] + 0.5) / (self.doc_freqs[term] + 0.5) + 1)
                for i in indices:
                    doc = self.code_chunks[i]
                    term_freq = doc.split().count(term)
                    doc_len = len(doc.split())
                    tf_norm = (term_freq * (k1 + 1)) / (term_freq +
                                                        k1 * (1 - b + b * (doc_len / self.avgdl)))
                    scores[i] += idf * tf_norm
        return sorted(scores, key=scores.get, reverse=True)  # type: ignore

    def keyword_density_rerank(
        self,
        query: str,
        indices: List[int],
        density_weight: float = 1,
        count_weight: float = 0,
        normalize_length: bool = True
    ) -> List[int]:
        """
        Rerank indices from cosine similarity based on a combination of keyword density and total count,
        with normalization to prevent smaller or larger chunks of code from being overly favored.
        """
        # NOTE(justin): BM25 is being used for reranking now, but I'm leaving this here temporarily for reference
        keywords = [utils.clean_token(keyword) for keyword in query.split()]
        scores: Dict[int, float] = {}
        avg_words = sum(
            len(chunk.split()) for chunk in self.code_chunks
        ) / len(self.code_chunks)
        for i in indices:
            chunk = self.code_chunks[i]
            words = chunk.split()
            if not words:
                continue
            count = sum(
                1 for word in words if
                any(keyword.lower() in word.lower() for keyword in keywords)
            )
            if count > 0:
                density = count / len(words)
                if normalize_length:
                    length_factor = min(1.0, len(words) / avg_words)
                    density *= length_factor
                score = (density_weight * density) + (count_weight * count)
                scores[i] = score
        return sorted(scores, key=scores.get, reverse=True)  # type: ignore

    def extract_keywords(self, query: str) -> str:
        """
        Extract important keywords from the query.
        """
        utils.download_stopwords()
        return ' '.join([
            word for word in query.split() if word.lower()
            not in set(stopwords.words("english")) and word.isalnum()
        ])

    def expand_query(self, query: str, count: int = 3) -> str:
        """
        Automatically expand the query using the T5 model to generate related programming phrases.
        """
        # TODO(justin): message around w different models/hyperparams to improve results
        input_text = f"""
        Expand this query by adding programming-related keywords and technical concepts.
        Focus on generating terms relevant to code retrieval or NLP-based code search engines.
        Query: '{query}'
        """
        inputs = self.tokenizer.encode(
            input_text, return_tensors="pt").to(self.device)
        outputs = self.query_expansion_model.generate(
            inputs,
            max_length=100,
            num_return_sequences=count,
            num_beams=7,
            do_sample=True,
            temperature=1.3,
            no_repeat_ngram_size=3,
            early_stopping=True
        )
        expanded_queries = [self.tokenizer.decode(
            output, skip_special_tokens=True).strip() for output in outputs]
        expanded_query = f"{query} " + " ".join(expanded_queries)
        return expanded_query

    def _bm25_precompute(self):
        """
        Compute the document frequency for each term in the corpus, and average document length.
        """
        self.doc_freqs = Counter()
        for chunk in self.code_chunks:
            words = set(chunk.split())
            self.doc_freqs.update(words)
        self.avgdl = sum(len(chunk.split())
                         for chunk in self.code_chunks) / len(self.code_chunks)
