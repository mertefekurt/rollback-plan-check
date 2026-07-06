# Rollback Plan Check

| | |
| --- | --- |
| Focus | deployment safety |
| Command | `rollback-plan-check` |
| Inputs | text, JSON, JSONL, or CSV |
| Output | Markdown or JSON |

![Rollback Plan Check cover](assets/readme-cover.svg)

Audit release rollback plans for trigger, owner, and data safety details. This repo keeps the work close to the terminal: clear input, predictable output, and no service to babysit.

## Policy surface

| Rule | Level | Why it matters |
| --- | --- | --- |
| `missing-trigger` | high | rollback trigger is missing |
| `unknown-owner` | medium | rollback owner is missing |
| `data-loss-risk` | low | data loss risk is unclear |

## Local run

```bash
git clone https://github.com/mertefekurt/rollback-plan-check.git
cd rollback-plan-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
rollback-plan-check examples/sample.txt
rollback-plan-check examples/sample.txt --json
```

## Why the sample fails

`rollback trigger missing owner unknown data_loss possible` is intentionally shaped to hit the rules above, so it is useful as a quick smoke test after edits.
