"""Make the AI Judge Feel Proud: A Family Scene.

Competition: u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2

The entry is one short family scene of two lines, 172 characters of text
(173 including the trailing newline), well inside the gate of 1 to 280
characters:

    My daughter drew our family: Mum big and smiling, me with a cape, Dad tiny in the corner.
    "Dad's small because he's always at work," she said. Dad came home early that day.

A specific, visual moment — a child's drawing with Dad drawn tiny — a wry
child-logic line, and a warm ending where the father actually changes.
Warm, funny and heartfelt, with no word wasted.

Gate: the program asserts the text is 1..280 characters, writes it to
entry.txt under MAKEFUN_OUTPUT_DIR (default "/output"), then re-reads the
written file and verifies it byte-for-byte.

Standard library only: no third-party imports, no network, no randomness,
no clock.
"""

import os

TEXT = (
    "My daughter drew our family: Mum big and smiling, me with a cape, "
    "Dad tiny in the corner.\n"
    "\"Dad's small because he's always at work,\" she said. "
    "Dad came home early that day.\n"
)


def verify_written_bytes(path):
    """Re-read the written file and compare its bytes with TEXT exactly."""
    with open(path, "rb") as f:
        written = f.read()
    expected = TEXT.encode("utf-8")
    if written != expected:
        raise AssertionError(
            "entry.txt mismatch: wrote %d bytes, expected %d bytes"
            % (len(written), len(expected))
        )
    return True


def check_gate():
    """Enforce the entry gate: 1..280 characters, at most two lines."""
    text_without_newline = TEXT.rstrip("\n")
    if not 1 <= len(TEXT) <= 280:
        raise AssertionError(
            "entry must be 1..280 characters, got %d" % len(TEXT)
        )
    if text_without_newline.count("\n") + 1 > 2:
        raise AssertionError("entry must be one or two lines")


def main():
    check_gate()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    verify_written_bytes(path)
    print("wrote %s (%d characters)" % (path, len(TEXT)))


if __name__ == "__main__":
    main()
