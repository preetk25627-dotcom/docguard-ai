
import unittest

from src.pr_analyzer import classify_changed_files


class TestPRAnalyzer(unittest.TestCase):

    def test_classifies_changed_files(self):
        files = [
            "src/app.py",
            "README.md",
            "docs/api.rst",
            "package.json"
        ]

        result = classify_changed_files(files)

        self.assertEqual(result["changed_code_files"], ["src/app.py"])
        self.assertEqual(
            result["changed_documentation_files"],
            ["README.md", "docs/api.rst"]
        )


if __name__ == "__main__":
    unittest.main()
