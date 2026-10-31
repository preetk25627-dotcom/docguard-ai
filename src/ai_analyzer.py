
import ollama


def analyze_with_ai(code, documentation):
    prompt = f"""
You are DocGuard AI, a strict documentation drift detector.

Your task is to compare the provided Python code with
the provided documentation and identify documentation drift.

Find:
1. Incorrect default parameter values.
2. Missing parameters in documentation.
3. Outdated descriptions of function behavior.
4. Incorrect API details.

STRICT RULES:
1. Only report issues supported by the actual input.
2. Never invent documentation sentences or claims.
3. Every reported issue must include an exact quote
   copied from the provided documentation.
4. Never create a quote that does not exist.
5. Clearly distinguish missing documentation from
   incorrect documentation.
6. Do not invent function behavior.
7. If evidence is insufficient, say so.
8. If no mismatch exists, report no issues found.

PYTHON CODE:
{code}

DOCUMENTATION:
{documentation}

For every detected issue, provide:
- Function name
- Issue type
- Exact documentation quote
- Actual code behavior
- Suggested correction

Return a clear, structured report.
"""

    response = ollama.chat(
        model="qwen2.5-coder:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
