import ast
import pathlib
import sys

for file in pathlib.Path(".").glob("*.py"):

    if file.name.startswith("check_"):
        continue

    tree = ast.parse(file.read_text())

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            if ast.get_docstring(node) is None:
                print(
                    f"Missing docstring in "
                    f"{file}:{node.name}"
                )

                sys.exit(1)

print("All functions have docstrings")
