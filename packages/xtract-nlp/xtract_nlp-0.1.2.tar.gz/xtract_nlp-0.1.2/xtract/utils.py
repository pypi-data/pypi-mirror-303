import nltk
import shutil
from typing import Any


def rmdir(path: str):
    try:
        shutil.rmtree(path)
        print(f"Directory '{path}' has been deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied: Unable to delete '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_stopwords():
    """
    Downloads NLTK stopwords if they are not already available.
    """
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')


def clean_token(token: str) -> str:
    """
    Clean tokens by removing marks/special chars added by different tokenizers.
    """
    token, erase= token.lower(), ["##", "Ġ", "ġ", "▁"]
    for e in erase:
        token = token.replace(e, "")
    token = token[1:] if token.startswith("'") else token
    return token.strip()

def get_full_module_path(variable: Any) -> str:
    variable_type = type(variable)
    module = variable_type.__module__
    class_name = variable_type.__name__
    return f"{module}.{class_name}"
