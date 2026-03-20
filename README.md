# Skill Optimizer

`skill-optimizer` 是一个用于治理和审计其他 skills 的 skill。它会结合当前对话和本地可见的 skill 目录，识别诸如触发遗漏、metadata 偏弱、重复 skills、失效引用、流程风险等问题，并输出一份详细报告和后续优化策略。

## 它适合解决什么问题

- 审计当前 workspace 里有哪些 skills
- 找出重复、重叠或边界不清的 skills
- 找出 metadata 偏弱、容易漏触发的 skills
- 找出缺少 `agents/openai.yaml`、引用失效、结构陈旧等问题
- 找出风险较高但缺少 guardrails 的 skills
- 先分析，再决定怎么改，避免直接误删或误改

## 快速开始

### 1. 先运行一次审计

你可以直接这样对 agent 说：

```text
Use $skill-optimizer to audit my current workspace skills and give me a report plus follow-up optimization strategies.
```

### 2. 阅读输出报告

通常会包含几部分：

- 执行摘要
- 按问题类型分类的 findings
- action queue
- 后续优化建议

### 3. 再决定要不要实施修改

这个 skill 默认会先做分析，不会在审计阶段直接改文件。  
如果你后续想继续执行修复，再根据报告中的建议逐项选择即可。

## 你会得到什么

典型输出包括：

- 哪些 skill 本来应该触发但没有触发
- 哪些 skill 的 metadata 太弱
- 哪些 skill 是重复副本或高度重叠
- 哪些 skill 的说明、引用或配套文件已经陈旧
- 哪些 skill 存在安全边界不清的问题
- 当前 skill 安装、同步、维护流程有哪些可以优化的地方

## 常见使用场景

- `请帮我审计当前仓库里的 skills，并给我一份详细报告。`
- `看看我这里有没有重复的 skills、弱 metadata 或危险的 skills。`
- `基于当前对话和本地 skills，给我一份后续优化策略。`

## 工作方式

这个 skill 的核心原则是：

- 先审计，后修改
- 先给证据，再给建议
- 把分析和执行分开
- 不轻易把“未使用”直接等同于“应该删除”

## 示例输出

可以参考：

- [examples/sample-report.md](./examples/sample-report.md)

## 目录结构

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

## 给维护者的说明

### 构建发布包

在当前目录执行：

```bash
python3 scripts/build_release.py
```

构建后会生成：

- `dist/clawhub/skill-optimizer-v<version>-clawhub.zip`
- `dist/claude/skill-optimizer-v<version>-claude.zip`

其中：

- ClawHub 包保留 `SKILL.md`
- Claude 包会使用 `Skill.md`

## 备注

- 这个发布包默认避免写入机器相关的绝对路径
- `evals/evals.json` 里包含了基础测试 prompts，便于后续回归测试
