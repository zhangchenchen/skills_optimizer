# Skill Optimizer

[English](./README.md) | [中文](./README.zh-CN.md)

`skill-optimizer` is a governance skill for auditing other skills. It analyzes the current conversation plus locally visible skill directories, finds problems such as missed triggers, weak metadata, duplicates, stale references, and risky workflows, then produces a detailed report with follow-up optimization strategies.

## Why Use It

- Audit the current thread and visible skill roots
- Identify duplicate or overlapping skills
- Flag weak metadata and missing `agents/openai.yaml`
- Spot risky skills that need clearer guardrails
- Separate analysis from execution
- Turn findings into clear next-step strategies

## Quick Guide

### 1. Run an audit

Ask the agent to inspect the current thread and your visible skills:

```text
Use $skill-optimizer to audit my current workspace skills and give me a report plus follow-up optimization strategies.
```

### 2. Read the report

The report usually includes:

- an executive summary
- findings grouped by issue type
- an action queue
- follow-up optimization strategies

### 3. Decide what to do next

This skill analyzes first and does not silently modify files during the audit step. After reviewing the report, you can decide which improvements to apply.

## What You Get

Typical findings include:

- places where a skill should have triggered but did not
- weak or incomplete metadata
- duplicate or highly overlapping skills
- stale files, references, or supporting resources
- risky workflows with weak guardrails
- installation or maintenance process problems

## Example Prompts

- `Use $skill-optimizer to audit my current workspace skills and give me a report plus follow-up optimization strategies.`
- `Please inspect this skill repo for duplicate skills, weak metadata, and missing guardrails, then give me a report and next-step recommendations.`
- `Audit the current thread and my installed skills to find places where a skill should have triggered but did not.`

## How It Works

This skill is designed around a few principles:

- audit first, edit later
- provide evidence before recommendations
- separate analysis from execution
- avoid treating "unused" as automatic proof that a skill should be deleted

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
README.zh-CN.md
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
- `evals/evals.json` contains starter prompts for regression testing.
