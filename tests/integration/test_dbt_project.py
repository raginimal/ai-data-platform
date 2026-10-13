import os
import subprocess
import sys
from pathlib import Path

TRANSFORM = Path(__file__).resolve().parents[2] / "src" / "transform"


def test_dbt_project_parses(tmp_path):
    env = {**os.environ, "DUCKDB_PATH": str(tmp_path / "test.duckdb"), "DBT_TARGET": "test"}
    result = subprocess.run(
        [sys.executable, "-m", "dbt.cli.main", "parse",
         "--project-dir", str(TRANSFORM), "--profiles-dir", str(TRANSFORM),
         "--target-path", str(tmp_path / "target")],
        env=env,
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
