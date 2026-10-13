#!/usr/bin/env bash
set -euo pipefail

# Stack-overlay dependency scanner required by ARCH-DEP-004.
python -m pip_audit .
