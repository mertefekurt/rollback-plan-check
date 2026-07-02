# rollback-plan-check

> Audit release rollback plans for trigger, owner, and data safety details.

## CLI contract Overview

Audit release rollback plans for trigger, owner, and data safety details. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 3

Accepts rollback plan. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 3

```bash
python -m pip install -e ".[dev]"
rollback-plan-check examples/sample.txt
rollback-plan-check examples/sample.txt --json --fail-on medium
python -m rollback_plan_check --help
```

## Rule Surface 3

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-trigger` | high | rollback trigger is missing |
| `unknown-owner` | medium | rollback owner is missing |
| `data-loss-risk` | low | data loss risk is unclear |

## Validation Notes 3

```bash
ruff check .
pytest
python -m rollback_plan_check --help
```

Example risky input:

```text
rollback trigger missing owner unknown data_loss possible
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
