import os
from typing import List
from xtract.codebase.parser import parse_python_code


class CodebaseProcessor:

    def __init__(self, codebase_path: str):
        self.codebase_path = codebase_path
        self.code_chunks = []

    def load_codebase(self):
        for root, dirs, files in os.walk(self.codebase_path):
            for file in files:
                file_path = os.path.join(root, file)
                # TODO(justin): language support: JS/TS, Go, C/C++, Java, C#, Rust, PHP
                if file.endswith(".py"):
                    with open(file_path, "r", encoding="utf-8") as f:
                        code = f.read()
                        chunks = self.tokenize_code(file, code)
                        self.code_chunks.extend(chunks)

    def tokenize_code(self, file_name: str, code: str) -> List[str]:
        if file_name.endswith(".py"):
            return parse_python_code(code)
        return []

    def get_code_chunks(self) -> list:
        return self.code_chunks
