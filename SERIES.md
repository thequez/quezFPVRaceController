# qez Development Lab Series

This is an 18-project development program owned by [thequez](https://github.com/thequez). The original 13 repositories form the **Core track**; five additional projects form the **AWS AI track**. Each is a separate project to build, troubleshoot, document, and operate, with its own stack and learning evidence.

This repository is **project 01: quezFPVRaceController**, in the **Core track**. Repository names and existing descriptions guide the project ideas; assumptions are documented in each README. Some linked repositories are private and require access.

## Program directory

| Project | Repository | Practice focus | Track |
| --- | --- | --- | --- |
| 01 | [quezFPVRaceController](https://github.com/thequez/quezFPVRaceController) | Replay a heat from the same gate events the timing desk saw. | Core |
| 02 | [quezFPV](https://github.com/thequez/quezFPV) | Turn a simulator session into a searchable flight record. | Core |
| 03 | [360RuckPack](https://github.com/thequez/360RuckPack) | Compare packing lists by mass, category and revision. | Core |
| 04 | [quez.shop](https://github.com/thequez/quez.shop) | Follow a fictional order from a cart to a reconciled receipt. | Core |
| 05 | [TomatoSensory](https://github.com/thequez/TomatoSensory) | Trace a blind tasting score from a paper ballot to a variety summary. | Core |
| 06 | [obsidian-secondbrain](https://github.com/thequez/obsidian-secondbrain) | Find broken note links and rebuild a disposable index from Markdown. | Core |
| 07 | [EsportsLockIn](https://github.com/thequez/EsportsLockIn) | Resolve roster and map conflicts before a practice night starts. | Core |
| 08 | [qez-local](https://github.com/thequez/qez-local) | Answer a question from a small local collection and show the supporting passage. | Core |
| 09 | [qez-IThomelab](https://github.com/thequez/qez-IThomelab) | Practice employee lifecycle changes across a disposable office environment. | Core |
| 10 | [qez-servicedesk](https://github.com/thequez/qez-servicedesk) | Trace one support ticket through triage, escalation and a verified resolution. | Core |
| 11 | [quez-explorer](https://github.com/thequez/quez-explorer) | Select a local action from a configurable radial wheel using a mouse or keyboard. | Core |
| 12 | [backendgallery](https://github.com/thequez/backendgallery) | Follow an image from intake through durable thumbnail processing to a ready gallery entry. | Core |
| 13 | [ketofast](https://github.com/thequez/ketofast) | Make a private, time-zone-aware record of meal notes and elapsed intervals. | Core |
| 14 | [qez-agent-supportops](https://github.com/thequez/qez-agent-supportops) | Grounded support investigation with human-approved actions | AWS AI |
| 15 | [qez-generative-ui](https://github.com/thequez/qez-generative-ui) | Schema-validated operational interfaces built from approved components | AWS AI |
| 16 | [qez-agent-evals](https://github.com/thequez/qez-agent-evals) | Repeatable evaluations for tool use, grounding, latency, and cost | AWS AI |
| 17 | [qez-agent-finops](https://github.com/thequez/qez-agent-finops) | Read-only cost investigations with evidence and reviewable recommendations | AWS AI |
| 18 | [qez-agent-docflow](https://github.com/thequez/qez-agent-docflow) | Document extraction, cited evidence, exception routing, and human review | AWS AI |

## Suggested progression

1. Choose one local project and complete its smallest useful slice. Record baseline behavior and a meaningful failing case.
2. Add persistence, migration, validation, and API boundaries where the project needs them.
3. Practice review, repeatable checks, structured logging, and a break/fix exercise.
4. Attempt one optional AWS lab in a sandbox, recording design choices, IAM scope, charge drivers, and cleanup.
5. Repeat in a different stack. Use the AWS AI track for bounded tool use, typed generated interfaces, evaluation, and human-reviewed workflows.

Do not build all projects or deploy every AWS service at once. Use the certification mapping as a skills checklist alongside the current official exam guide. The series is a personal learning program, not vendor-endorsed training or a guarantee of exam coverage.

## Evidence standard

Keep the input, expected result, observed result, failure diagnosis, fix, retest, and cleanup verification for each lab. Start with [the evidence template](evidence/TEMPLATE.md). Use synthetic data; redact account IDs, tokens, personal records, and unnecessary resource identifiers before sharing.
