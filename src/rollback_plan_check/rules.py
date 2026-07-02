from __future__ import annotations

from rollback_plan_check.models import Rule

PROJECT_NAME = 'rollback-plan-check'
SUMMARY = 'Audit release rollback plans for trigger, owner, and data safety details.'
SAMPLE_RISK = 'rollback trigger missing owner unknown data_loss possible'
SAMPLE_CLEAN = 'rollback trigger p95_error owner platform data_loss none'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='missing-trigger',
        severity='high',
        pattern='trigger\\s+(missing|none|unknown)',
        message='rollback trigger is missing',
        recommendation='define measurable rollback trigger',
    ),
    Rule(
        code='unknown-owner',
        severity='medium',
        pattern='owner\\s+(unknown|none|missing)',
        message='rollback owner is missing',
        recommendation='name rollback decision owner',
    ),
    Rule(
        code='data-loss-risk',
        severity='low',
        pattern='data_loss\\s+(possible|unknown)',
        message='data loss risk is unclear',
        recommendation='document data safety constraints',
    ),
)
