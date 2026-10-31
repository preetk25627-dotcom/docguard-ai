
import ast
from pathlib import Path

from src.pr_analyzer import get_changed_files
from src.analyzer import detect_documentation_drift


def extract_functions(code):
    tree = ast.parse(code)

    return [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]


def run_pipeline():
    changed_files = get_changed_files()

    code_files = [
        file for file in changed_files
        if file.endswith(".py") and Path(file).is_file()
    ]

    documentation_files = []

    for extension in ("*.md", "*.rst", "*.txt"):
        documentation_files.extend(Path(".").rglob(extension))

    report = []

    for code_file in code_files:
        code = Path(code_file).read_text(encoding="utf-8")
        functions = extract_functions(code)

        for doc_file in documentation_files:
            if any(part in {".git", ".venv", "venv"} for part in doc_file.parts):
                continue

            docs = doc_file.read_text(encoding="utf-8")

            for function in functions:
                if function not in docs:
                    continue

                issues = detect_documentation_drift(code, docs)

                for issue in issues:
                    if issue["function"] == function:
                        report.append({
                            "code_file": code_file,
                            "documentation_file": str(doc_file),
                            **issue
                        })

    return {
        "total_issues": len(report),
        "issues": report
    }
