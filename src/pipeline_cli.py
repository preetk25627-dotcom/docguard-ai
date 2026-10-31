import json
from src.pipeline import run_pipeline

if __name__ == "__main__":
    result = run_pipeline()
    print(json.dumps(result, indent=4))