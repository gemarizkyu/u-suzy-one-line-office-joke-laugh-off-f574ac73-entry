"""One-line office joke.

Writes a single original one-line office joke to /output/entry.txt.
Deterministic: no clock, no randomness, no network, no model calls.
The line is 136 characters, one line, inside the 1-200 gate.
"""

from pathlib import Path

SETUP = "I brought a plant to my desk to boost morale;"
DETAIL = "it died in a week,"
PUNCH = "and HR wrote me up for failing to maintain a positive work environment."


def build_joke() -> str:
    """Assemble the single joke line from its parts.

    Setup frames a relatable office gesture (a desk plant for morale);
    the middle turns it (the plant dies in a week); the punch lands on
    the last words, with HR treating a dead plant as a conduct issue,
    so the absurd escalation arrives fast and the line is one a reader
    would repeat to a coworker.
    """
    return f"{SETUP} {DETAIL} {PUNCH}"


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    line = build_joke()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"joke line is {len(line)} characters, must be 1-200")
    if "\n" in line or "\r" in line:
        raise ValueError("joke line must be a single line")
    # Write exactly the joke line: no trailing newline, so the file
    # holds one line of 1-200 characters and nothing else.
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
