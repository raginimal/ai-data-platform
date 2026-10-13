# ADR-0001: DuckDB as the local store for F1 CSV ingestion

- Status: proposed
- Date: 2026-10-14
- Owners: data platform team
- Baseline impact: change
- Baseline boundaries: BL-DATA, BL-TECH
- Baseline update: no
- Approver: architecture owner (human)

## Context

F1 loads sample sales and customer CSV files into a queryable store. `docs/architecture/baseline.yaml` is still `draft` and approves no data store or language, so this decision needs human approval.

## Decision

Use Python and the embedded DuckDB library (`duckdb`, MIT license) as the data store for F1. Code lives in `src/ingestion/load_csv.py`. Tables `sales` and `customers` are created from CSV files; the database path is a caller parameter (default in-memory).

## Alternatives considered

- SQLite: no native CSV type inference.
- A server database: unnecessary operational cost for sample data.

## Consequences

Adds the `duckdb` and `pytest` (test only) dependencies. No network access, no secrets, no PII (sample data is synthetic).

## Impact and risks

Embedded store only; not an approved production data platform. Schemas are inferred from CSV and have no formal data contract yet.

## Automated controls

Unit tests in `tests/unit/test_load_csv.py`, run by `scripts/test.sh`.

## Review and expiry

Architecture owner to approve or reject; revisit when the baseline is approved.
