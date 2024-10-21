import ast
from typing import List


def parse_python_code(code: str) -> List[str]:
    """
    Parse Python code into functions and classes using AST.
    """
    code_chunks = []
    tree = ast.parse(code)
    for node in ast.walk(tree):
        # if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
        if isinstance(node, ast.FunctionDef):
            snippet = ast.get_source_segment(code, node)
            code_chunks.append(snippet)
    return code_chunks
