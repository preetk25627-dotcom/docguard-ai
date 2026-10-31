
import re
from pathlib import Path


def find_documentation_references(symbols, docs_directory="."):
    extensions = {".md", ".rst", ".txt"}
    results = []

    for path in Path(docs_directory).rglob("*"):
        if not path.is_file() or path.suffix not in extensions:
            continue

        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue

        for line_number, line in enumerate(lines, start=1):
            for symbol in symbols:
                pattern = rf"\b{re.escape(symbol)}\b"

                if re.search(pattern, line):
                    results.append({
                        "document": str(path),
                        "line_number": line_number,
                        "symbol": symbol,
                        "documentation_sentence": line.strip()
                    })

    return results

def detect_mapped_drift(code, references):
    from src.analyzer import detect_documentation_drift

    issues = []

    for reference in references:
        result = detect_documentation_drift(
            code,
            reference["documentation_sentence"]
        )

        for issue in result:
            if issue["parameter"] == reference["symbol"]:
                issues.append({
                    **issue,
                    "document": reference["document"],
                    "line_number": reference["line_number"]
                })

    return issues
