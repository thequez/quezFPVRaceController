# Local development

## What works today

Only the repository verification tools and sample contract checks are executable. See the [README commands](../README.md#start-here). No product server, simulator, database migration, cloud deployment, or model invocation is implemented yet.

## Proposed application setup

Start with a two-pilot synthetic heat and a hand-scored results table. Implement a Go replay command before adding the database or browser view. Run each review against a fresh SQLite file.

Translate this plan into exact supported runtime versions and reproducible setup commands in the first implementation PR. Commit the relevant application dependency lockfiles. Add a minimal health/smoke path and relevant behavioral tests before claiming the application runs.

## First implementation issue

In 60 minutes, implement a Go function that accepts six crossings in arbitrary order and emits a stable finish-gate sequence. Add one test with a repeated event ID and attach expected versus observed rows.

## Working loop

1. Read [the architecture](ARCHITECTURE.md) and [the first lab](LABS.md).
2. Create a short feature branch and choose one acceptance criterion.
3. Implement the smallest local slice with synthetic data and a meaningful failure case.
4. Run `python scripts/verify.py` in the verification environment, plus the new stack's relevant checks.
5. Update the status and setup instructions to distinguish implemented, tested, and unrun behavior. Keep cloud work optional.
