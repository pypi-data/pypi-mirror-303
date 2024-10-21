# xTrAct-NLP: A Code Query and Embedding Toolkit

**xTrAct-NLP** is a toolkit designed to process codebases, generate embeddings from code chunks, and retrieve relevant snippets using natural language queries. It uses state-of-the-art models to create meaningful embeddings and facilitates sophisticated query expansion and ranking mechanisms. This project is especially useful for developers looking to integrate NLP into code search engines.

## Features

- **Code Parsing**: Supports code parsing using AST to extract functions and classes as code chunks.
- **Embedding Generation**: Generates embeddings from code chunks using HuggingFace models (e.g., CodeBERT, T5).
- **Query Expansion**: Automatically expands natural language queries with relevant technical terms using language models.
- **Reranking**: Supports BM25 and cosine similarity-based ranking for more relevant code retrieval.
- **Visualization**: Supports both scatter plots (for PCA and t-SNE) and heatmaps to visually analyze and compare code embeddings.

## Installation

```bash
pip install xtract-nlp
```

For development:

```bash
git clone https://github.com/ooojustin/xTrAct-NLP.git
cd xTrAct-NLP
pip install -e .
```

## Usage

### CLI Usage

1. **Process Codebase:**

   ```bash
   xtract process <path_to_codebase>
   ```

2. **Generate Embeddings:**

   ```bash
   xtract generate
   ```

3. **Query the Codebase:**
   ```bash
   xtract query "parse python code using ast"
   ```

### Python Library Usage

```python
from xtract.core import process_code, generate_embeddings, query_code

# Process codebase
num_chunks = process_code("/path/to/codebase")

# Generate embeddings
num_embeddings = generate_embeddings()

# Query codebase
results = query_code("parse python code using ast")
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ooojustin/xTrAct-NLP/blob/main/LICENSE) for more details.
