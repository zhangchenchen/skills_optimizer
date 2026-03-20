# Skill Optimizer

`skill-optimizer` is a governance skill for auditing other skills. It analyzes the current conversation plus locally visible skill directories, finds problems such as missed triggers, weak metadata, duplicates, stale references, and risky workflows, then produces a detailed report with a short action queue the user can choose from.

## Why Use It

- Audit the current thread and visible skill roots
- Identify duplicate or overlapping skills
- Flag weak metadata and missing `agents/openai.yaml`
- Spot risky skills that need clearer guardrails
- Separate analysis from execution
- Keep user-facing actions simple:
  - `Fix`
  - `Merge`
  - `Delete`
  - `Keep and Skip`

## Quick Guide

### 1. Run an audit

Ask the agent to inspect the current thread and your visible skills:

```text
Use $skill-optimizer to audit my current workspace skills and tell me what should be fixed, merged, deleted, or skipped.
```

### 2. Read the report

The skill returns:

- an executive summary
- findings grouped by issue type
- an action queue with one item per recommended intervention

### 3. Choose actions

Reply using one line per decision:

```text
I01 -> Fix
I02 -> Merge
I03 -> Keep and Skip
```

### 4. Apply changes

After you choose actions, the agent can move on to implementation:

- update metadata
- synchronize `agents/openai.yaml`
- consolidate duplicates
- remove confirmed leftovers

## What You Get

Typical finding categories include:

- missed triggers
- weak metadata
- duplicate or overlapping skills
- stale files or references
- risky workflows with weak guardrails
- install or maintenance problems

## Example Prompts

- `Use $skill-optimizer to audit my current workspace skills and tell me what should be fixed, merged, deleted, or skipped.`
- `Please inspect this skill repo for duplicate skills, weak metadata, and missing guardrails, then give me an action queue.`
- `Audit the current thread and my installed skills to find places where a skill should have triggered but did not.`

## Safety Model

- audit first, edit later
- never deletes anything during analysis
- asks the user to choose actions before modifying files
- treats "unused" as a weak signal unless stronger evidence exists

## Example Output

See [examples/sample-report.md](./examples/sample-report.md) for a sample report format.

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

## For Maintainers

### Build release artifacts

From this directory:

```bash
python3 scripts/build_release.py
```

The script creates:

- `dist/clawhub/skill-optimizer-v<version>-clawhub.zip`
- `dist/claude/skill-optimizer-v<version>-claude.zip`

The Claude package uses `Skill.md` naming for compatibility with Claude upload docs. The ClawHub package keeps `SKILL.md`.

## Notes

- The package intentionally avoids machine-specific absolute paths.
- `evals/evals.json` contains starter prompts for internal regression testing.
