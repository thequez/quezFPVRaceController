# Contract: Gate crossing

The version-one contract is in [record.schema.json](../contracts/record.schema.json), using JSON Schema Draft 2020-12. Its records are synthetic and do not come from a real user, device, account, patient, or organization.

| Field | Type | Meaning |
| --- | --- | --- |
| event_id | string | Unique detection identifier. |
| heat_id | string | Configured synthetic heat. |
| pilot_alias | string | Entrant alias registered for the heat. |
| gate_id | string | Timing gate label. |
| elapsed_ms | integer | Milliseconds after the heat start. |

## Fixtures

- [Valid example](../examples/record.valid.json): must pass schema validation.
- [Missing required field](../examples/record.missing-field.json): must fail.
- [Wrong field type](../examples/record.wrong-type.json): must fail.

The verifier checks all three outcomes with `jsonschema` and a format checker. String lengths and collection sizes have basic bounds. The schema describes structure; domain rules, cross-record relationships, authorization, retries, and calculations must be implemented and tested in the application. Tighten semantic constraints with a documented compatibility decision as the first slice is built.

The sample does not imply an HTTP endpoint or event producer exists. Keep a stable schema at an integration boundary; add migrations or versioned contracts when a consumer cannot accept a change.
