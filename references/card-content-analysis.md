# 知识卡 · 内容分析（文章 → 视觉结构）

在调生图之前**必须先做这一步**。不要「文章直接丢给 image-2」，更不要靠模型想象力补知识。

本文件只服务 **3:4 知识卡片**；长文走 `article-workflow.md`。

## 流程位置

```text
USER ARTICLE
  → CONTENT ANALYZER（本文件）
  → LAYOUT ENGINE
  → STYLE SYSTEM
  → CHARACTER SYSTEM
  → IMAGE-2
  →（二期）TEXT RENDERER
  → FINAL
```

## 输入

优先顺序：

1. 用户指定的正文 / `article.md` / 粘贴的文章  
2. 用户口述的要点列表  
3. 仅有主题时：先向用户确认 3–5 条要讲的点，再分析——**禁止静默编造知识点**

## 分析步骤（Agent 内部）

1. 识别 **CONTENT TYPE**（concept / comparison / process / framework / …）  
2. 提取 **CORE QUESTION** 与 **HERO / TAKEAWAY**（尽量用原文原句或原文紧缩，不擅自改术语）  
3. 提取 **3–5 个知识模块**（多卡系列则分配到各张，每张通常 1–3 个模块 + 必要短解释）  
4. 确定模块关系：stack / compare / flow / hub / metaphor  
5. 确定 **VISUAL METAPHOR**  
6. 确定 **LAYOUT MOLD** 与 **DENSITY BAND**，并写明 **LOOK / FRAME / SURFACE / TYPE / PANEL CONTRACT**
7. 确定 **CHARACTER ACTION**、**CHARACTER CROP**、**CHARACTER SLOT**、**CHARACTER FOOTPRINT** 与 **CHARACTER BINDINGS**（`none` / bust / fullbody / multi-mini + 理由，含职能测试）
8. 写出 **EXACT LABELS**：要进画面的字，**逐字可追溯到原文**；需要解释句时从原文压缩，禁止同义乱改术语

## 输出格式

```text
SOURCE: （文章路径或「用户粘贴 / 口述要点」）
CONTENT TYPE: …
CORE QUESTION: …
HERO / TAKEAWAY: …
MODULES:
  - 01 …（来源：第×节 / 原句摘录）
  - 02 …
RELATIONSHIPS: …
VISUAL METAPHOR: …
CHARACTER ROLE: 视觉讲解者
CHARACTER ACTION: …
CHARACTER CROP: none | bust | fullbody | multi-mini
CROP REASON: （互动 / 占位 / 职能测试一句话）
CHARACTER SLOT: none | edge-narrow-column | module-cell | takeaway-band | …
CHARACTER FOOTPRINT: none | fullbody narrow 5%–8% | bust 4%–7% | multi-mini total <=18%
CHARACTER BINDINGS: 手/道具/视线分别绑定哪个文字模块
LOOK LOCK: bundled | first-approved | approved-card paths
FRAME CONTRACT: continuous rounded pixel frame; espresso outer + brown inner + warm highlight
SURFACE CONTRACT: flat warm ivory paper; minimal texture
TYPE CONTRACT: pixel display title + bold module labels + readable Chinese sans body
PANEL CONTRACT: solid primary containers + dashed secondary annotations; consistent corners/lines
DENSITY BAND: low | medium | high（并说明纵向 band）
LAYOUT MOLD: cover-hook | definition-dashboard | architecture-tree | qa-metaphor | wrong-right-tips | two-panel | steps-flow | cta
LAYOUT CHOICE: …
EXACT LABELS: …
  - …
IDENTITY METHOD: edit-from-package（默认）
```

多卡时：上面可以有一份「总纲」，再为每张卡写缩略版；shot list 的 EXACT LABELS 必须能对上总纲。

## 信息密度

对齐合格样例（气质锁 / 用户点名 OK 的卡）：

- 不止大标题：要有模块标题 + 必要的一句说明或结构关系  
- 禁止「只有三行钩子 + 巨大角色」  
- 也禁止把整段文章贴进图里；短句、可扫读  

## 硬规则

- 知识来自原文；没有来源就停下来问，不要编  
- 术语保留：`SKILL.md`、Cursor、Claude、Codex、API、GitHub 等  
- 一张卡一个主问题；系列用 shot list 拆  
- 2–3 秒内可读：标题 → 角色在演示什么 → 主图示 → 结论  

## 写入 Prompt 的自检句

```text
Before generating, use ONLY the provided SOURCE modules and EXACT LABELS.
Do not invent extra tips, pros/cons lists, or facts not in the source.
Transform the source into visual information architecture.
```
