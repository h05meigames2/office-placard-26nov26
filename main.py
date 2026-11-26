#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest — make.fun entry.

Writes a single museum placard line for an ordinary office object
(a binder clip), treated as an ancient artifact, to /output/entry.txt.
Deterministic, no network, no input. Gate: UTF-8 text, 1-180 chars.

Bounty: https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2
"""

import os

ENTRY = (
    "Binder clip, c. 2015. Spring steel, black enamel. A jaw trap for "
    "loose papers: once clamped, no document ever escaped. "
    "Donated by a survivor of the Great Audit."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 180, f"entry must be 1-180 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} chars to /output/entry.txt:")
    print(line)


if __name__ == "__main__":
    main()
