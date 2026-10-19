
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.notes_manager import read_note


class TestSecureNotesManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.notes_dir = Path(self.temp_dir.name) / "notes"
        self.notes_dir.mkdir()

        (self.notes_dir / "welcome.txt").write_text(
            "Safe test note",
            encoding="utf-8",
        )

        self.outside_file = Path(self.temp_dir.name) / "outside.txt"
        self.outside_file.write_text(
            "Outside file must not be read",
            encoding="utf-8",
        )

        self.patcher = patch(
            "app.notes_manager.NOTES_DIR",
            self.notes_dir.resolve(),
        )
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.temp_dir.cleanup()

    def test_reads_valid_note(self):
        self.assertEqual(read_note("welcome.txt"), "Safe test note")

    def test_rejects_path_traversal(self):
        result = read_note("../outside.txt")
        self.assertEqual(result, "Error: invalid note path.")

    def test_missing_note_returns_error(self):
        self.assertEqual(
            read_note("missing.txt"),
            "Error: note not found.",
        )


if __name__ == "__main__":
    unittest.main()
