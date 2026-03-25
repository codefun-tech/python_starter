---
name: check-repository
description: Checks repository structure, git status, configuration files, and code quality. Use when you need to quickly assess the state of a Python project including: (1) Git status and uncommitted changes, (2) Directory structure (src/, tests/, config files), (3) Project configuration (pyproject.toml, Python version, dependencies), (4) Code quality (flake8, mypy, pytest results)
---

# Repo Structure Check

## Overview

This skill runs a comprehensive check of a Python repository's structure and settings, providing a quick overview of the project's state including git status, configuration, and code quality.

## Running the Check

Execute the script to check the repository:

```bash
python skills/repo-structure-check/scripts/check_repo.py
```

## What Gets Checked

### Git Status
- Current branch
- Whether there are uncommitted changes
- Number of modified and untracked files

### Directory Structure
- Presence of `src/` and `tests/` directories
- Config files: pyproject.toml, .flake8, .editorconfig, .gitignore, AGENTS.md

### pyproject.toml
- Valid TOML format
- Project name
- Python version requirement
- Total dependency count

### Code Quality
- Flake8 linting errors
- MyPy type checking errors
- Pytest test results (passed/failed)

## Script Location

The script is at: `skills/repo-structure-check/scripts/check_repo.py`

The script runs from the current working directory, so run it from the repository root.
