import unittest

from src.analyzer import detect_documentation_drift


class TestDocGuard(unittest.TestCase):

    def test_detects_mismatch(self):
        code = "def calculate_price(price, tax=18): pass"
        docs = "Default tax: tax=10"

        issues = detect_documentation_drift(code, docs)

        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]["code_value"], "18")
        self.assertEqual(
            issues[0]["documentation_value"], "10"
        )

    def test_no_mismatch(self):
        code = "def calculate_price(price, tax=18): pass"
        docs = "Default tax: tax=18"

        issues = detect_documentation_drift(code, docs)

        self.assertEqual(len(issues), 0)
    def test_missing_documentation(self):
        code = "def calculate_price(price, tax=18): pass"
        docs = "This function calculates the final price."

        issues = detect_documentation_drift(code, docs)

        self.assertEqual(len(issues), 1)
        self.assertIsNone(issues[0]["documentation_value"])
        self.assertIn("missing", issues[0]["issue"])


if __name__ == "__main__":
    unittest.main()