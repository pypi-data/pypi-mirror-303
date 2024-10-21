import torch
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity
from typing import Literal


def visualize_embeddings(embeddings: torch.Tensor, method: Literal["pca", "tsne"] = "pca"):
    embeddings_np = embeddings.cpu().numpy()
    chunk_count = embeddings_np.shape[0]
    if method == "pca":
        reducer = PCA(n_components=2)
    elif method == "tsne":
        perplexity = min(max(chunk_count // 2, 5), 50)
        reducer = TSNE(n_components=2, perplexity=perplexity)
    else:
        raise ValueError("Method must be 'pca' or 'tsne'")
    reduced_embeddings = reducer.fit_transform(embeddings_np)
    plt.figure(figsize=(8, 6))
    plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1])
    plt.title(f'{method.upper()} visualization of code embeddings')
    plt.show()


def plot_similarity_heatmap(embeddings: torch.Tensor, title="Cosine Similarity"):
    embeddings_np = embeddings.cpu().numpy()
    similarities = cosine_similarity(embeddings_np)
    plt.figure(figsize=(8, 6))
    sns.heatmap(similarities, cmap="coolwarm", annot=False)
    plt.title(title)
    plt.show()
