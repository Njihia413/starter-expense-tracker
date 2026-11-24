---
description: "Use when changing Python package code, models, money handling, JSON persistence, or CLI entry points."
applyTo: "expense_tracker/**/*.py"
---

# Python Package Guidelines

- Keep the package dependency-free; use the standard library.
- Represent money as integer cents. Parse and format through `money.py`; do not
  use floats or silently round decimal input.
- Use `models.Expense` for expense data and preserve its JSON keys and dataclass
  shape unless persistence compatibility is intentionally changed.
- Validate ISO 8601 dates at the input boundary. Keep `YYYY-MM-DD` strings in
  storage and calculations.
- Use `pathlib.Path` for file paths. `storage.Store` owns JSON loading and
  saving and `EXPENSE_TRACKER_DATA` resolution.
- Keep CLI dispatch thin. `cli.py` builds parsers and routes registered command
  modules; command behavior belongs in `expense_tracker/commands/`.
- Preserve existing exit-code behavior: command success returns `0`, handled
  errors print an `error: ...` message and return `1`.
