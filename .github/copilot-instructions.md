# GitHub Copilot Instructions

## What This Is

This is a small, dependency-free Python command-line expense tracker. It stores
expenses in a local JSON file and has add, list, and delete commands.

The package entry point is `expense_tracker/__main__.py`; CLI parsing and
dispatch live in `expense_tracker/cli.py`. Command implementations live in
`expense_tracker/commands/`, shared persistence in `storage.py`, and money
handling in `money.py`.

## Stack & Versions

- Python 3.10 or newer; runtime dependencies are intentionally empty.
- pytest 8 or newer for tests.
- Ruff 0.6 or newer for linting and formatting.
- Ruff is configured for a 100-character line length and Python 3.10 syntax.

## How to Run Things

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

python -m expense_tracker <command> [options]
pytest
ruff check .
ruff format .
```

Use `EXPENSE_TRACKER_DATA` to point `Store` at a test or alternate JSON file.
The CLI is also exposed by the `expense-tracker` project script.

## Conventions

- Follow PEP 8 and the settings in `pyproject.toml`.
- Use `snake_case` for functions and variables and `PascalCase` for classes.
- Add type hints to public functions and keep module-level functions
  self-documenting; preserve the existing Google-style docstrings where they
  are used.
- Keep dependencies and abstractions small. Do not add a framework or database
  without an explicit requirement.
- Update `README.md` when setup, commands, or storage behavior changes.

## Boundaries

- Do not change `exercise_spec/` unless the request explicitly asks for it.
- Do not introduce React, SQL, Kubernetes, observability, or API conventions;
  they do not belong to this repository.
- Never log or commit personal or financial data. Use `tmp_path` for test data.
- Do not convert integer cents or ISO 8601 strings to floats or guessed formats.


## Definition of Done

- The requested behavior works through `python -m expense_tracker`.
- New behavior has focused pytest coverage.
- `pytest`, `ruff check .`, and `ruff format --check .` pass.
- JSON persistence and existing CLI output remain compatible unless the task
  explicitly changes their contract.
- The final diff is limited to the requested files and contains no secrets or
  unrelated source changes.
