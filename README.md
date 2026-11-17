# quezFPVRaceController — Race timing desk

> **qez Development Lab Series · Project 01/18 · Core track 01/13**
>
> This repository belongs to a coordinated series of development and certification-practice projects by [thequez](https://github.com/thequez). Each project explores a different engineering problem and set of industry practices. [Browse the series](SERIES.md).

Replay a heat from the same gate events the timing desk saw.

## The program we will build

A timing volunteer needs to explain why one pilot gained a lap when two gate detections arrived close together.

**For:** FPV club timing volunteers and developers practicing event-driven systems.

## Status

**Project blueprint and verification scaffold.** Implemented today: this brief, stack and architecture plans, five labs, certification skill mapping, a JSON Schema with synthetic fixtures, and CI that checks these artifacts. The application, cloud infrastructure, and live integrations are planned. Passing CI validates this scaffold; it does not establish application behavior, deployment, or certification readiness.

## First useful version

- Import timestamped gate detections from JSON Lines.
- Assign eligible detections to entrants within one heat.
- Flag suspected duplicate detections for a marshal.
- Apply a correction while preserving the original event.
- Rebuild standings and export an adjudication log.

## Planned stack

| Layer | Planned technology | What we will use it for |
| --- | --- | --- |
| Timing engine | Go | Process an ordered fixture deterministically using integer milliseconds. |
| Persistence | SQLite | Store heat configuration, raw crossings and append-only rulings. |
| Operator view | Go templates and HTML | Expose the lap ledger and provisional standings locally. |
| Testing | Go test | Compare standings against a hand-scored fixture. |

## Optional AWS extension

| Planned AWS service | Project-specific purpose |
| --- | --- |
| Amazon S3 | Optionally archive sanitized heat exports for later comparison. |
| AWS Lambda | Optionally recompute a result digest when an export is archived. |

Start with the local path. AWS resources are not provisioned by this repository or its CI. Review the [cost and teardown plan](docs/COST-AND-CLEANUP.md) before a cloud lab.

## What we are practicing

- Idempotent ingest
- Event-time ordering
- Integer duration arithmetic
- Append-only corrections
- Golden-file testing
- Replayable audit trails

## Start here

Use **Python 3.12** for the repository verification tools; this is separate from the planned application stack above.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --require-hashes -r requirements-dev.lock
.\.venv\Scripts\python.exe scripts/verify.py
```

On macOS/Linux, use `python3.12 -m venv .venv` and `.venv/bin/python` for the other two commands. Verification requires no AWS account, credentials, model calls, or running application.

**First implementation task:** In 60 minutes, implement a Go function that accepts six crossings in arbitrary order and emits a stable finish-gate sequence. Add one test with a repeated event ID and attach expected versus observed rows.

## Project guides

| Guide | What it answers |
| --- | --- |
| [Series directory](SERIES.md) | How this repo fits the 18-project program |
| [Stack](docs/STACK.md) | Technology choices and local/cloud boundaries |
| [Architecture](docs/ARCHITECTURE.md) | Data flow and design tradeoffs |
| [Labs](docs/LABS.md) | Five hands-on exercises, failures, and evidence |
| [Certification mapping](docs/CERTIFICATIONS.md) | Skills practiced and evidence to retain |
| [Local development](docs/LOCAL-DEVELOPMENT.md) | What runs today and the first implementation task |
| [Roadmap](docs/ROADMAP.md) | Milestones with acceptance criteria |
| [Contracts](docs/CONTRACTS.md) | Versioned synthetic example and validation |
| [Security](docs/SECURITY.md) | Threats and access boundaries |
| [Costs and cleanup](docs/COST-AND-CLEANUP.md) | AWS charge drivers and teardown evidence |
| [Runbook](docs/RUNBOOK.md) | Diagnosis and recovery exercises |
| [Contributing](CONTRIBUTING.md) | Review, testing, and the definition of done |

## Scope assumptions

- Assume controller means the race desk and heat clock. All gate signals originate in synthetic files. No aircraft connection is planned.

Out of scope for the first version:

- Aircraft control
- Radio-frequency configuration
- Official race certification

## Check a local record

After installing the verification dependencies, run the following from the repository root. The checker validates the record schema and timing offsets. A rejected record prints a diagnostic and exits with status 1.

```sh
python scripts/check_record.py examples/record.valid.json
python scripts/check_record.py examples/record.domain-invalid.json
python -m unittest discover -s tests
```
