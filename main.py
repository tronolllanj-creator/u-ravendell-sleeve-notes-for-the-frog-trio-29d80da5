import os  # standard library only: no network, no file reads

"""Sleeve Notes for the Frog Trio bounty."""

TEXT = """The Lily Pad Sessions
In the back booth of the dampest cellar on 4th Street, Hopper blows a low alto saxophone, driven by Mud on upright bass and Croak on the small drum kit. They don't play for tourists."""


def main() -> None:
    assert 1 <= len(TEXT) <= 400, "Text length out of bounds (1-400 characters)"

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, "entry.txt")
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()