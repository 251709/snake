import unittest
import tempfile

from pathlib import Path

from src.models.highscore import HighScore


class TestHighScore(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "highscore.txt"
        self.high_score = HighScore(self.file_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_load_without_file(self):
        self.assertEqual(self.high_score.load(), 0)

    def test_save_and_load(self):
        self.high_score.save(10)

        self.assertEqual(self.high_score.load(), 10)

    def test_update_new_record(self):
        result = self.high_score.update(15)

        self.assertEqual(result, 15)
        self.assertEqual(self.high_score.load(), 15)

    def test_update_lower_score(self):
        self.high_score.save(20)

        result = self.high_score.update(10)

        self.assertEqual(result, 20)
        self.assertEqual(self.high_score.load(), 20)

    def test_update_equal_score(self):
        self.high_score.save(20)

        result = self.high_score.update(20)

        self.assertEqual(result, 20)


if __name__ == "__main__":
    unittest.main()
