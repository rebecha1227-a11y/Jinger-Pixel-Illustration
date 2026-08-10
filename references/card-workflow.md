# 知识卡片工作流

前提：当前角色 `confirmed`。

这是 Skill 里的 **第二套出图系统**（3:4 知识卡），与 16:9 长文配图并列，**不是**独立 Skill。

## 必读顺序（按需，不要一次塞完）

1. `card-content-analysis.md` — 文章 → 视觉结构  
2. `card-style-system.md` — 固定画风 / 色盘 / 纯色底  
3. `card-layout-system.md` — 按类型选版式  
4. `card-character-system.md` — 身份锁 + 讲解者互动 + 体量  
5. `card-templates.md` — 多卡页型（shot list 用）  
6. `prompt-templates.md` 的「知识卡片」整段 — 固定层 + 内容层  
7. 当前角色 `character-spec.md`  
8. 生图前过 `qa-checklist.md` 知识卡项  

气质锁：`assets/style-lock/knowledge-card-editorial-3x4.png`  
（不要用长文的 `warm-pixel-scene-16x9.png` 当知识卡主锁。）

`templates/` HTML 仅无生图且用户要求占位时用，**不是**目标气质。

## 数量与形态

- 默认 **6–8 张**多卡系列，最多 9；封面必有；末页默认 CTA。  
- 用户明确只要 **1 张总览深讲**时，可出单卡（模块可到 4–7 块）。  
- 两种形态共用同一套 Style / Character / Layout 规则。

## 总流程

```text
主题或文章
  → 内容分析（card-content-analysis）
  → 多卡：写 shot list；单卡：写一份 visual plan
  → 等人确认
  → 每张：LAYOUT 选型 + 组装「固定层 Prompt + 本张 CONTENT」
  → 生图（角色参考 + 可选知识卡 style-lock）
  → 只后盖水印
  → QA
  → 存 .jinger-pixel-assets/cards/<slug>/
```

### Shot list（多卡，必须等确认）

每张写清：

- 页型（cover / pain / concept / steps / compare / pitfall / cta）  
- CONTENT TYPE + LAYOUT CHOICE  
- 中文标题 / HERO  
- 这一页只讲什么  
- CHARACTER ACTION（讲解动作，勿重复同一 pose）  
- EXACT LABELS（连标点，禁止同义改写）  
- 1–3 个像素图标/物件（不是复杂房间道具）  

确认前不要批量生图。

### 确认后生图

1. Prompt = **固定层**（style + character rules + layout rules + pixel QC）+ **内容层**（本张 ARTICLE / MODULES / LABELS）。  
2. 参考图：当前角色 **clean + bust +（若有）sheet** 一并传入，并读 spec；可选附上 `knowledge-card-editorial-3x4.png` **只锁版式气质**（勿把样例角色身份盖过当前角色）。  
3. 背景：几乎纯色暖米白。人小、字与模块大。  
4. 水印后盖，文案来自当前角色 spec。  
5. **强制审核**：`qa-checklist.md` 先做「角色包对照审核」，再做其余必查。中文错漏：重画或局部修字，不要改走 HTML 成品方案。  

## 文字模式（现实预期）

- **Mode A（默认）**：图内短句由生图模型画出。适合概念卡、对比卡、步骤短句。要求可读、术语准确。  
- **Mode B（可选，未默认开启）**：生图少字/无正文，再程序叠中文。仅当用户明确要求「程序排字」或长文密集到模型稳不住时再走；本 Skill 暂不捆绑排字脚本。

## 硬规则

- 整张是**编辑式像素信息图**，不是复杂房间剧场，也不是 HTML 杂志贴图  
- 先内容分析，再出图  
- 角色是讲解者，体量约 1/4～1/3（或小分身进模块）  
- 固定 Style，可变 Layout  
- 水印后盖  
- 不要 Vox 黄黑拼贴、不要深色 Game Boy 整屏、不要 PPT SmartArt  
