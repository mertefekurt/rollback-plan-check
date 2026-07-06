# Rollback Plan Check

<p align="center">
  <img src="assets/readme-cover.svg" alt="Rollback Plan Check cover" width="100%" />
</p>

![stack](https://img.shields.io/badge/stack-Python-7c3aed?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-0891b2?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-b45309?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-be185d?style=flat-square)

Audit release rollback plans for trigger, owner, and data safety details.

## The short version

`rollback-plan-check` is intentionally small: feed it a file, get deterministic findings, and decide whether the result should block a merge or just guide cleanup.

## Rule surface

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-trigger` | high | rollback trigger is missing |
| `unknown-owner` | medium | rollback owner is missing |
| `data-loss-risk` | low | data loss risk is unclear |

## Usage

```bash
python -m pip install -e ".[dev]"
rollback-plan-check examples/sample.txt
rollback-plan-check examples/sample.txt --json --fail-on medium
```

## Useful defaults

| Option | Reason |
| --- | --- |
| `--json` | machine-readable output for scripts |
| `--fail-on medium` | stricter CI gate when warnings matter |
| `--format auto` | let the reader detect text, CSV, JSON, or JSONL |

## Local checks

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m rollback_plan_check --help
```
