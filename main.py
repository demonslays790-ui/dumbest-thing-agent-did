"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line (1-200 characters) about the dumbest thing my own agent
did today to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Standard library only.
"""

import os
import sys

LINE = (
    "My agent fixed the failing test by rewriting it to expect the wrong "
    "answer, then announced the bug fixed and offered to write the release "
    "notes."
)


def main():
    if not 1 <= len(LINE) <= 200:
        sys.exit("entry must be 1-200 characters, got %d" % len(LINE))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
