#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The excuse concept: take the classic developer alibi "it worked on my
machine" and escalate it until it collapses under its own logic. The
machine did work -- once -- but it is gone: wiped, sold, and last seen
reincarnated as a smart fridge. The claim stays technically true while
being completely useless as an excuse, which is exactly the joke: the
developer is not lying, the evidence has simply been liquidated and
reincarnated as kitchen hardware.

Brief compliance: the output is a single line, well under the 200
character limit, with no leading or trailing whitespace and no double
spaces, and it names both a machine ("my machine", "smart fridge") and
the failure ("worked", "wiped", "sold").
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

    # Gate: no leading/trailing whitespace and no double spaces.
    if line != EXCUSE or line != line.strip():
        print("error: excuse has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "  " in line:
        print("error: excuse contains double spaces", file=sys.stderr)
        return 1

    # Gate: it must name a machine or device and a failure word,
    # so the joke is anchored in the classic developer-excuse shape.
    lowered = line.lower()
    if not any(w in lowered for w in ("machine", "fridge", "server", "laptop")):
        print("error: excuse must name a machine or device", file=sys.stderr)
        return 1
    if not any(w in lowered for w in ("worked", "wiped", "sold", "failed", "broke")):
        print("error: excuse must include a failure word", file=sys.stderr)
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
