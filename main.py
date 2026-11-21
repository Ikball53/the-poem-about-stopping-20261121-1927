"""Emit a short first-person poem about choosing to stop and stay.

The text is fixed in this file so every run produces identical bytes.
Only the standard library is used, and nothing touches the network.
"""

from pathlib import Path

# Kept as one literal so the rhythm is visible at a glance while editing.
POEM_TEXT = (
    "I had one shoe on, bag by the door, my thumb pressing the latch. "
    "The hallway smelled of rice left cooling on the stove. "
    "I took the shoe off, set the bag down where it belonged, and stayed "
    "at the table until my breathing matched the ticking clock and let my hands loosen."
)

OUTPUT_LOCATION = Path("/output/entry.txt")


def render_entry() -> bytes:
    """Return the poem encoded exactly as it should land on disk."""
    return POEM_TEXT.encode("utf-8")


def main() -> None:
    """Create the output folder if needed, then write the poem file."""
    OUTPUT_LOCATION.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_LOCATION.write_bytes(render_entry())


if __name__ == "__main__":
    main()
