# Project security plan

- Use synthetic pilot aliases.
- Bind the timing desk to loopback during labs.
- Validate event times against the configured heat window.
- Associate corrections with a local operator alias.
- Escape entrant text when rendering scoreboards.

## Development boundaries

Use synthetic fixtures and least-privilege local accounts. Keep credentials out of source, browser bundles, screenshots, examples, and test output. The example environment file contains configuration names only and is not consumed by an application yet.

For future AWS CI, use GitHub OIDC with an exact repository/branch or protected-environment subject and the expected STS audience. Give the deployment role only its required resources and operations. Do not add permanent AWS access keys to GitHub secrets to bypass identity setup. The current verification workflow has no deployment role.

## Review and reporting

Before introducing external access, add authorization failure cases, validate inputs at the boundary, and document data retention. If a real secret is committed, revoke or rotate it before cleaning up source/history. Avoid posting live values in a public issue.
