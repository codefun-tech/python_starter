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

### Initialize the project

```bash
uv init
```

The above command will create a _pyproject.toml_ configuration file in the current directory.

### Install Python

```bash
uv install python <python_version>
```

### Create virtual environment

```bash
uv venv --python <python_version>
```

### Pin Python version

```bash
uv python pin <python_version>
```

The above command will pin the Python version in the _.python-version_ file.

## Formatting

Use `black` for code formatting and `isort` for import sorting.

### Install `black`

```bash
uv add --dev black
```

### Configure `black` in _pyproject.toml_

```toml
[tool.black]
# 行长度限制
line-length = 120

# 目标Python版本
target-version = ["py313"]

# 包含的目录
include = '\.pyi?$'

# 排除的目录
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
# 使用Black兼容模式
profile = "black"

# 行长度（与Black保持一致）
line_length = 120

# 已知的第一方模块
known_first_party = ["python_demo"]

# 源码目录
src_paths = ["src", "tests"]

# 跳过的目录
skip = [".git", ".venv", "__pycache__", "build", "dist"]

# 导入分组顺序
sections = ["FUTURE", "STDLIB", "THIRDPARTY", "FIRSTPARTY", "LOCALFOLDER"]
```

### Run formatters

```bash
# 代码格式化
uv run black .

# 检查格式（不修改）
uv run black --check .

# 导入排序
uv run isort .

# 检查导入排序（不修改）
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
# 行长度（与Black保持一致）
max-line-length = 120

# 排除的目录
exclude =
    .git,
    .venv,
    __pycache__,
    build,
    dist

# 忽略的规则
ignore =
    # E501: 行太长（由Black处理）
    E501,
    # W503: 二元运算符前换行（与Black风格冲突）
    W503,
    # E203: 冒号前空格（与Black风格冲突）
    E203

# 每个文件的最大复杂度
max-complexity = 10

# 启用的扩展
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
- Markdown All in One
- YAML

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


## References

- [Visual Studio Code Setup for Python Beginners](https://codefun.tech/visual-studio-code-setup-for-python-beginners/)
