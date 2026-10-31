# Hackathon Submission

## Team Details

- **Team Name:** DocGuard
- **Team Members:** Preet, Anushka, Khushi
- **Selected Problem:** Problem 05 – Automated Documentation Drift Detection

## Project Name

**DocGuard AI**

## Problem Understanding

Documentation can become outdated when developers modify source code without updating the related documentation.

DocGuard AI aims to detect documentation drift by analyzing code changes and identifying documentation statements that may no longer match the actual code behavior.

## Proposed Solution

We plan to build a tool that:

1. Analyzes code changes introduced through GitHub Pull Requests.
2. Identifies documentation related to the changed code.
3. Detects potentially outdated API references, function parameters, default values, configuration descriptions, and behavior.
4. Highlights the exact documentation statements that may be incorrect.
5. Links each detected issue to the relevant code change.
6. Uses AI to explain detected inconsistencies and suggest documentation corrections.

## AI Model Selection

- **Planned Model:** Qwen2.5-Coder:7B (Ollama model tag: qwen2.5-coder:7b; license verification pending).
- **Runtime:** Ollama.
- **Purpose:** The model will help explain evidence-backed documentation inconsistencies and suggest corrected documentation.

We will use deterministic code analysis to identify potential mismatches and use the AI model to generate explanations and suggestions. This approach aims to reduce unsupported AI-generated warnings.

## Technology Stack

- Python
- Python AST
- Git
- GitHub Pull Requests
- Ollama
- Qwen2.5-Coder:7B

## Expected Outcome

A working documentation drift detection tool that provides evidence-backed warnings, exact references to affected documentation, links to relevant code changes, and suggested corrections.