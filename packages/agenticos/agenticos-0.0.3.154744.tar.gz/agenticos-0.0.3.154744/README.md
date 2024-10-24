# AgenticOS

AgenticOS is a flexible and modular framework designed to help developers deploy and manage AI-driven workflows using agent-based systems. The framework is designed to be LLM-agnostic and core-tech switchable in the future, allowing developers to integrate their preferred agent systems seamlessly.

The goal is to provide a framework that integrates easily into your existing or planned infrastructure, giving you the flexibility to focus on AI task execution without complex setups.

# Geting started

## Installing the prerequisites

### pipx
This is currently a recomended way to install comamnds that are available accros your systems like build backends or other code generators. Please follow instructions for your operating system: https://pipx.pypa.io/stable/installation/

### poetry
This build backend is required by crew AI. You can install it with pipx:
```sh
pipx install poetry
```
For other installation options please check the official instructions: https://python-poetry.org/docs/#ci-recommendations

### CrewAI
Please install CrewAI using the pipx:
```sh
pipx install crewai
```

> :warning:  Please make sure that you update CrewAI before every use.

## Creating a new project
1. Create a new CrewAI crew. If you are installing agenticos alongside exising CrewAI project please go to point 3.
```sh
crewai create crew new_crew
```
2. Generate venv and install dependencies:
```sh
cd new_crew
poetry shell
poetry install
```
3. Install agenticos package using poetry:
```sh
poetry add agenticos
```
4. Generate agenctic scaffold files:
```sh
agentic init
```

It will generate following files in your project:
```
[app_root]
|-src
  |-agentic
    |-agentic_node.py
    |-agentic_config.py
```
> :warning: This configuration should work with out-of the box crewai project. If you made any changes to project structure you will have to update `agentic_config.py` file.

## Running
Currentic agentic node may be run only as a standalone HTTP server. Production fastapi mode:
```bash
agentic run
```
or dev fastapi mode:
```bash
agentic run --dev
```

## Config via ENV VARS
Order of priority CLI ARGS > ENV_VARS > DEFAULTS. Current env vars with defaults:
```python
    AUTH_TOKEN: str = ""
    REGISTRY_URL: str = "ws://localhost:8080"
    NODE_MODE: str = "httpserver"
    HTTP_PORT: int = 8000
    AGENTIC_CONFIG_PATH: str = "src/agentic/agentic_config.py"
    HTTP_HEALTHCHECK : bool = False
```