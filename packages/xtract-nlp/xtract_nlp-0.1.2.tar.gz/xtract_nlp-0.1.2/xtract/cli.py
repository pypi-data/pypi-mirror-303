import click
from xtract.core import process_code, generate_embeddings, query_code

from xtract.embedding import PoolingType
pooling_types = list(PoolingType.__args__)


@click.group()
def cli():
    """CLI for querying codebase using embeddings."""
    pass


@cli.command()
@click.argument("codebase_path")
def process(codebase_path):
    """
    Load and process the codebase into chunks.
    """
    num_chunks = process_code(codebase_path)
    click.echo(f"Codebase processed: {num_chunks} chunks found.")


@cli.command()
@click.option("--model", "-m", default="microsoft/codebert-base", help="Name of the embedding model to use.")
@click.option("--pooling", "-p", default="mean", type=click.Choice(pooling_types, case_sensitive=False), help=f"Pooling strategy to use: {pooling_types}")
@click.option("--no_normalization", "-nn", is_flag=True, help="Disable normalization of generated embeddings.")
def generate(model, pooling, no_normalization):
    """
    Generate embeddings for the codebase.
    """
    num_embeddings = generate_embeddings(
        model_name=model,
        normalize=not no_normalization,
        pooling=pooling
    )
    click.echo(f"Embeddings generated: {num_embeddings} embeddings saved.")


@cli.command()
@click.argument("query")
@click.option("--model", "-m", default="microsoft/codebert-base", help="Name of the embedding model to use.")
@click.option("--count", "-c", default=5, help="Number of top results to return.")
@click.option("--pooling", "-p", default="mean", type=click.Choice(pooling_types, case_sensitive=False), help=f"Pooling strategy to use: {pooling_types}")
@click.option("--visualize", "-v", is_flag=True, help="Visualize the code embeddings and their similarity heatmap.")
@click.option("--no_preprocessing", "-np", is_flag=True, help="Disable query preprocessing (via keyword extraction).")
def query(query, model, count, pooling, visualize, no_preprocessing):
    """
    Query the codebase for relevant code snippets.
    """
    results = query_code(
        query,
        model_name=model,
        count=count,
        pooling=pooling,
        preprocess=not no_preprocessing,
        visualize=visualize
    )
    click.echo(f"Top {count} results:")
    for i, snippet in enumerate(results):
        click.echo(f"\nResult {i+1}:\n{snippet}\n")


if __name__ == "__main__":
    cli()
