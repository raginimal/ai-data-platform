#!/usr/bin/env bash
set -euo pipefail

bash scripts/lint.sh
bash scripts/test.sh
bash scripts/security.sh
bash scripts/validate.sh

echo "Baseline checks passed."
