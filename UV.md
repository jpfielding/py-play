# Using `uv` in this Project

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency management and package resolution.

## 1. Setup

To install the dependencies defined in `pyproject.toml`, run:

```bash
uv sync --all-extras
```

This will create a virtual environment in `.venv` with all optional dependencies installed.

## 2. Managing Dependencies

### Adding a Shared Dependency
To add a dependency available to all parts of the project:

```bash
uv add <package_name>
```

### Adding a Group-Specific Dependency
To add a dependency to a specific group (e.g., `adk-google-search`):

```bash
uv add --optional adk-google-search <package_name>
```

### Dependency Groups
The project is organized into optional dependency groups in `pyproject.toml`:

- **`adk-google-search`**: Dependencies for the Google Search Agent (`google-adk`, `google-genai`).
- **`flask-demo`**: Dependencies for the Flask application (`flask`).
- **`all`**: A convenience group containing all dependencies.

## 3. Running Code

You can run scripts using `uv run`, which ensures the correct environment and dependencies are used.

### Running the Google Search Agent
```bash
# Ensure you have the extra dependencies installed or available
uv run --extra adk-google-search python adk-google-search/agent.py
```

### Running the Flask Demo
```bash
uv run --extra flask-demo python flask-demo/src/main.py
```

## 4. Virtual Environment

`uv` automatically manages the virtual environment in `.venv`.
To activate it manually in your shell:

```bash
source .venv/bin/activate
```
