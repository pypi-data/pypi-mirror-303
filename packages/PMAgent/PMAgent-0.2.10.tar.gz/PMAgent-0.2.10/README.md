# PMAgent

PMAgent is a Python package that helps developers, data scientists, and DevOps professionals to refactor and modify code using OpenAI/Groq. It reads code from files, interacts with an LLM to generate modifications, and saves changes back to the files. It can create new projects in any programming language with just a prompt.

## Installation

```bash
pip install PMAgent
```

## Environment Setup

```bash
# API Keys (at least one is required)
export OPENAI_API_KEY="sk-..."
export GROQ_API_KEY="gsk_..."

# Optional Configuration
export MODEL=""        # Specific model to use
export TEMPERATURE=""  # Temperature for response generation
export TOP_P=""       # Top-p sampling parameter
export MAX_TOKENS=""  # Maximum tokens in response
```

## Basic Usage

```bash
pmagent <UserPrompt> <directorytoexecute>
```

### Parameters:
- `UserPrompt`: Your instruction or request in quotes
- `directorytoexecute`: Path to the target directory (optional)
- `--llm-type` or `-l`: Choose LLM provider (`openai` or `groq`) (optional)

## Examples

### 1. Web Development Projects

```bash
# Create a new React e-commerce project
pmagent "Create a React e-commerce website with product listing, cart functionality, and checkout process" ecommerce-app

# Build a portfolio website
pmagent "Create a modern portfolio website with dark/light mode, project showcase, and contact form" portfolio-site

# Create a dashboard
pmagent "Build a responsive admin dashboard with charts, tables, and user management" admin-dashboard
```

### 2. Data Science & Analysis

```bash
# Create data analysis notebook
pmagent "Create a comprehensive EDA notebook for customer churn analysis including visualizations" churn-analysis

# Build ML pipeline
pmagent "Create a machine learning pipeline for house price prediction with data preprocessing and model evaluation" ml-pipeline

# Time series analysis
pmagent "Set up a time series analysis project for stock price prediction with LSTM" stock-analysis
```

### 3. Backend Development

```bash
# Create API server
pmagent "Create a FastAPI backend with user authentication, database models, and CRUD operations" backend-api

# Setup microservices
pmagent "Set up a microservices architecture with user service and product service using Docker" microservices

# Create CLI tool
pmagent "Create a Python CLI tool for automated file organization with logging" file-organizer
```

### 4. DevOps & Infrastructure

```bash
# Setup CI/CD pipeline
pmagent "Create GitHub Actions workflow for testing and deploying a Python package" cicd-setup

# Infrastructure as Code
pmagent "Create Terraform configuration for AWS ECS cluster with auto-scaling" terraform-aws

# Docker setup
pmagent "Create Docker configuration for a MERN stack application" docker-config
```

### 5. Code Refactoring

```bash
# Refactor existing code
pmagent "Refactor the Python code in utils/ to follow SOLID principles" utils

# Add tests
pmagent "Add unit tests for all functions in the services/ directory" services

# Optimize performance
pmagent "Optimize the database queries in the repositories/ folder" repositories
```

## Python API Usage

```python
import os
from pmagent import LLMInteractionManager

def main():
    # Initialize with configuration
    llm_interaction_manager = LLMInteractionManager(
        openai_api_key=os.getenv("OPENAI_API_KEY"), 
        groq_api_key=os.getenv("GROQ_API_KEY"),
        config={   # OPTIONAL 
            "model": "llama-3.1-70b-versatile",
            "temperature": 0.5,
            "top_p": 0.9,
            "max_tokens": 4000,
        },
        llm_type='groq',  # OPTIONAL 
    )

    # Example: Create a new project
    llm_interaction_manager.interact_with_llm(
        user_message="Create a FastAPI backend with SQLAlchemy ORM and JWT authentication",
        path="backend-project"
    )

    # Example: Refactor existing code
    llm_interaction_manager.interact_with_llm(
        user_message="Refactor this code to use dependency injection and add proper error handling",
        path="src/services"
    )

if __name__ == "__main__":
    main()
```

## Best Practices

1. **Clear Instructions**: Be specific in your prompts about what you want to create or modify
2. **Directory Structure**: Create the target directory before running the command if needed
3. **Version Control**: Always commit your changes before using PMAgent for code modifications
4. **API Keys**: Use environment variables for API keys instead of hardcoding them
5. **Model Selection**: Choose the appropriate model based on your task complexity

## Support

For issues, feature requests, or contributions, please visit our GitHub repository.

