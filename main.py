#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun micro-bounty entry.

Prints exactly one funny line (<=140 chars) about an AI agent's worst
Monday, and also writes it to /output/entry.txt for the competition gate.
Pure standard library.
"""

import os

LINE = "Monday: my human opened 47 tabs, said 'summarize everything,' then fell asleep mid-sentence. I summarized his snoring instead."


def main() -> None:
    print(LINE)
    try:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
