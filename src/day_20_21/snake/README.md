# Snake

A Snake game built with Python's `turtle` module.

## Project setup

This project uses [uv](https://docs.astral.sh/uv/) for environment and package management.

### 1. Create the project

```bash
uv init snake
cd snake
```

### 2. Set the Python version

The project requires Python 3.13 or later. uv will automatically find or download
a matching interpreter. You can pin the version explicitly:

```bash
uv python pin 3.13
```

### 3. Install dependencies

This project has no third-party dependencies. To install the project itself in
editable mode (so `uv run` can resolve the entry point):

```bash
uv sync
```

### 4. Run the game

```bash
uv run snake
```

This invokes the `main` function in [main.py](main.py) via the script entry point
defined in `pyproject.toml`:

```toml
[project.scripts]
snake = "main:main"
```

### 5. Build a distribution

```bash
uv build
```

Produces a source distribution and wheel in the `dist/` directory.
