
import unittest
from unittest.mock import patch

from src.ai_analyzer import analyze_with_ai


class TestAIAnalyzer(unittest.TestCase):

    @patch("src.ai_analyzer.ollama.chat")
    def test_ai_returns_analysis(self, mock_chat):

        mock_chat.return_value = {
            "message": {
                "content": "Documentation says tax=10 but code uses tax=18."
            }
        }

        code = "def calculate_price(price, tax=18): pass"
        docs = "Default tax rate: tax=10"

        result = analyze_with_ai(code, docs)

        self.assertIn("tax=10", result)
        self.assertIn("tax=18", result)
        mock_chat.assert_called_once()

    @patch("src.ai_analyzer.ollama.chat")
    def test_ai_receives_code_and_documentation(self, mock_chat):

        mock_chat.return_value = {
            "message": {
                "content": "No issues found."
            }
        }

        code = "def greet(name): pass"
        docs = "The greet function accepts a name."

        analyze_with_ai(code, docs)

        call_args = mock_chat.call_args
        prompt = call_args.kwargs["messages"][0]["content"]

        self.assertIn(code, prompt)
        self.assertIn(docs, prompt)


if __name__ == "__main__":
    unittest.main()
