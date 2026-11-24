---
description: "Use when writing or updating pytest tests for the expense tracker."
applyTo: "tests/**/*.py"
---

# Test Guidelines

- Use pytest and keep tests in `tests/`, with one module for the behavior under
  test when practical.
- Use `tmp_path` and `make_store(tmp_path)` for filesystem-backed tests. Do not
  write test data into the repository.
- Use `tests.conftest.args(...)` for direct command-handler calls and assert the
  returned exit code plus persisted state or captured CLI output.
- Add focused positive, validation, and empty/no-match cases appropriate to the
  behavior. Test observable behavior rather than internal implementation details.
- For money tests, assert integer cents for parsing and `$`-formatted strings for
  display; include invalid amount boundaries when changing `money.py`.
