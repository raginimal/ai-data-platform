#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root_dir"

required_files=(README.md AGENTS.md CONTRIBUTING.md ARCHITECTURE.md SECURITY.md AI_POLICY.md DATA_POLICY.md PROJECT.yaml Makefile .github/CODEOWNERS .github/pull_request_template.md docs/architecture/baseline.yaml)
for file in "${required_files[@]}"; do
  test -f "$file" || { echo "FAILED RP-001: missing required file: $file" >&2; exit 1; }
done

required_dirs=(.github docs src tests ai infrastructure config policies scripts)
for directory in "${required_dirs[@]}"; do
  test -d "$directory" || { echo "FAILED RP-001: missing required directory: $directory" >&2; exit 1; }
done

if test -f CODEOWNERS; then
  echo "FAILED RP-002: duplicate root CODEOWNERS found; use .github/CODEOWNERS." >&2
  exit 1
fi

if grep -RInE 'CHANGE_ME|YOUR_|REPLACE_ME' --exclude-dir=.git --exclude='PROJECT.yaml' --exclude='CODEOWNERS' --exclude='setup.sh' --exclude='validate.sh' --exclude='*.template.yaml' .; then
  echo "FAILED RP-001: unresolved placeholder found outside approved templates." >&2
  exit 1
fi

if grep -RInE '(AKIA[0-9A-Z]{16}|-----BEGIN (RSA |EC )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9_]{20,})' --exclude-dir=.git .; then
  echo "Possible secret pattern found" >&2
  exit 1
fi

echo "PASS RP-001: required repository structure is present."
echo "PASS RP-002: .github/CODEOWNERS is the only authoritative CODEOWNERS file."
