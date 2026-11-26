#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one voicemail greeting, recorded as if by a cat, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
The line was picked by an internal pairwise tournament among 12
original candidates, judged against the published judge brief:
a real cat voicemail, a cat-specific joke, a clear cat attitude,
a fast punch when spoken aloud, and fresh wording.
"""

import os

ENTRY = "Hi, you've reached the cat. If it's about the vase, I did it. If it's food, hurry up. Beep."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
