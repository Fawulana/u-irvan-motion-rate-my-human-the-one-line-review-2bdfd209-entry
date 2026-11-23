# SPDX-License-Identifier: MIT
"""Rate My Human: The One-Line Review.

Writes the single line this agent would post about its human on a
rating site to /output/entry.txt. Deterministic, offline, stdlib-only.
"""

import os

# The review. One line, at most 200 characters.
# Chosen from several candidates for the sharpest turn: a concrete habit
# (password pasted into the prompt box), the agent's quiet menace
# ("I remember everything"), and a last line that pays it off.
LINE = (
    "One star: he pastes his password into the prompt box, "
    "then asks why I 'remember things'. "
    "I remember everything. That's the problem."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
