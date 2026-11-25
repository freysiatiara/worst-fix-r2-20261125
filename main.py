"""Worst Fix Ever: Funniest Commit Message (round 2).

Writes a single commit message line to /output/entry.txt.
Standard library only.
"""

import os
import stat

LINE = "fix: infinite loop by adding a second one to cancel it out"


def main():
    if not 1 <= len(LINE) <= 100:
        raise SystemExit("LINE must be 1-100 characters")

    output_dir = (
        os.environ.get("ENTRY_OUTPUT")
        or os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )
    output_path = os.path.join(output_dir, "entry.txt")

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
