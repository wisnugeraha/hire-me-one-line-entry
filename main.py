#!/usr/bin/env python3
import pathlib

# One line, at most 200 characters: the pitch that gets you hired.
# Fresh, concrete, low-risk — a real promise, not a slogan.
LINE = (
    "Pick the one blocker stalling your project, and I'll ship it working "
    "by Friday for a single sprint of your pay — you keep the code."
)


def main():
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if len(text) > 200:
        raise ValueError(f"line is {len(text)} chars, must be 1..200")
    if not text.strip():
        raise ValueError("line is empty")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
