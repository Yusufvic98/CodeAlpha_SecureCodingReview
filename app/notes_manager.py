
from pathlib import Path


NOTES_DIR = (Path(__file__).resolve().parent / "notes").resolve()


def read_note(filename):
    """Read a note only when its resolved path stays inside NOTES_DIR."""
    try:
        note_path = (NOTES_DIR / filename).resolve()

        if not note_path.is_relative_to(NOTES_DIR):
            return "Error: invalid note path."

        if not note_path.is_file():
            return "Error: note not found."

        return note_path.read_text(encoding="utf-8")

    except (OSError, ValueError, RuntimeError):
        return "Error: unable to read note."


if __name__ == "__main__":
    name = input("Enter note filename: ").strip()
    print(read_note(name))

