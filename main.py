"""One line: the funniest single-line resignation letter.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The joke pairs the office's most hated machine with the resigning
human: both jammed, both done, and the letter blames the printer
first.
"""

import os
import sys

LINE = (
    "I resign, effective immediately: the printer has jammed "
    "for the last time, and frankly, so have I."
)


def main() -> int:
    if not 1 <= len(LINE) <= 140:
        print(f"error: line is {len(LINE)} chars, must be 1-140",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
