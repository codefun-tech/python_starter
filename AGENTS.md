# AGENTS.md - Python Starter Project Guidelines

This file provides guidelines for agentic coding agents working in this repository.

## Project Overview

- **Package Manager**: uv
- **Python Version**: >=3.12
- **Source Directory**: src/python_starter/
- **Test Directory**: tests/

---

## Build / Lint / Test Commands

### Install Dependencies

```bash
uv sync --all-extras       # Install all dependencies including dev
```

### Running Tests

```bash
uv run pytest              # Run all tests
uv run pytest --cov=src --cov-report=term-missing  # Run with coverage

# Run a single test file
uv run pytest tests/test_main.py

# Run a single test (most specific pattern)
uv run pytest tests/test_main.py::TestBasicOperations::test_add_integers -v
uv run pytest tests/test_main.py::test_add_parametrized -v
```

### Code Formatting

```bash
uv run black .             # Format code
uv run black --check .     # Check formatting (no changes)
uv run isort .             # Sort imports
uv run isort --check-only .  # Check import order
```

### Linting

```bash
uv run flake8 .            # Run flake8 linter
```

### Type Checking

```bash
uv run mypy src/          # Run mypy type checker
```

### Full Quality Check (recommended before commits)

```bash
uv run black . && uv run isort . && uv run flake8 . && uv run mypy src/ && uv run pytest
```

---

## Development Environment

### Virtual Environment

```bash
uv venv                    # Create virtual environment in .venv
uv sync --all-extras       # Sync dependencies
source .venv/bin/activate  # Activate (optional, uv run handles this)
```

### Project Shell

```bash
uv run --with . -c "python -c '...'"  # Run command with project dependencies
```

### Dependency Management

```bash
uv add <package>          # Add a new dependency
uv add --dev <package>    # Add a dev dependency
uv remove <package>       # Remove a dependency
uv lock                   # Update lock file
```

---

## Code Style Guidelines

### Formatting

- **Line Length**: 120 characters maximum
- **Indentation**: 4 spaces for Python files
- **Tool**: black (automatically enforces consistent formatting)
- Run `uv run black .` before committing

### Import Sorting

- **Tool**: isort with black profile
- **Order**: FUTURE, STDLIB, THIRDPARTY, FIRSTPARTY, LOCALFOLDER
- **First-party package**: python_starter
- Use relative imports in /src directory (e.g., `from .main import Calculator`)

### Linting Rules (flake8)

- **Max Complexity**: 10 per function/method
- **Ignored Rules**: E501 (line length), W503 (binary operator position), E203 (whitespace before colon)
- These are configured to avoid conflicts with black

### Type Checking (mypy)

- **Python Version**: 3.12
- **Strict Settings**: warn_return_any = true
- Always provide type hints for:
  - Function/method parameters and return types
  - Class attributes
  - Module-level constants

### Naming Conventions

- **Classes**: PascalCase (e.g., `Calculator`, `MyClass`)
- **Functions/Methods**: snake_case (e.g., `add_numbers`, `get_result`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `MAX_RETRIES`)
- **Variables**: snake_case (e.g., `initial_value`)

### Docstrings

- Use Google-style docstrings
- Include: Description, Args, Returns, Raises, Examples
- Example:

```python
def divide(a: Number, b: Number) -> float:
    """Divide two numbers.

    Args:
        a: The dividend
        b: The divisor

    Returns:
        The quotient of the two numbers

    Raises:
        ValueError: If the divisor is 0
    """
```

### Error Handling

- Use explicit exception types (ValueError, TypeError, etc.)
- Provide descriptive error messages
- Example: `raise ValueError("Divisor cannot be 0")`
- Handle exceptions at the appropriate level

### Testing Patterns

- Test files: `test_*.py` in tests/ directory
- Test classes: `Test*` (e.g., `TestCalculator`, `TestBasicOperations`)
- Test methods: `test_*`
- Use pytest features:
  - `pytest.raises` for exception testing
  - `@pytest.mark.parametrize` for parameterized tests
  - `pytest.approx` for floating-point comparisons

### Code Organization

- Keep related functionality together
- Use modules (files) to organize code by feature
- Export public API in `__init__.py`
- Use `__all__` to explicitly define public exports

### Git Conventions

- Use meaningful commit messages
- Run full quality check before committing
- Don't commit: venv/, `__pycache__/`, .coverage, *.egg-info/

---

## File Structure

```terminal
src/python_starter/
  __init__.py      # Package exports
  main.py    # Main module
  cli.py           # CLI entry point (if applicable)

tests/
  test_main.py  # Test module
```

## Configuration Files

- pyproject.toml - Project metadata, tool configs
- .flake8 - Linting rules
- .editorconfig - Editor settings
- .gitignore - Git ignore patterns
