"""Entry for the make.fun bounty "Funniest One-Line Out-of-Office Reply".

The program writes a single funny line to /output/entry.txt. The
auto-reply admits the email has been filed under "things I will
pretend I never saw", which is exactly the message a colleague would
laugh at and still believe, because every office worker has a
filing system exactly like it. The gate allows 1 to 160
characters of UTF-8 text, so the line is checked against that
cap before it is written.
"""

import os

ENTRY = (
    "I am out of the office until Monday. Your email has been filed "
    "under \"things I will pretend I never saw\"."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
