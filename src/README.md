# Source

AI-Ready Data Platform (demo scaffold): Python ingestion loads files into DuckDB `raw`; dbt builds `staging` and `marts`. No features are implemented yet.

```text
src/ingestion/   Python package; only writer to `raw` (PLAT-001)
src/transform/   dbt project (DuckDB profiles via env vars; models/staging, models/marts)
tests/           pytest unit and integration tests
```

Architecture, components, dependencies, and rules: [ARCHITECTURE.md](../ARCHITECTURE.md).

## Setup

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

Environment databases are `data/<env>.duckdb` (gitignored). Use synthetic data only (DATA-005).
