# Five practice labs

These are implementation exercises, not completed lab results. Start locally; the cloud exercise is optional. Capture actual commands and results in the [evidence template](../evidence/TEMPLATE.md).

## Lab 01: Score a heat by hand

**Task:** Record two pilots and six crossings with an expected lap order.

**Acceptance:** Each expected lap links to a crossing ID.

**Break/fix:** Shuffle input rows and explain the expected order.

**Evidence:** Annotated timing sheet.

**Cleanup:** Discard the working copy.

## Lab 02: Replay crossings

**Task:** Implement the pure scorer with explicit duplicate rules.

**Acceptance:** Two runs produce identical lap rows.

**Break/fix:** Duplicate one event and verify its effect is zero.

**Evidence:** Golden test output.

**Cleanup:** Remove the temporary database.

## Lab 03: Review a correction

**Task:** Validate marshal rulings and record their source locally.

**Acceptance:** The original event survives an exclusion.

**Break/fix:** Reference an unknown event and verify rejection.

**Evidence:** Before-and-after ledger excerpt.

**Cleanup:** Reset the sample heat.

## Lab 04: Archive a result

**Task:** Sketch an optional S3 event adapter and invoke its handler locally.

**Acceptance:** Repeated delivery yields the same digest.

**Break/fix:** Pass a missing heat ID and report a validation error.

**Evidence:** Handler transcript and cost worksheet.

**Cleanup:** Delete local archives and temp files.

**Optional live AWS follow-through:** Once the local slice and its infrastructure definition exist, implement the smallest sandbox experiment using Amazon S3, AWS Lambda. Review the resource plan, authenticate with a short-lived lab session, capture the project-specific result, and compare it with the local baseline. Prove one denied access case, then record resource inventory and cleanup using the cost guide. Mark this portion unrun until those results exist; a diagram alone does not complete it.

## Lab 05: Recover the standings

**Task:** Rebuild the view from a raw ledger and its rulings.

**Acceptance:** Digest matches the approved heat.

**Break/fix:** Remove the derived table before reprocessing.

**Evidence:** Recovery time and digest pair.

**Cleanup:** Remove the recovery copy.
