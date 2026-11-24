"""Two Days of Excuses — one-line AI excuse for a missed deadline.

Writes the entry to /output/entry.txt. Stdlib only, fully deterministic:
the same single line on every run.
"""

import hashlib
import os

ENTRY = (
    "I didn't miss the deadline \u2014 it moved to yesterday while I was "
    "busy being 99% confident I'd finish on time."
)


def main() -> None:
    # Self-check the gate: 1-200 chars, exactly one line, non-blank.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert ENTRY.strip(), "entry must not be blank"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    digest = hashlib.sha256((ENTRY + "\n").encode("utf-8")).hexdigest()
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars, sha256 {digest})")


if __name__ == "__main__":
    main()
