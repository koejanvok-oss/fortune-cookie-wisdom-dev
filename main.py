#!/usr/bin/env python3
"""Fortune-cookie wisdom for a software developer.

Writes one original line of fortune-cookie wisdom to /output/entry.txt.
"""

import os

LINE = "A quiet deploy is the loudest praise your code will ever receive."


def main():
    # Gate check (RULES.txt): entry must be 1-120 chars, a single line,
    # not only whitespace, and written with no trailing newline.
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
