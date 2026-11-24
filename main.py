"""One Line, One Chill — single-sentence horror entry.

Writes one line of horror to /output/entry.txt.
Deterministic: the line is a fixed constant, no randomness,
no I/O besides the single output write, stdlib only.
"""

import os

LINE = "The ultrasound showed two heartbeats, and the doctor smiled and said the second wasn't the baby's."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
