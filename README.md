# 🛡️ DocGuard AI

### Automated Documentation Drift Detection

**Keeping documentation synchronized with code changes.**

DocGuard AI is a documentation drift detection tool that helps developers identify outdated documentation when source code changes.

It analyzes code changes, identifies related documentation references, detects mismatches in documented default values, and generates evidence-based reports.

The project combines deterministic code analysis with optional local AI-powered analysis to help developers maintain accurate and reliable documentation.

---

## 🚨 The Problem

Documentation often becomes outdated when developers modify source code without updating the corresponding documentation.

For example:

**Updated Python code:**

```python
def calculate_price(price, tax=18):
    return price + (price * tax / 100)
```

**Outdated README documentation:**

```text
Default tax rate: tax=10
```

This creates confusion for developers who rely on documentation.

DocGuard AI aims to identify these inconsistencies and highlight the affected documentation.

---

## 💡 Our Solution

DocGuard AI provides an automated approach to detecting documentation drift.

Its core workflow includes:

1. Identifying changed source code files.
2. Extracting function names from Python code using AST.
3. Finding references to those functions in documentation.
4. Comparing documented default parameter values with actual code values.
5. Generating a structured report containing detected mismatches and documentation evidence.
6. Optionally using a local AI model to perform additional semantic analysis.

---

## ⚙️ How It Works

```text
       Git Changes
            |
            v
    Changed File Detection
            |
            v
     Python AST Analysis
            |
            v
   Documentation Mapping
            |
            v
    Drift Detection Engine
            |
            v
     Evidence-Based Report
            |
            v
       Optional AI Analysis
```

---

## ✨ Key Features

- **Changed File Detection:** Identifies modified files using Git diff.
- **Python AST Analysis:** Extracts function definitions from Python source code.
- **Documentation Mapping:** Finds function references in Markdown, RST and text documentation.
- **Default Value Validation:** Detects mismatches between documented and actual numeric default parameter values.
- **Evidence-Based Reporting:** Includes documentation references and line numbers for detected mismatches.
- **Local AI Integration:** Uses Qwen2.5-Coder through Ollama for optional AI-powered analysis.
- **Unit Testing:** Includes tests for code analysis, documentation mapping, PR analysis and AI integration.

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| Python AST | Source code analysis |
| Git | Changed file detection |
| Ollama | Local AI model execution |
| Qwen2.5-Coder 7B | AI-powered analysis |
| unittest | Automated testing |
| GitHub Actions | Continuous integration |

---

## 📁 Project Structure

```text
docguard-ai/
│
├── src/
│   ├── analyzer.py
│   ├── ai_analyzer.py
│   ├── documentation_mapper.py
│   ├── pipeline.py
│   ├── pipeline_cli.py
│   ├── pr_analyzer.py
│   └── pr_cli.py
│
├── tests/
│   ├── test_analyzer.py
│   ├── test_ai_analyzer.py
│   ├── test_documentation_mapper.py
│   └── test_pr_analyzer.py
│
├── examples/
│   ├── README.md
│   └── sample.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── HACKATHON.md
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/preetk25627-dotcom/docguard-ai.git

cd docguard-ai
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the test suite

```bash
python3 -m unittest discover -s tests -v
```

---

## 🧪 Usage

### Rule-Based Documentation Analysis

Run the analyzer against sample source code and documentation:

```bash
python3 -m src.cli \
  --code examples/sample.py \
  --docs examples/README.md
```

### AI-Powered Analysis

Install [Ollama](https://ollama.com/) and download the model:

```bash
ollama pull qwen2.5-coder:7b
```

Start Ollama, then run:

```bash
python3 -m src.cli \
  --code examples/sample.py \
  --docs examples/README.md \
  --ai
```

The AI analysis is optional. The basic rule-based analyzer does not require the model to be downloaded.

### Git Change Analysis

Fetch the latest remote changes:

```bash
git fetch origin
```

Identify changed files:

```bash
python3 -m src.pr_cli
```

### Integrated Detection Pipeline

```bash
python3 -m src.pipeline_cli
```

The pipeline compares changed Python files against documentation references and generates a JSON report.

---

## 📊 Example Detection

Given:

**Code:**

```python
def calculate_price(price, tax=18):
    return price + (price * tax / 100)
```

**Documentation:**

```text
Default tax rate: tax=10
```

DocGuard can identify:

| Field | Result |
|---|---|
| Function | calculate_price |
| Parameter | tax |
| Actual default | 18 |
| Documented default | 10 |
| Issue | Default value mismatch |

---

## 🤖 Why AI?

Traditional rule-based analysis is useful for detecting structured changes such as parameter defaults.

However, documentation can also describe behavior in natural language.

DocGuard integrates a locally running Qwen2.5-Coder model to provide additional analysis of code and documentation.

AI is an enhancement to the detection engine, not a replacement for deterministic analysis.

The system aims to provide evidence for reported issues rather than relying on unsupported AI-generated claims.

---

## 🔬 Current Limitations

DocGuard AI is an evolving prototype.

Currently supported:

- Python function extraction.
- Basic documentation reference matching.
- Numeric default parameter mismatch detection.
- Missing default-value documentation detection.
- Local AI-assisted analysis.
- Basic Git changed-file identification.

Further development is needed for:

- Complete GitHub Pull Request integration.
- Semantic mapping between indirectly related code and documentation.
- Configuration and API reference drift detection.
- More programming language support.
- Improved false-positive handling.
- Automated evidence-based PR annotations.

---

## 🔮 Future Roadmap

- GitHub Actions integration for automated PR analysis.
- More accurate code-to-documentation relationship mapping.
- Detection of outdated API parameters and configuration values.
- Exact source-code and documentation line references.
- Better semantic analysis of behavioral changes.
- Actionable Pull Request reports with suggested corrections.

---

## 👥 Team DocGuard

**Team Members:**
- Preet
- Anushka
- Khushi

**Hackathon:** Hacktoberfest 2026 Hack Day

**Selected Problem:** Problem 05 – Automated Documentation Drift Detection

---

## 📜 License

This project is intended to be released under the MIT License. See the `LICENSE` file for the applicable license terms.

---

**DocGuard AI — Because code changes, but documentation shouldn't fall behind.**
