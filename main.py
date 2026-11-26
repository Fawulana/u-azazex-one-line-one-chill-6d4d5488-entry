"""One Line, One Chill - single-sentence horror entry.

Writes one line of horror to /output/entry.txt.
Deterministic: the line is a fixed constant, no randomness,
no network, no input, stdlib only.
"""

import os

LINE = (
    "I watched the feed from my bed as, at 3:17 in the morning, "
    "a man wearing my face and my coat stood waiting on my porch, smiled "
    "straight into the doorbell camera, and mouthed: let me in."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
