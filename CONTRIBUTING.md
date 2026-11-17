# Contributing to the qez Development Lab Series

Start with the [project roadmap](docs/ROADMAP.md). Keep one feature branch focused on a reviewable behavior, failure, or documentation outcome. No open-source license has been selected; repository visibility alone is not a license grant.

## Before a change

Read the stack, architecture, security plan, and relevant lab. State the acceptance criterion and use synthetic inputs. Preserve project boundaries and the visible series identity in the README.

## Checks and review

Install Python 3.12 verification dependencies with `python -m pip install --require-hashes -r requirements-dev.lock`, then run `python scripts/verify.py`. Application changes also need the appropriate stack checks and meaningful behavioral tests. The scaffold checker cannot validate a future application.

Review the diff for credentials, personal records, generated clutter, incorrect status claims, broken local links, and deployment side effects. Use the PR template to report passed, failed, and unrun checks. Keep logs and evidence redacted.

## Definition of done

- The changed behavior meets its stated acceptance criterion and relevant failure handling is verified.
- Documentation describes what actually exists and how to reproduce it.
- Schema changes explain consumer compatibility; persistence changes include migrations and recovery.
- Optional AWS work has least-privilege identity, an explicit cost estimate, resource inventory, and cleanup proof.
- Dependency changes update the appropriate lockfile. Use supported runtimes; review GitHub Action pin updates.

The initial branch is `main`. Once a baseline exists, use pull requests and configure required checks in repository settings as desired; branch protection is not automatically configured by this scaffold.
