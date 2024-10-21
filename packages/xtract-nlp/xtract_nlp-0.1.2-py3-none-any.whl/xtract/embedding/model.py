import os
import torch
from transformers import AutoTokenizer, AutoModel, PreTrainedTokenizer, PreTrainedTokenizerFast
from typing import List, Union, Literal

ATTENTION_VECTOR_PATH = "./attention_vector.pt"

TokenizerType = Union[PreTrainedTokenizer, PreTrainedTokenizerFast]
PoolingType = Literal["mean", "max", "cls", "attention"]


class EmbeddingModel:

    def __init__(self, model_name: str = "microsoft/codebert-base"):
        self.model_name = model_name
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.add_special_tokens(
                {'pad_token': self.tokenizer.eos_token})
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        self.model.eval()
        self.attention_vector = self.load_attention_vector()

    def generate_embeddings(self, code_chunks: List[str], batch_size: int = 8, normalize: bool = True, pooling: PoolingType = "mean") -> torch.Tensor:
        embeddings = []
        for i in range(0, len(code_chunks), batch_size):
            batch = code_chunks[i:i+batch_size]
            inputs = self.tokenizer(
                batch, return_tensors="pt", padding=True, truncation=True
            ).to(self.device)

            with torch.no_grad():
                if "t5" in self.model.config.architectures[0].lower():
                    outputs = self.model.encoder(**inputs)
                else:
                    outputs = self.model(**inputs)

                if pooling == "mean":
                    batch_embeddings = outputs.last_hidden_state.mean(
                        dim=1).to(self.device)
                elif pooling == "max":
                    batch_embeddings, _ = outputs.last_hidden_state.max(dim=1)
                elif pooling == "cls":
                    batch_embeddings = outputs.last_hidden_state[:, 0, :]
                elif pooling == "attention":
                    batch_embeddings = self.attention_pooling(
                        outputs.last_hidden_state)
                else:
                    raise ValueError(
                        "Invalid pooling type. Options include 'mean', 'max', and 'cls'.")

                if normalize:
                    batch_embeddings = torch.nn.functional.normalize(
                        batch_embeddings, p=2, dim=1)

                embeddings.append(batch_embeddings)

        if pooling == "attention":
            self.save_attention_vector()

        return torch.cat(embeddings, dim=0)

    def attention_pooling(self, embeddings: torch.Tensor) -> torch.Tensor:
        scores = torch.matmul(
            embeddings, self.attention_vector.unsqueeze(-1)).squeeze(-1)
        weights = torch.nn.functional.softmax(scores, dim=1)
        assert embeddings.size(1) == weights.size(
            1), "Embedding and weight dimensions do not match."
        weighted = embeddings * weights.unsqueeze(-1)
        pooled = weighted.sum(dim=1)
        return pooled

    def save_attention_vector(self):
        torch.save(self.attention_vector.cpu(), ATTENTION_VECTOR_PATH)

    def load_attention_vector(self) -> torch.Tensor:
        if os.path.exists(ATTENTION_VECTOR_PATH):
            return torch.load(
                ATTENTION_VECTOR_PATH, weights_only=True).to(self.device)
        else:
            # return torch.nn.Parameter(
            #     torch.randn(self.model.config.hidden_size)).to(self.device)
            return torch.randn(
                self.model.config.hidden_size).to(self.device)

    def save_embeddings(self, embeddings: torch.Tensor, file_path: str):
        torch.save(embeddings, file_path)

    def load_embeddings(self, file_path: str) -> torch.Tensor:
        return torch.load(file_path, weights_only=True)
