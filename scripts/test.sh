#!/usr/bin/env bash
set -euo pipefail

if test -d tests && find tests -type f -name 'test_*.py' -print -quit | grep -q .; then
  python -m pytest tests -q
  exit 0
fi

if test -d tests && find tests -type f -not -name README.md -print -quit | grep -q .; then
  echo "Project tests detected; configure the stack overlay test command in scripts/test.sh."
  exit 1
fi

echo "No application tests configured in the technology-neutral core."
