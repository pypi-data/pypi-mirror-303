# PMAgent

PMAgent is a Python package that helps developers refactor and modify code using OpenAI. It reads code from files, interacts with an LLM to generate modifications, and saves changes back to the files.

## Installation

To install PMAgent:

```bash
pip install PMAgent

export OPENAI_API_KEY="sk-"

pmagent "Fix the code from playground folder" playground

# pmagent <UserPrompt> <directorytoexecute>

```
### Put API KEY ON ENV: OPENAI_API_KEY

