
import unittest
import tempfile
from pathlib import Path
from src.documentation_mapper import (
    find_documentation_references,
    detect_mapped_drift
)

from src.documentation_mapper import find_documentation_references


class TestDocumentationMapper(unittest.TestCase):

    def test_finds_symbol_in_documentation(self):
        with tempfile.TemporaryDirectory() as directory:
            doc = Path(directory) / "README.md"
            doc.write_text(
                "The calculate_price function calculates the price.",
                encoding="utf-8"
            )

            results = find_documentation_references(
                ["calculate_price"],
                directory
            )

            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]["line_number"], 1)
    def test_detects_mapped_default_mismatch(self):
        code = "def calculate_price(price, tax=18): pass"

        references = [{
            "document": "README.md",
            "line_number": 1,
            "symbol": "tax",
            "documentation_sentence": "Default tax rate: tax=10"
        }]

        issues = detect_mapped_drift(code, references)

        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]["code_value"], "18")
        self.assertEqual(issues[0]["documentation_value"], "10")
        self.assertEqual(issues[0]["line_number"], 1)


if __name__ == "__main__":
    unittest.main()
