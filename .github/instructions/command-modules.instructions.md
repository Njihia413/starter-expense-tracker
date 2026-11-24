---
description: "Use when adding or modifying expense-tracker CLI command modules and command registration."
applyTo: "expense_tracker/commands/**/*.py"
---

# Command Module Guidelines

- Follow the existing module shape: export `NAME`, `HELP`, `add_parser`, and
  `handle`.
- Register a new command module in `expense_tracker/commands/__init__.py`.
- `add_parser(subparsers)` defines positional arguments and options.
- `handle(args, store)` loads and saves only as needed, prints user-facing output,
  and returns an integer exit code.
- Return `0` for success and `1` for a handled command error. Match existing
  output names and formats unless the task changes the CLI contract.
- Reuse `parse_amount`, `format_amount`, `Store`, and `Expense` instead of
  duplicating money or persistence logic.
