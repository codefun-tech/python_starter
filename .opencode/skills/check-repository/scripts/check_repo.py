#!/usr/bin/env python3
"""Script to check repository structure and settings."""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], cwd: Path | None = None) -> tuple[int, str, str]:
    """Run a command and return exit code, stdout, stderr."""
    try:
        result = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, timeout=30
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return 1, "", "Command timed out"
    except Exception as e:
        return 1, "", str(e)


def check_git_status(repo_path: Path) -> dict:
    """Check git status and info."""
    status = {"branch": "", "has_changes": False, "untracked": 0, "modified": 0}
    
    code, stdout, _ = run_command(["git", "branch", "--show-current"], cwd=repo_path)
    if code == 0:
        status["branch"] = stdout.strip()
    
    code, stdout, _ = run_command(["git", "status", "--porcelain"], cwd=repo_path)
    if code == 0:
        lines = [l for l in stdout.strip().split("\n") if l]
        status["has_changes"] = len(lines) > 0
        status["modified"] = sum(1 for l in lines if l.startswith(" M") or l.startswith("M "))
        status["untracked"] = sum(1 for l in lines if l.startswith("??"))
    
    return status


def check_directory_structure(repo_path: Path) -> dict:
    """Check directory structure."""
    structure = {
        "src_exists": False,
        "tests_exists": False,
        "config_files": [],
    }
    
    structure["src_exists"] = (repo_path / "src").exists()
    structure["tests_exists"] = (repo_path / "tests").exists()
    
    config_files = ["pyproject.toml", ".flake8", ".editorconfig", ".gitignore", "AGENTS.md"]
    for f in config_files:
        if (repo_path / f).exists():
            structure["config_files"].append(f)
    
    return structure


def check_pyproject(repo_path: Path) -> dict:
    """Check pyproject.toml contents."""
    pyproject = {"valid": False, "name": "", "python_version": "", "deps_count": 0}
    
    pyproject_path = repo_path / "pyproject.toml"
    if not pyproject_path.exists():
        return pyproject
    
    try:
        content = pyproject_path.read_text()
        pyproject["valid"] = True
        
        import tomllib
        data = tomllib.loads(content)
        
        if "project" in data:
            pyproject["name"] = data["project"].get("name", "")
            pyproject["python_version"] = data["project"].get("requires-python", "")
            deps = data["project"].get("dependencies", [])
            if "optional-dependencies" in data["project"]:
                for extra in data["project"]["optional-dependencies"].values():
                    deps.extend(extra)
            pyproject["deps_count"] = len(deps)
    except Exception as e:
        pyproject["error"] = str(e)
    
    return pyproject


def check_code_quality(repo_path: Path) -> dict:
    """Check code quality (lint, type check, tests)."""
    quality = {"flake8_errors": 0, "mypy_errors": 0, "pytest_passed": None}
    
    code, stdout, _ = run_command(["uv", "run", "flake8", "."], cwd=repo_path)
    if code == 0:
        quality["flake8_errors"] = 0
    else:
        quality["flake8_errors"] = len(stdout.strip().split("\n")) if stdout.strip() else 1
    
    code, stdout, _ = run_command(["uv", "run", "mypy", "src/"], cwd=repo_path)
    if code == 0:
        quality["mypy_errors"] = 0
    else:
        quality["mypy_errors"] = len(stdout.strip().split("\n")) if stdout.strip() else 1
    
    code, stdout, stderr = run_command(["uv", "run", "pytest", "-v"], cwd=repo_path)
    if code == 0:
        quality["pytest_passed"] = True
    else:
        quality["pytest_passed"] = False
        quality["pytest_error"] = stderr[:500] if stderr else stdout[:500]
    
    return quality


def main():
    repo_path = Path.cwd()
    print(f"Checking repository: {repo_path}\n")
    
    print("=" * 50)
    print("GIT STATUS")
    print("=" * 50)
    git_status = check_git_status(repo_path)
    print(f"Branch: {git_status['branch']}")
    print(f"Has changes: {git_status['has_changes']}")
    if git_status["has_changes"]:
        print(f"  Modified: {git_status['modified']}")
        print(f"  Untracked: {git_status['untracked']}")
    
    print("\n" + "=" * 50)
    print("DIRECTORY STRUCTURE")
    print("=" * 50)
    structure = check_directory_structure(repo_path)
    print(f"src/ exists: {structure['src_exists']}")
    print(f"tests/ exists: {structure['tests_exists']}")
    print(f"Config files: {', '.join(structure['config_files']) if structure['config_files'] else 'None'}")
    
    print("\n" + "=" * 50)
    print("PYPROJECT.TOML")
    print("=" * 50)
    pyproject = check_pyproject(repo_path)
    print(f"Valid: {pyproject['valid']}")
    if pyproject["valid"]:
        print(f"Name: {pyproject['name']}")
        print(f"Python version: {pyproject['python_version']}")
        print(f"Dependencies: {pyproject['deps_count']}")
    
    print("\n" + "=" * 50)
    print("CODE QUALITY")
    print("=" * 50)
    quality = check_code_quality(repo_path)
    print(f"Flake8 errors: {quality['flake8_errors']}")
    print(f"Mypy errors: {quality['mypy_errors']}")
    print(f"Tests passed: {quality['pytest_passed']}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())