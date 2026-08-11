# Jinger Pixel Illustration Architecture

## Objective

让任何 Agent 都能沿着同一条路径完成：

```text
锁角色 → 读内容 → 定每张图的任务 → 选择视觉语法 → 生成 → 对照返修 → 正确交付
```

## Design decisions

- 用户当前的 confirmed 角色包是唯一身份来源。
- 画风锁只负责像素密度、边框、纸面、UI 气质和构图语言。
- 用户本次明确要求优先于默认规则；当前角色包优先于风格示例；通过的系列样张优先于后续自由发挥。
- 长文按视觉节拍拆图，不按段落机械配图。
- 知识卡先提取信息模块，再决定页数和版式；允许单卡深讲，不固定凑 6–8 张。
- 一张图只承担一个 communication job。
- 角色只有在对文字模块、道具、箭头或结论有明确绑定时才出场。
- 图中文字来自 source-grounded exact text；水印由后处理叠加。

## Runtime references

| 任务 | 权威文件 |
|---|---|
| 主路由 | `SKILL.md` |
| 角色创建和确认 | `references/character-workflow.md` + `character-spec.md` |
| 文章到视觉任务 | `references/visual-planning.md` |
| 16:9 长文 | `references/article-workflow.md` |
| 3:4 知识卡 | `references/card-workflow.md` + `card-design-contract.md` |
| 画风和参考图职责 | `references/style-contracts.md` |
| Prompt 字段 | `references/prompt-contracts.md` |
| QA 和返修 | `references/qa-repair.md` |
| 工具与交付 | `references/runtime-delivery.md` |

## Verification

Run these checks before publishing a revision:

```bash
python3 /Users/rebecha/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
python3 scripts/character_registry.py doctor --root <runtime-root>
npm pack --dry-run
```

Use `scripts/validate_visual_plan.py` for a machine-readable plan and `scripts/validate_delivery.py` for final PNG dimensions. Forward-test at least: new character, confirmed article, single card, multi-card series, character-free information card, style-reference identity separation, and no-image-tool fallback.

## Packaging boundary

The installed Skill needs `SKILL.md`, `agents/`, `assets/`, `examples/`, `references/`, and runtime scripts. README, PLAN, QA logs, screenshots, HTML placeholders, duplicate style-reference folders, caches, and local runtime assets are repository or development material, not Agent runtime instructions.
