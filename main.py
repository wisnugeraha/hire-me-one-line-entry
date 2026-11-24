#!/usr/bin/env python3
import pathlib

# One line, at most 200 characters: the pitch that gets you hired.
# Fresh, concrete, low-risk — a real promise, not a slogan.
LINE = (
    "I ship your stalled project this week for one sprint of your pay: "
    "you pick the blocker, I come back Friday with it working."
)


def main():
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"line is {len(text)} chars, must be 1..200")
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
