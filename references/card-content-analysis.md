# 知识卡 · 内容分析（文章 → 视觉结构）

在调生图之前**必须先做这一步**。不要「文章直接丢给 image-2」。

本文件只服务 **3:4 知识卡片**这一套出图系统；长文配图走 `article-workflow.md`。

## 流程位置

```text
用户主题 / 文章
  → CONTENT ANALYSIS（本文件）
  → LAYOUT 选型（card-layout-system.md）
  → 拼固定层 Prompt + 内容层（prompt-templates.md）
  → 生图
  → 后盖水印
```

## 输出格式（每张卡或整套总纲都要写）

```text
CONTENT TYPE: concept | comparison | process | framework | tutorial | list | timeline | cause-effect | architecture | abstract
CORE QUESTION: （读者打开图要被回答的一句话）
HERO / TAKEAWAY: （最重要的一句，可进结论框）
MODULES: （3–5 个；多卡系列则每张只保留 1–2 个）
  - 01 …
  - 02 …
RELATIONSHIPS: stack | compare | flow | hub | metaphor
VISUAL METAPHOR: （文件夹 / 箭头 / 双栏 / 清单 UI …）
CHARACTER ROLE: 视觉讲解者（不是旁观装饰）
CHARACTER ACTION: （拿着什么、指着什么、操作什么；每张不同）
LAYOUT CHOICE: （对照 card-layout-system.md）
EXACT LABELS: （要进画面的中英文字，禁止同义改写）
```

## 硬规则

- 先理解结构，再决定版式；禁止把段落原文贴进画布。
- 一张卡只服务一个主问题；多卡系列用 shot list 拆开。
- 术语保留原文：`SKILL.md`、Cursor、Claude、Codex、API、GitHub 等不得乱改。
- 2–3 秒内应能读出：标题 → 角色在演示什么 → 主图示 → 结论。

## 内部自检（写进生图 prompt 的一小段即可）

```text
Before generating, internally analyze:
- core question, single takeaway, content type
- 3–5 supporting concepts and their relationships
- best visual metaphor and character action
- best infographic layout for THIS content type
Then design visual information architecture.
Do NOT simply typeset the article onto the canvas.
```
