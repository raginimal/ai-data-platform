"""F1: load sales and customer CSV files into DuckDB tables."""

from __future__ import annotations

from pathlib import Path

import duckdb

TABLES = ("sales", "customers")


def _check_file(path: Path) -> Path:
    resolved = Path(path).resolve()
    if resolved.suffix.lower() != ".csv" or not resolved.is_file():
        raise ValueError(f"Expected an existing .csv file: {path}")
    return resolved


def load_csv_files(
    sales_csv: Path, customers_csv: Path, database: str = ":memory:"
) -> duckdb.DuckDBPyConnection:
    """Create or replace the `sales` and `customers` tables from CSV files.

    Returns an open connection; the caller is responsible for closing it.
    """
    files = {"sales": _check_file(sales_csv), "customers": _check_file(customers_csv)}
    con = duckdb.connect(database)
    try:
        for table, path in files.items():
            # Table names are fixed constants; the path is bound as a parameter.
            con.execute(
                f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM read_csv(?, header = true)",
                [str(path)],
            )
    except Exception:
        con.close()
        raise
    return con
