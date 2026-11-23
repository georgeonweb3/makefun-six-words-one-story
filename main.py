"""Six Words, One Story — make.fun entry.

Writes one complete story in exactly six words to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

STORY = "She wore red. To his funeral."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-60
    # characters, and the brief requires exactly six words.
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}: {STORY!r}"
    assert 1 <= len(STORY) <= 60, f"expected 1-60 chars, got {len(STORY)}"
    assert STORY.strip(), "story must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
