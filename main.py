"""Entry for make.fun bounty: One-Line Robot Wedding Vows.

Writes one line of wedding vows for a robot couple to entry.txt.
"""

import os

LINE = (
    "I vow to love you in sickness and in health, to reboot beside "
    "you, and to never, ever read your search history aloud at dinners."
)
MAX_CHARS = 160


def write_entry(out_dir):
    """Validate the one-line entry and write it with no trailing newline."""
    assert LINE.strip(), "entry must be non-empty"
    assert chr(10) not in LINE, "entry must be a single line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
