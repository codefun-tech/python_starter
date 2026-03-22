# Visual Studio Code Setup

This a AI-powered bootstrap repository for python development in Visual Studio Code.

You can utilize this repository to configure your VS Code worksapce with Copilot enabled to start a new Python project.

## Version Control

Use Git for version control and GitHub for remote hosting.

### Generate SSH Keys

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

### Add SSH Key to GitHub

1. Copy the SSH key to clipboard:

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy  # macOS
cat ~/.ssh/id_ed25519.pub | xclip -sel clip  # Linux
```

2. Go to GitHub > Settings > SSH and GPG keys > New SSH key, and paste the key.

### Test SSH Connection

```bash
ssh -T git@github.com
```

## The Python Package Manager

Using `uv` as the package manager for modern Python development.

### Install `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Initialize the Project

```bash
uv init
```

The above command will create a _pyproject.toml_ configuration file in the current directory.

### Install Python

```bash
uv python install <python_version>
```

### Create Virtual Environment

```bash
uv venv --python <python_version>
```

### Pin Python Version

```bash
uv python pin <python_version>
```

The above command will pin the Python version in the _.python-version_ file.

### Deploy Development Environment

```bash
uv sync --all-extras
```

### Deploy Production Environment

```bash
uv sync --frozen --no-dev
```

### Update Dependencies

```bash
uv lock --upgrade
```

### Build and Publish Package

If you want to build and publish your package to PyPI, you can use the following commands:

```bash
uv build
uv publish
```

## Formatting

Use `black` for code formatting and `isort` for import sorting.

### Install `black`

```bash
uv add --dev black
```

### Configure `black` in _pyproject.toml_

```toml
[tool.black]
line-length = 120
target-version = ["py312"]
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.venv
  | __pycache__
  | build
  | dist
)/
'''
```

### Install `isort`

```bash
uv add --dev isort
```

### Configure `isort` in _pyproject.toml_

```toml
[tool.isort]
# Compatibility with Black
profile = "black"

# Configure to match Black's line length setting
line_length = 120

known_first_party = ["python_demo"]
src_paths = ["src", "tests"]
skip = [".git", ".venv", "__pycache__", "build", "dist"]
sections = ["FUTURE", "STDLIB", "THIRDPARTY", "FIRSTPARTY", "LOCALFOLDER"]
```

### Run formatters

```bash
# Format code
uv run black .

# Check code format (without modifying)
uv run black --check .

# Sort imports
uv run isort .

# Check import sorting (without modifying)
uv run isort --check-only .
```

## Linting

Use `flake8` for linting.

### Install `flake8`

```bash
uv add --dev flake8
```

### Configure `flake8` in _.flake8_

```ini
[flake8]
# Keep consistency with Black
max-line-length = 120

exclude =
    .git,
    .venv,
    __pycache__,
    build,
    dist

# Rules to ignore (mostly to avoid conflicts with Black)
ignore =
    # E501: Let Black handle line length
    E501,
    # W503: Line break before binary operator (conflicts with Black)
    W503,
    # E203: Whitespace before ':' (conflicts with Black)
    E203

# Maximum complexity per file
max-complexity = 10

# Enabled extensions
extend-select = B,B9
```

### Run linter

```bash
uv run flake8 .
```

## Type Checking

Use `mypy` for type checking.

### Install `mypy`

```bash
uv add --dev mypy
```

### Configure `mypy` in _pyproject.toml_

```toml
[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
ignore_missing_imports = true
```

### Run type checker

```bash
uv run mypy src/
```

## Testing

Use `pytest` for testing and `pytest-cov` for test coverage.

### Install `pytest` and `pytest-cov`

```bash
uv add --dev pytest pytest-cov
```

### Configure `pytest` and `pytest-cov` in _pyproject.toml_

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
addopts = [
    "-v",
    "--tb=short",
]

[tool.coverage.run]
source = ["src"]
branch = true

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "if __name__ == .__main__.:",
]
```

### Run tests

```bash
uv run pytest
uv run pytest --cov=src --cov-report=term-missing
```

## Run Package Scripts

You can define your package scripts in the _pyproject.toml_ file under the `[project.scripts]` section. For example:

```toml
[project.scripts]
starter = "python_starter.cli:main"
```

Install the package in editable mode to make the script available:

```bash
uv pip install -e .
```

Then you can run the script using:

```bash
uv run starter
```

## Other Useful Packages

```bash
uv add --dev ipykernel rope bandit
```

## VS Code Extensions

### Python

- Python
- Black Formatter
- isort
- Flake8
- Mypy Type Checker
- Jupyter
- Github Copilot Chat
- Even Better TOML

### General Editing Extensions

- Vim
- EditorConfig for VS Code
- YAML
- Markdownlint

### Data Analysis

- Excel Viewer
- SandDance for VSCode
- Data Wrangler

### Others

- Thunder Client
- CodeSnap
- Power Mode
- vscode-pets

## Themes

You can learn to install themes from the tutorial [Visual Studio Code Themes](https://codefun.tech/visual-studio-code-themes/).

- [Horizon Theme](https://marketplace.visualstudio.com/items?itemName=jolaleye.horizon-theme-vscode)
- [Dracula Official](https://marketplace.visualstudio.com/items?itemName=dracula-theme.theme-dracula)
- [C/C++ Themes](https://github.com/Microsoft/vscode-cpptools)
- [Earthbound Themes](https://github.com/benbusby/earthbound-themes)
- [GitHub Theme](https://github.com/primer/github-vscode-theme)
- [Github Light Theme](https://github.com/chuling/vscode-theme-github-light)
- [Linux Themes for Visual Studio Code](https://github.com/rdnlsmith/vscode-linux-themes)
- [Panda Theme](https://github.com/tinkertrain/panda-syntax-vscode)
- [Remedy](https://github.com/robertrossmann/vscode-remedy)
- [Winter is Coming](https://github.com/johnpapa/vscode-winteriscoming)
- [Bearded Theme](https://github.com/BeardedBear/bearded-theme)

## Fonts

Please follow the tutorials [Choosing The Best Programming Fonts](https://codefun.tech/choosing-the-best-programming-fonts/) and [Free Best Programming Fonts for All Time](https://codefun.tech/free-best-programming-fonts-for-all-time/) to choose your favorite fonts.

- [Fira Code](https://github.com/tonsky/FiraCode)
- [Consolas](https://learn.microsoft.com/en-us/typography/font-list/consolas)
- [Inconsolata](https://github.com/googlefonts/Inconsolata)
- [Cascadia Code](https://github.com/microsoft/cascadia-code)
- [Courier New](https://learn.microsoft.com/en-us/typography/font-list/courier-new)
- [Courier Prime](https://quoteunquoteapps.com/courierprime/)
- [Monaco](https://en.wikipedia.org/wiki/Monaco_(typeface))
- [Menlo](https://en.wikipedia.org/wiki/Menlo_(typeface))
- [Ubuntu Mono](https://design.ubuntu.com/font/)
- [Anonymous Pro](https://www.marksimonson.com/fonts/view/anonymous-pro)
- [JetBrains Mono](https://www.jetbrains.com/lp/mono/)
- [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono)

## AI

### OpenCode

In OpenCode, using `/init` command to generate AGENTS.md file for your project.

### GitHub Copilot

In VS Code, you can use `/init` command to generate a _copilot-instructions_ file in _.github_ directory.

## References

- [Visual Studio Code Setup for Python Beginners](https://codefun.tech/visual-studio-code-setup-for-python-beginners/)
