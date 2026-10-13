import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from ingestion.load_csv import load_csv_files  # noqa: E402

SAMPLES = ROOT / "src" / "ingestion" / "samples"


def test_loads_sample_files_into_tables():
    con = load_csv_files(SAMPLES / "sales.csv", SAMPLES / "customers.csv")
    try:
        assert con.execute("SELECT count(*) FROM sales").fetchone()[0] == 4
        assert con.execute("SELECT count(*) FROM customers").fetchone()[0] == 3
        cols = [r[0] for r in con.execute("DESCRIBE customers").fetchall()]
        assert cols == ["customer_id", "name", "country", "signup_date"]
    finally:
        con.close()


def test_sales_join_customers():
    con = load_csv_files(SAMPLES / "sales.csv", SAMPLES / "customers.csv")
    try:
        rows = con.execute(
            "SELECT count(*) FROM sales s JOIN customers c USING (customer_id)"
        ).fetchone()[0]
        assert rows == 4
    finally:
        con.close()


def test_reload_is_idempotent(tmp_path):
    db = str(tmp_path / "f1.duckdb")
    load_csv_files(SAMPLES / "sales.csv", SAMPLES / "customers.csv", db).close()
    con = load_csv_files(SAMPLES / "sales.csv", SAMPLES / "customers.csv", db)
    try:
        assert con.execute("SELECT count(*) FROM sales").fetchone()[0] == 4
    finally:
        con.close()


def test_rejects_missing_file(tmp_path):
    with pytest.raises(ValueError):
        load_csv_files(tmp_path / "nope.csv", SAMPLES / "customers.csv")


def test_rejects_non_csv(tmp_path):
    other = tmp_path / "data.txt"
    other.write_text("a,b\n1,2\n")
    with pytest.raises(ValueError):
        load_csv_files(SAMPLES / "sales.csv", other)
