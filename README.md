# Skill Optimizer

`skill-optimizer` is a governance skill for auditing other skills. It analyzes the current conversation plus locally visible skill directories, finds problems such as missed triggers, weak metadata, duplicates, stale references, and risky workflows, then produces a detailed report with a short action queue the user can choose from.

## What It Does

- audits the current thread and visible skill roots
- identifies duplicate or overlapping skills
- flags weak metadata and missing `agents/openai.yaml`
- spots risky skills that need clearer guardrails
- separates analysis from execution
- limits user-facing actions to:
  - `修复`
  - `合并`
  - `删除`
  - `保留并跳过`

## Package Layout

```text
skill-optimizer/
  SKILL.md
  agents/openai.yaml
  references/report-schema.md
  evals/evals.json
examples/
  sample-report.md
scripts/
  build_release.py
VERSION
LICENSE
README.md
```

## Marketplace Positioning

This skill is a good fit for:

- ClawHub / OpenClaw registries
- Claude custom skill uploads
- community skill directories that accept GitHub repos or ZIP files

It is especially useful for users who maintain many local skills and want a safer way to clean up duplication before making changes.

## Safety Model

- audit first, edit later
- never deletes anything during analysis
- asks the user to choose actions before modifying files
- treats "unused" as a weak signal unless stronger evidence exists

## Recommended Metadata

- Name: `skill-optimizer`
- Short description: `Audit skills and produce an actionable cleanup plan`
- Tags: `governance`, `audit`, `developer-tools`, `skills`, `cleanup`

## Example Prompts

- `Use $skill-optimizer to audit my current workspace skills and tell me what should be fixed, merged, deleted, or skipped.`
- `Please inspect this skill repo for duplicate skills, weak metadata, and missing guardrails, then give me an action queue.`
- `Audit the current thread and my installed skills to find places where a skill should have triggered but did not.`

## Build Release Artifacts

From this directory:

```bash
python3 scripts/build_release.py
```

The script creates:

- `dist/clawhub/skill-optimizer-v<version>-clawhub.zip`
- `dist/claude/skill-optimizer-v<version>-claude.zip`

The Claude package uses `Skill.md` naming for compatibility with Claude upload docs. The ClawHub package keeps `SKILL.md`.

## Publish Flow

### GitHub

1. Create a repository and upload this directory.
2. Tag a version such as `v0.1.0`.
3. Attach the ZIP artifacts from `dist/` to a release.

### ClawHub

1. Build the release package.
2. Publish the ClawHub artifact or point ClawHub at the unpacked skill directory.
3. Verify listing metadata and installation instructions.

### Claude Custom Skill Upload

1. Build the Claude artifact.
2. In Claude, go to custom Skills upload.
3. Upload the generated Claude ZIP.

## Notes

- The package intentionally avoids machine-specific absolute paths.
- `examples/sample-report.md` shows the intended reporting style.
- `evals/evals.json` contains starter prompts for internal regression testing.
