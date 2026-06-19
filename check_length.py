import pathlib
import sys

for file in pathlib.Path(".").glob("*.py"):
    lines = file.read_text().splitlines()

    if len(lines) > 100:
        print(f"{file} exceeds 100 lines")
        sys.exit(1)

print("All files below 100 lines")
