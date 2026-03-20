# Report Schema

Use this schema when `skill-optimizer` produces its audit report.

## Report Structure

Always use this top-level shape:

```md
# Skill Audit Report

## Executive Summary

## Findings

### Missed Trigger Cases

### Duplicate Or Overlapping Skills

### Metadata Quality Issues

### Risk And Safety Review

### Installation And Maintenance Workflow

## Action Queue
```

Only include sections that have meaningful content, but always include `Executive Summary`, `Findings`, and `Action Queue`.

## Finding Record

Each finding should contain:

- `id`
- `title`
- `category`
- `target_skills`
- `evidence`
- `why_it_matters`
- `recommended_action`
- `available_actions`

Recommended markdown shape:

```md
#### I01 - Duplicate copies of `baoyu-url-to-markdown`
- Category: `duplicate_skill`
- Target skills: `baoyu-url-to-markdown`
- Evidence:
  - Found active copies in multiple directories
  - Similar purpose and overlapping files indicate maintenance duplication
- Why it matters: Duplicate active copies raise maintenance cost and can create trigger ambiguity.
- Recommended action: `合并`
- Available actions: `修复 / 合并 / 删除 / 保留并跳过`
```

## Action Queue Record

Each action queue item should be self-contained and easy for the user to choose from.

Use this shape:

```md
- `I01`
  Title: Duplicate copies of `baoyu-url-to-markdown`
  Recommendation: `合并`
  Why: There are multiple active copies and no clear canonical source.
  Options: `修复 / 合并 / 删除 / 保留并跳过`
```

If the UI or conversation format benefits from more structure, the same information can be expressed in YAML-like blocks:

```yaml
id: I01
title: Duplicate copies of baoyu-url-to-markdown
category: duplicate_skill
target_skills:
  - baoyu-url-to-markdown
severity: medium
confidence: high
evidence:
  - Multiple active copies found in visible skill roots
why_it_matters: Duplicate active copies make maintenance and triggering less predictable
recommended_action: 合并
available_actions:
  - 修复
  - 合并
  - 删除
  - 保留并跳过
```

## Action Semantics

Keep the four actions stable:

- `修复`
  Update metadata, trigger wording, safety language, structure, or stale files.
- `合并`
  Consolidate duplicate or overlapping skills into a clearer single source of truth.
- `删除`
  Remove the selected skill or duplicate copy after the user explicitly chooses deletion.
- `保留并跳过`
  Record the finding as reviewed for now, but make no changes.

## User Reply Format

Prompt the user to reply using one line per action:

```text
I01 -> 修复
I02 -> 合并
I03 -> 删除
I04 -> 保留并跳过
```

If a chosen action is ambiguous, ask a narrow follow-up question before editing files.
