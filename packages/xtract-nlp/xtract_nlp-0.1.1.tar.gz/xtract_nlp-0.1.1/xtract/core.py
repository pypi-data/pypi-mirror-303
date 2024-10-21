import torch
from xtract.embedding import EmbeddingModel, PoolingType
from xtract.codebase import CodebaseProcessor
from xtract.query import QueryProcessor
from typing import List

# TODO(justin): cache for different directories
# - generate hash str from absolute path
# - store in temp directory accordingly, cross platform impl.
EMBEDDINGS_FILE = "code_embeddings.pt"
CODE_CHUNKS_FILE = "code_chunks.pt"


def process_code(codebase_path: str) -> int:
    """
    Process the codebase into chunks of code and save them.
    """
    processor = CodebaseProcessor(codebase_path)
    processor.load_codebase()
    code_chunks = processor.get_code_chunks()
    torch.save(code_chunks, CODE_CHUNKS_FILE)
    return len(code_chunks)


def generate_embeddings(
    model_name: str = "microsoft/codebert-base",
    normalize: bool = True,
    pooling: PoolingType = "mean"
) -> int:
    """
    Generate embeddings for the codebase and save them.
    """
    chunks = torch.load(CODE_CHUNKS_FILE, weights_only=True)
    model = EmbeddingModel(model_name)
    embeddings = model.generate_embeddings(
        chunks,
        normalize=normalize,
        pooling=pooling
    )
    model.save_embeddings(embeddings, EMBEDDINGS_FILE)
    return len(embeddings)


def query_code(
    query: str,
    model_name: str = "microsoft/codebert-base",
    count: int = 5,
    pooling: PoolingType = "mean",
    preprocess: bool = True,
    visualize: bool = False
) -> List[str]:
    """
    Query the codebase and return the top 'count' most relevant code snippets.
    """
    model = EmbeddingModel(model_name)
    embeddings = model.load_embeddings(
        EMBEDDINGS_FILE).to(model.device)
    chunks = torch.load(CODE_CHUNKS_FILE, weights_only=True)
    processor = QueryProcessor(
        model, chunks, embeddings)
    return processor.query(
        query,
        count=count,
        pooling=pooling,
        preprocess=preprocess,
        visualize=visualize,
    )
