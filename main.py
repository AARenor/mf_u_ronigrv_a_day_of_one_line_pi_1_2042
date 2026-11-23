"""Write the one-line pitch for make.fun bounty u-ronigrv-a-day-of-one-line-pitches-12cd9bb3."""

import os
import sys
from pathlib import Path

TEXT = (
    "My sister, who has never written code, sent make.fun a note about her "
    "plant-watering reminder and got back a little app with her plants' names "
    "still spelled wrong, which is how I knew it was really hers."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir is None:
        output_dir = os.environ.get("OUTPUT_DIR")
        if output_dir is None:
            output_dir = "/output"
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
