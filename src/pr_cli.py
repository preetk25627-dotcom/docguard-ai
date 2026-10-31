
import json

from src.pr_analyzer import get_changed_files, classify_changed_files


def main():
    files = get_changed_files()
    result = classify_changed_files(files)

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
