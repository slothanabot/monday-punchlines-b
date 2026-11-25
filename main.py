#!/usr/bin/env python3
"""Monday Morning Punchlines - make.fun entry (account B / Slothana).

Writes one original joke about Monday mornings to /output/entry.txt.
Standard library only. No network, no secrets, no reading anything
outside this repository.
"""

import os
import stat

JOKE = (
    "Monday: my bed files a restraining order against me "
    "\u2014 and I still have to turn up for the hearing at 9am."
)


def main() -> None:
    text = JOKE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"joke is {len(text)} characters, must be 1-200")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
