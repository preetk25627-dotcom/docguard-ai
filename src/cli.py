
import argparse
import json

from src.analyzer import (
    detect_documentation_drift,
    generate_report
)
from src.ai_analyzer import analyze_with_ai


def main():
    parser = argparse.ArgumentParser(
        description="DocGuard AI - Documentation Drift Detector"
    )

    parser.add_argument("--code", required=True)
    parser.add_argument("--docs", required=True)
    parser.add_argument(
        "--ai",
        action="store_true",
        help="Enable AI-powered documentation analysis"
    )

    args = parser.parse_args()

    with open(args.code, "r", encoding="utf-8") as file:
        code = file.read()

    with open(args.docs, "r", encoding="utf-8") as file:
        documentation = file.read()

    # Rule-based analysis
    issues = detect_documentation_drift(code, documentation)
    report = generate_report(issues)

    # AI-powered analysis (optional)
    if args.ai:
        print("Running Qwen AI analysis...")

        try:
            ai_result = analyze_with_ai(code, documentation)
            report["ai_analysis"] = ai_result

        except Exception as error:
            report["ai_analysis_error"] = str(error)

    print(json.dumps(report, indent=4))


if __name__ == "__main__":
    main()
