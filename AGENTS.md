# AGENTS.md

This file contains development guidelines for agentic coding agents working in this FastAPI repository.

## Development Environment Setup

Use `uv` as the package manager. The project uses Python 3.10+.

```bash
# Install dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install
```

## Build/Lint/Test Commands

### Testing

```bash
# Run all tests with coverage (require 100% coverage)
uv run coverage run -m pytest && uv run coverage report

# Run specific test file
uv run pytest tests/test_main.py

# Run specific test function
uv run pytest tests/test_main.py::test_read_root

# Run tests with verbose output
uv run pytest -v

# Run tests with coverage HTML report
uv run coverage html
```

### Linting & Formatting

```bash
# Format code
uv run black .

# Check formatting without changing files
uv run black --check .

# Check imports without changing files
uv run isort --check-only .

# Sort imports
uv run isort .

# Lint code
uv run ruff check

# Auto-fix linting issues
uv run ruff check --fix

# Type checking with pyright
uv run pyright

# Run all pre-commit hooks (quality checks)
uv run pre-commit run --all-files
```

### Development Server

```bash
# Run in development mode (with auto-reload)
uv run fastapi dev

# Run in production mode
uv run fastapi run
```

## Code Style Guidelines

### Import Organization

- Use `collections.abc` for collection abstract base classes
- Standard library imports first, then third-party, then local imports
- Use `isort` to maintain consistent import ordering
- Use absolute imports for local modules (e.g., `from app.main import app`)
- Use `# isort: skip` to skip sorting for specific import lines (e.g., when models need to be imported for side effects)
- Use `# isort: skip_file` at the top of a file to skip the entire file

### Type Annotations

- All functions must have explicit type annotations
- Use modern union syntax: `str | None` instead of `Optional[str]`
- Use generic dict syntax: `dict[str, str]` instead of `Dict[str, str]`
- Enable strict MyPy mode - all code must pass strict type checking

### Naming Conventions

- `snake_case` for variables, functions, and files
- `PascalCase` for classes and Pydantic models
- `UPPER_SNAKE_CASE` for constants
- Router instances: `router`
- FastAPI app instance: `app`
- Test client fixture: `client`

### Code Structure

- Use APIRouter for modular endpoint organization
- Include routers in main.py with descriptive prefixes
- Keep Pydantic models simple and focused
- Return types should be explicit in route handlers

### Error Handling

- Raise FastAPI HTTPException for HTTP errors
- Use `B904` ruff exception (allow raising without from e for HTTPException)
- No print statements in production code (T201 ruff rule)

### Code Quality Rules

- Maximum line length: 88 characters (Black default)
- No unused function arguments (ARG001 ruff rule)
- Use pyupgrade-compatible code (UP ruff rules)
- Prefer comprehensions over loops where appropriate (C4 ruff rule)
- Avoid bug-prone patterns (B ruff rules)

### Testing Guidelines

- Use pytest for all testing
- Test client should be a module-scoped fixture
- Each test function should be focused on one behavior
- Use descriptive test names starting with `test_`
- Assert on both status codes and response content
- Include type annotations for test functions: `def test_function() -> None:`
**100% test coverage is enforced** - `fail_under = 100` in pyproject.toml
- Use `# pragma: no cover` for lines that are impossible/impractical to test
- Add type hints for test fixtures to avoid pyright errors
- Use `# isort: skip` for imports that need specific ordering

### Documentation

- All API endpoints should have proper FastAPI documentation via docstrings
- Use clear, descriptive variable names
- Keep functions focused and small
- Return types should be self-documenting

### Performance Guidelines

- Use fast=True for Black formatting
- Use uv for fast dependency management
- Enable coverage dynamic context for better test insights

## Project Structure

```
app/
├── __init__.py
├── main.py          # FastAPI app initialization and router includes
├── healthcheck.py   # Health check endpoints
└── items.py         # Item-related endpoints

tests/
├── __init__.py
├── conftest.py      # Pytest fixtures
├── test_main.py     # Main app tests
├── test_healthcheck.py  # Health check tests
└── test_items.py    # Item endpoints tests
```

## Key Configuration Files

- `pyproject.toml`: Main project configuration, tool settings ((Black, isort, Ruff, Pyright, Coverage, MyPy)
- `.pre-commit-config.yaml`: Pre-commit hooks configuration
- `uv.lock`: Dependency lock file (do not edit manually)

## Tool Configuration

### Black
- Line length: 88 characters (default)
- Fast mode enabled

### isort
- Profile: black (compatible with Black formatting)
- Line length: 88 characters

### Ruff
- Target: Python 3.10+
- Selected rules: pycodestyle, pyflakes, isort, flake8-bugbear, comprehensions, pyupgrade
- Enforces: no unused arguments, no print statements, proper exception handling

### Pyright
- Strict type checking for `app/` directory
- Reports unused imports, incorrect types, and type mismatches

### Coverage
- Enforces 100% code coverage (`fail_under = 100`)
- Tracks per-test coverage with dynamic context

## Code Quality Standards

The project enforces strict code quality standards:

- **Black** - Code formatting with 88 character line length
- **isort** - Import sorting and organization
- **Ruff** - Fast Python linting with auto-fix support
- **Pyright** - Strict type checking for `app/` directory
- **Coverage** - 100% test coverage enforced via `fail_under = 100`
- **Pre-commit hooks** - Automatically run checks before each commit

All checks must pass before code can be merged:

```bash
# Run all quality checks
uv run black --check .
uv run isort --check-only .
uv run ruff check
uv run pyright
uv run coverage run -m pytest && uv run coverage report
```

## Notes

- The project is configured for Python 3.10+ with modern type annotations
- Coverage reports are automatically generated and uploaded to Codecov
- Any code that drops coverage below 100% will fail CI/CD checks
