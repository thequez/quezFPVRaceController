# Stack and solution boundaries

## Planned local stack

| Layer | Planned technology | What we will use it for |
| --- | --- | --- |
| Timing engine | Go | Process an ordered fixture deterministically using integer milliseconds. |
| Persistence | SQLite | Store heat configuration, raw crossings and append-only rulings. |
| Operator view | Go templates and HTML | Expose the lap ledger and provisional standings locally. |
| Testing | Go test | Compare standings against a hand-scored fixture. |

## Local implementation path

Start with a two-pilot synthetic heat and a hand-scored results table. Implement a Go replay command before adding the database or browser view. Run each review against a fresh SQLite file.

The stack is a design decision, not an installed toolchain. At the first implementation milestone, choose supported stable runtime versions, commit dependency lockfiles, and document exact setup commands. Avoid selecting preview runtimes just to make the stack look current.

## Optional cloud path

| Planned AWS service | Project-specific purpose |
| --- | --- |
| Amazon S3 | Optionally archive sanitized heat exports for later comparison. |
| AWS Lambda | Optionally recompute a result digest when an export is archived. |

Use a dedicated AWS sandbox and short-lived identity. Infrastructure should be defined and reviewed as code before applying it. Keep service-specific resources in a future `infra/` directory with an explicit teardown path. Identity, logs, encryption keys, networking, and storage retention must be accounted for when that slice is implemented; listing a service here does not imply those dependencies are already configured.

## Verification toolchain shipped now

Python 3.12 and the hash-locked packages in `requirements-dev.lock` validate local documentation links and the JSON Schema fixtures. They are development tools, not the future application's runtime dependencies. CI has read-only repository permissions and does not request cloud credentials.
