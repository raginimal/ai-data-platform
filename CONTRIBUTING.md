# Contributing

Read [docs/developer-workflow.md](docs/developer-workflow.md), [.github/BRANCHING.md](.github/BRANCHING.md), and [.github/definition-of-done.md](.github/definition-of-done.md) before starting. Use [docs/governance/approval-matrix.md](docs/governance/approval-matrix.md) and [docs/governance/risk-classification.md](docs/governance/risk-classification.md) to select reviewers.

## Golden path

```text
Issue -> feature branch -> development -> local validation -> commit -> push
-> Pull Request -> CI -> review -> merge -> build -> deploy
```

## Branches
Use `feature/<issue>-<name>`, `bugfix/<issue>-<name>`, or `hotfix/<issue>-<name>`. `main` is protected: no direct pushes, squash merge is preferred, and the branch must be up to date.

## Local commands

```bash
bash scripts/setup.sh          # configure a new project from PROJECT.yaml
bash scripts/lint.sh           # formatting and lint hooks
bash scripts/test.sh           # unit and available integration tests
bash scripts/security.sh       # deterministic security checks and optional scanners
bash scripts/validate.sh       # repository, policy, and structure checks
bash scripts/check.sh          # baseline validation before commit
bash scripts/build-artifact.sh # produce a versioned local artifact
```

Run `bash scripts/check.sh` before committing. Add stack-overlay commands through the project configuration rather than replacing the core checks.

If a check fails, resolve it or record why it is not applicable; never hide a required failure. Stack overlays may add commands but must preserve the core checks.

## Commits

Use Conventional Commits where the selected stack permits it: `type(scope): imperative summary`. Commits MUST be meaningful, focused, free of secrets and generated output, and traceable to the work item. Do not mix unrelated changes or force-push shared branches without maintainer approval.

For each change, consult the relevant `policies/` document and disclose affected principle IDs in the pull request when applicable. Automated checks may block deterministic violations; architecture, security, data, AI, production, and exception decisions remain human decisions.

## Pull requests
Describe what changed and why. Complete testing, architecture, security, data, AI/model, infrastructure, breaking-change, and AI-assistance sections. Link the issue, identify migrations and rollback needs, and request the appropriate CODEOWNER review.

## Delivery
CI must pass before merge. The pipeline builds one immutable artifact, promotes it through DEV and TEST/UAT, and requires explicit human approval for production. Deployments must be traceable to a commit and have a documented rollback path.

After merge, the release owner follows deployment, monitoring, rollback, and post-deployment validation guidance. Recurring review or operational issues are recorded through the learning loop.

Exceptions use [docs/governance/exceptions.md](docs/governance/exceptions.md) and [docs/adr/exception-template.md](docs/adr/exception-template.md). AI review may advise but cannot approve exceptions, risk acceptance, production deployment, or merge.

## Automation Candidates

| Candidate | Principle ID | Future component | Mode | Trigger | Human approval | Phase |
|---|---|---|---|---|---|---|
| Commit format | DEVOPS-PR-001 | Commit policy check | Deterministic | Commit/PR | No | 4 |
| Local-check evidence | DEVOPS-CI-005 | PR evidence check | Deterministic | PR opened | Reviewer | 4 |
| AI assistance disclosure | AI-005 | PR governance | Deterministic | AI-assisted change | Reviewer | 4 |
