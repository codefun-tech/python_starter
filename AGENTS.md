# AGENTS.md - Agent Guidelines for This Repository

## Overview

This repository contains VS Code setup configuration for Python development. It includes:
- VS Code settings (`.vscode/settings.json`)
- EditorConfig (`.editorconfig`)
- Python requirements (`requirements.txt`)
- Documentation (README.md)

This is a configuration repository, not a Python source code project.

## Build, Lint, and Test Commands

### Python Environment Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment (Linux/macOS)
source venv/bin/activate

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Tests

This project uses pytest for testing. Run tests with:

```bash
# Run all tests
pytest

# Run a single test file
pytest tests/test_example.py

# Run a single test function
pytest tests/test_example.py::test_function_name

# Run tests matching a pattern
pytest -k "test_pattern"

# Run tests with verbose output
pytest -v

# Run tests with coverage
pytest --cov=. --cov-report=term-missing
```

### Linting and Type Checking

The repository is configured to use these tools (see `.vscode/settings.json`):

```bash
# Run flake8 (with ignores for E501, E203, W503)
flake8 .

# Run black formatter (check only)
black --check .

# Run black formatter (auto-fix)
black .

# Run isort (check only)
isort --check .

# Run isort (auto-fix)
isort .

# Run mypy type checker
mypy .

# Run bandit security linter
bandit -r .
```

### Running All Checks

```bash
# Run all linters and formatters
flake8 . && black --check . && isort --check . && mypy . && bandit -r .
```

## Code Style Guidelines

### General Editor Settings (from `.vscode/settings.json`)

- **Indentation**: 2 spaces for most files, 4 spaces for Python
- **Encoding**: UTF-8
- **Line endings**: LF (Unix-style)
- **Trailing whitespace**: Trimmed
- **Final newline**: Inserted

### Python-Specific Settings

#### Formatting
- **Formatter**: Black (`ms-python.black-formatter`)
- **Import sorting**: isort with Black profile
- **Line length**: Default (88 characters, Black default)

#### Type Checking
- **Type checker**: mypy
- **Type checking mode**: Basic
- **Inlay hints**: Function return types enabled, variable types disabled, pytest parameters enabled

#### Linting
- **Linter**: flake8
- **Ignored rules**: E501 (line too long), W503 (line break before binary operator), E203 (whitespace before colon)

#### Testing
- **Test framework**: pytest
- **Test directory**: `tests/`
- **Unittest**: Disabled (pytest preferred)

### Editor Configuration (from `.editorconfig`)

```ini
[*]
charset = utf-8
indent_style = space
indent_size = 2
trim_trailing_whitespace = true
end_of_line = lf
insert_final_newline = true

[*.py]
indent_size = 4
```

### Naming Conventions

- **Variables/functions**: `snake_case` (e.g., `my_variable`, `calculate_total`)
- **Classes**: `PascalCase` (e.g., `MyClass`, `DataProcessor`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_BUFFER_SIZE`)
- **Private methods/variables**: `_leading_underscore`

### Imports

- Use isort with Black profile for automatic sorting
- Group imports: standard library, third-party, local
- Add type hints where beneficial
- Use explicit relative imports for local modules

### Error Handling

- Use specific exception types rather than bare `except:`
- Include context in error messages
- Use logging instead of print statements for debugging
- Handle errors at the appropriate level

### Code Actions on Save

The following actions run automatically on save:
- `source.organizeImports` - Sort and organize imports
- `source.fixAll` - Fix auto-fixable issues

### VS Code Extensions

Recommended extensions for this project (auto-installed via settings):
- Python (Pylance, Python Debugger)
- Flake8
- Black Formatter
- Mypy Type Checker
- isort
- Jupyter (for notebooks)
- GitHub Copilot

### Working With This Repository

1. **Do not commit Python source files** - This is a configuration-only repository
2. **Keep requirements.txt updated** - Add any new Python dependencies
3. **Maintain .editorconfig** - Update for any new file types
4. **Update .vscode/settings.json** - Add new VS Code settings as needed
5. **Document in README.md** - Keep setup instructions current

### File Patterns

- `.vscode/settings.json` - VS Code workspace settings
- `.editorconfig` - Cross-editor configuration
- `requirements.txt` - Python dependencies
- `README.md` - Documentation

## Notes for Agents

- This repository serves as a template/setup for Python development
- No source code exists here - only configuration
- When making changes, maintain consistency with existing settings
- Test any new settings in a local VS Code instance before committing
