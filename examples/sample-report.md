# Skill Audit Report

## Executive Summary

Three themes stand out:

- duplicate skill copies are causing maintenance drift
- several skills under-describe when they should trigger
- one publishing skill needs a stronger confirmation checkpoint

## Findings

### Duplicate Or Overlapping Skills

#### I01 - Duplicate copies of `rss-source-picker`
- Category: `duplicate_skill`
- Target skills: `rss-source-picker`
- Evidence:
  - Multiple visible copies were found in active skill roots
  - Descriptions overlap and create no clear canonical source
- Why it matters: Duplicate active copies make future fixes inconsistent.
- Recommended action: `Merge`
- Available actions: `Fix / Merge / Delete / Keep and Skip`

### Metadata Quality Issues

#### I02 - `social-polish` under-describes its input contract
- Category: `weak_metadata`
- Target skills: `social-polish`
- Evidence:
  - The body explains bundle-based input clearly
  - The frontmatter does not strongly say that it expects a Chinese opinion draft, not raw English source material
- Why it matters: The skill may under-trigger or get used too early.
- Recommended action: `Fix`
- Available actions: `Fix / Merge / Delete / Keep and Skip`

### Risk And Safety Review

#### I03 - `baoyu-post-to-wechat` needs an explicit publish confirmation checkpoint
- Category: `risky_skill`
- Target skills: `baoyu-post-to-wechat`
- Evidence:
  - The workflow supports real write actions to WeChat
  - The confirmation step was not prominent enough
- Why it matters: High-consequence actions should confirm target account and publish intent before execution.
- Recommended action: `Fix`
- Available actions: `Fix / Merge / Delete / Keep and Skip`

## Action Queue

- `I01`
  Title: Duplicate copies of `rss-source-picker`
  Recommendation: `Merge`
  Why: Multiple active copies create drift and no single source of truth.
  Options: `Fix / Merge / Delete / Keep and Skip`

- `I02`
  Title: `social-polish` needs stronger metadata
  Recommendation: `Fix`
  Why: The body is clear, but the trigger description is still weaker than the real usage boundary.
  Options: `Fix / Merge / Delete / Keep and Skip`

- `I03`
  Title: `baoyu-post-to-wechat` needs an explicit confirmation gate
  Recommendation: `Fix`
  Why: Publish actions should confirm account, input, and draft-only intent before writing.
  Options: `Fix / Merge / Delete / Keep and Skip`

Reply format:

```text
I01 -> Merge
I02 -> Fix
I03 -> Keep and Skip
```
