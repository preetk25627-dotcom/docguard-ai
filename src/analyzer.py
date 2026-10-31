
import ast
import re


def get_function_defaults(code):
    tree = ast.parse(code)
    functions = {}

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            defaults = {}
            args = node.args.args
            default_values = node.args.defaults

            if default_values:
                for arg, default in zip(args[-len(default_values):], default_values):
                    defaults[arg.arg] = ast.unparse(default)

            functions[node.name] = defaults

    return functions


def get_documentation_evidence(documentation, parameter):
    for line_number, line in enumerate(documentation.splitlines(), start=1):
        if parameter in line:
            return {
                "line_number": line_number,
                "documentation_line": line.strip()
            }

    return None



def detect_documentation_drift(code, documentation):
    functions = get_function_defaults(code)
    issues = []

    for function_name, defaults in functions.items():
        for parameter, code_value in defaults.items():

            pattern = rf"\b{re.escape(parameter)}\s*=\s*(\d+)"
            match = re.search(pattern, documentation)

            if match:
                doc_value = match.group(1)

                if doc_value != code_value:
                    evidence = get_documentation_evidence(
                        documentation, parameter
                    )

                    issues.append({
                        "function": function_name,
                        "parameter": parameter,
                        "code_value": code_value,
                        "documentation_value": doc_value,
                        "issue": f"Mismatch: code has {code_value}, documentation has {doc_value}",
                        "evidence": evidence
                    })

            else:
                evidence = get_documentation_evidence(
                    documentation, parameter
                )

                issues.append({
                    "function": function_name,
                    "parameter": parameter,
                    "code_value": code_value,
                    "documentation_value": None,
                    "issue": f"Default value {code_value} is missing from documentation",
                    "evidence": evidence
                })

    return issues



def generate_report(issues):
    return {
        "total_issues": len(issues),
        "status": "Issues found" if issues else "No issues found",
        "issues": issues
    }
