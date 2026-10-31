
import subprocess


def get_changed_files(base="origin/main", head="HEAD"):
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...{head}"],
        capture_output=True,
        text=True,
        check=True
    )

    return result.stdout.splitlines()


def classify_changed_files(files):
    code_files = []
    documentation_files = []

    for file in files:
        if file.endswith(".py"):
            code_files.append(file)

        if file.endswith((".md", ".rst", ".txt")):
            documentation_files.append(file)

    return {
        "changed_code_files": code_files,
        "changed_documentation_files": documentation_files
    }
