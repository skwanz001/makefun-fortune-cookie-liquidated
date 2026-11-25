"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line to /output/entry.txt.

The line (10 words, 54 characters):
    Your lucky numbers were sold to cover the margin call.

Angle: the most iconic fortune-cookie trope -- your lucky numbers --
twisted into the loss itself. The thing that was supposed to bring luck
was already sold to pay for the margin call. Oracular opening, rueful
punchline, one breath.
"""

import os

FORTUNE = "Your lucky numbers were sold to cover the margin call."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    words = FORTUNE.split()
    assert 1 <= len(words) <= 20, f"word count {len(words)} exceeds 20"
    assert 1 <= len(FORTUNE) <= 160, f"char count {len(FORTUNE)} exceeds 160"
    assert FORTUNE.strip(), "fortune must not be blank"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
