# AI-Powered Knowledge Base CLI

A production-grade, modular CLI tool designed for interacting with local LLMs via Ollama. This project demonstrates advanced software engineering principles, moving beyond basic script writing toward maintainable, infrastructure-aware application design.

## Key Engineering Capabilities

- **Service Encapsulation:** Implements a clean client-wrapper (`OllamaClient`) to decouple business logic from the underlying API communication.
- **Infrastructure as Code (IaC):** Utilizes `.devcontainer` configuration to ensure environment reproducibility and automated setup (postCreateCommand).
- **Resilient API Interaction:** Implements advanced timeout handling and connection retry logic to manage resource-intensive local inference.
- **Fault-Tolerant Design:** Includes health-check mechanisms and robust exception handling to manage local LLM state transitions.
- **CI/CD Integration:** Automated code quality checks (Flake8) via GitHub Actions to maintain enterprise-grade coding standards.

## Project Structure

```text
ai-knowledge-base-cli/
├── .devcontainer/         # Infrastructure as Code (environment orchestration)
├── .github/workflows/     # Automated linting and CI pipelines
├── docs/                  # Project documentation and test samples
├── src/                   # Core application logic
│   ├── cli.py             # CLI entry point (argparse)
│   └── engine.py          # Service encapsulation layer
├── requirements.txt       # Hardened dependency definitions
└── README.md              # Project documentation
```

## Execution Guide

### 1. Development (GitHub Codespaces)
The environment is fully automated. Simply create a codespace, and the system will provision Ollama and dependencies automatically.

### 2. Local Execution
For running locally, ensure you have Ollama installed and running:

    # Install dependencies
    pip install -r requirements.txt

    # Run the CLI tool
    python3 src/cli.py "Your prompt here"

## Troubleshooting
- **Model Loading:** If the system is slow, ensure sufficient RAM is allocated. Consider switching to smaller models (e.g., phi3) if the host environment is resource-constrained.
- **Connection Refused:** Verify that ollama serve is active in the background.
- **ReadTimeout:** In environments with limited CPU/RAM, the initial inference request may take longer. Adjust the timeout parameter in engine.py accordingly.

## Best Practices Implemented
- **Type Hinting:** Extensive use of Python type hints for better IDE support and maintainability.
- **Configuration Management:** Uses environment variables to handle API endpoints and model settings.
- **Modular Design:** Clear separation of CLI interface and core logic, allowing for easy integration into larger systems.

## Contribution Guidelines
1. Fork the repository.
2. Create a feature branch (git checkout -b feat/new-inference-strategy).
3. Run flake8 to ensure code compliance before submitting a Pull Request.