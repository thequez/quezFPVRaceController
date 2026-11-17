# Implementation roadmap

All application milestones are open. The initial five contributions establish project identity, design, learning labs, example contracts, and repository verification.

## Milestone 1: Sample heat

- [ ] Write crossing fixtures and hand-score laps.

**Done when:** A second reader can reproduce the order.

## Milestone 2: Timing core

- [ ] Implement parsing, ordering and duplicate handling.

**Done when:** Golden heat passes after shuffled input.

## Milestone 3: Marshal desk

- [ ] Add rulings and a read-only standings page.

**Done when:** Excluded crossing is traceable from the result.

## Milestone 4: Operations rehearsal

- [ ] Export a heat and rebuild a fresh database.

**Done when:** Two exports have identical result digests.

## First implementation issue

In 60 minutes, implement a Go function that accepts six crossings in arbitrary order and emits a stable finish-gate sequence. Add one test with a repeated event ID and attach expected versus observed rows.
