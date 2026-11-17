# Cost and cleanup plan

All cloud work is optional and unprovisioned. Set a personal budget before each session and record the chosen region, resource inventory, owner, and expiry date. Budget notifications are delayed signals, not a hard spending cap. Do not assume a service is free because it appears in a lab.

## Project-specific charge drivers and teardown

- Optional S3 charges follow object size, retention and requests. Lambda charges follow invocation count and execution duration. For a later cloud trial, remove its notification, function, logs and archived object versions before deleting the bucket.

## Session workflow

1. Write the smallest experiment and its stop condition. Estimate charges with current regional pricing; include requests, retained data, logs, network transfer, and idle resources.
2. Tag resources with `Project=quezFPVRaceController`, `Series=qez-development-labs`, `Environment=lab`, and an owner/expiry value. Enable the chosen budget alerts before provisioning.
3. Review the infrastructure plan and exact target account. Apply only the planned slice; capture a resource inventory.
4. Stop producers, schedules, and consumers before teardown. Remove lab-owned resources in dependency order using the reviewed infrastructure definition.
5. Inventory retained versions, snapshots, backups, container images, log groups, encryption keys, and network resources. Record which are deleted and which are intentionally retained, with reasons and expiration dates. A successful destroy command alone is not complete cleanup proof.
6. Check the resource inventory and later billing data after teardown. Record the observed cost and any delayed usage charges in the lab evidence.

No teardown automation is shipped yet. Review delete operations against the recorded sandbox inventory; never target another project's resources by name pattern alone.

Reference: [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).
