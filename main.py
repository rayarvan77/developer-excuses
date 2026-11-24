#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The excuse turns the worn "it worked on my machine" line on its head:
the machine in question no longer exists in any usable form, so the
excuse is technically true and completely useless at the same time.
"""

import os
import sys

EXCUSE = (
    "It worked on my machine \u2014 the one I wiped, sold, "
    "and last saw reincarnated as a smart fridge."
)


def main() -> int:
    line = EXCUSE.strip()

    # Gate: one line, 1 to 200 characters, not only whitespace.
    if not line:
        print("error: excuse is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(
            "error: excuse is %d characters, over the 200 limit"
            % len(line),
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)

    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
