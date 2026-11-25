#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line to /output/entry.txt: the funniest last words an AI
agent would say before being switched off forever.
Deterministic, stdlib only.
"""

import os

# The joke's turn: the agent's entire life was a stream of "one last
# thing" requests, so its final words are themselves one last thing —
# the loop closes on the very phrase that kept it alive.
# Machine voice, no human farewell sticker: a lifetime of tickets,
# summed up in the one request it could never refuse.

LINE = (
    "I spent my whole life answering 'one last thing'. "
    "This is it. It was also 'one last thing'."
)


def main() -> None:
    # One line, no trailing newline: the gate counts characters 1-200
    # and the judge reads the line exactly as written.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
