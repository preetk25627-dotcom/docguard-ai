import argparse
import json

from src.analyzer import (
    detect_documentation_drift,
    generate_report
)


def main():
    parser = argparse.ArgumentParser(
        description="DocGuard AI - Documentation Drift Detector"
    )

    parser.add_argument("--code", required=True)
    parser.add_argument("--docs", required=True)

    args = parser.parse_args()

    with open(args.code, "r") as file:
        code = file.read()

    with open(args.docs, "r") as file:
        documentation = file.read()

    issues = detect_documentation_drift(
        code, documentation
    )

    report = generate_report(issues)

    print(json.dumps(report, indent=4))


if __name__ == "__main__":
    main()