#!/usr/bin/env python3
"""The 3AM Fridge Text — a make.fun entry.

The program writes the single line a smart fridge would text its owner
at 3 a.m. to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The line is 128 characters, inside the competition's gate of 1 to 140
characters of UTF-8 text. Standard library only, no network, and
deterministic: the same bytes on every run.
"""

import os

LINE = "3:00 a.m. The cake is gone. I said nothing for six hours because I respect you, but I keep the log, and the log is disappointed."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry file holds exactly the one line: no trailing newline, so
    # the text the judge reads is the line itself, byte for byte. Write
    # it as UTF-8 bytes so the output is identical on every platform.
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as fh:
        fh.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
