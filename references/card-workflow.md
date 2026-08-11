# 知识卡片工作流

前提：当前角色 `confirmed`。

这是 Skill 里的 **第二套出图系统**（3:4 知识卡），与 16:9 长文配图并列，**不是**独立 Skill。

## 总蓝图（采纳的流水线）

```text
USER ARTICLE / 主题
      ↓
CONTENT ANALYZER          ← card-content-analysis.md（必须从原文抽）
      ↓
识别文章类型 → 核心观点 → 3–5 知识模块 → 视觉隐喻 → 角色动作
      ↓
LAYOUT ENGINE             ← card-layout-system.md
      ↓
STYLE SYSTEM              ← card-style-system.md
      ↓
CHARACTER SYSTEM          ← card-character-system.md（角色包底图 / edit）
      ↓
IMAGE-2 / 生图模型（直连优先）  ← 视觉素材（一期含短句；二期可少字）
      ↓
TEXT RENDERER（二期可选） ← 程序叠中文；一期默认不做
      ↓
FINAL 3:4 + 后盖水印 + QA
```

### 一期 vs 二期

| | 一期（默认，立刻执行） | 二期（用户明确要求或字稳不住时） |
|---|---|---|
| 文字 | Mode A：短句由 image-2 画进图 | Mode B：image-2 少字/无正文 → TEXT RENDERER 叠中文 |
| 角色 | 角色包全量参照；优先 **edit 改姿态**，禁止从零空想重画一个人 | 同左 |
| 通道 | **能调生图模型的 Agent** 上运行；直连优先（如 Codex→GPT-Image-2）；完整内容层 + 身份锁必须保留；**禁止**为躲超时砍掉原文模块/发型锁 | 可分步：底板 → 贴角色；或换其他直连模型 |

气质锁：`assets/style-lock/knowledge-card-editorial-3x4.png`  
（不要用长文 `warm-pixel-scene-16x9.png` 当知识卡主锁。）

## 必读顺序（按需）

1. `card-content-analysis.md`  
2. `card-layout-system.md`  
3. `card-style-system.md`  
4. `card-character-system.md`  
5. `card-templates.md`（多卡 shot list 页型）  
6. `prompt-templates.md`「知识卡片」固定层 + 内容层  
7. 当前角色 `character-spec.md` + 角色包图  
8. `qa-checklist.md`  

## 数量与形态

- 默认 **6–8** 张多卡，最多 9；封面必有；末页默认 CTA。  
- 也可 **1 张总览深讲**（模块 4–7）。  
- 信息密度对齐气质锁样例与合格成品：标题 + 模块说明 + 短解释 + 讲解者；**禁止**「三行字 + 一个大人」。

## 执行步骤

### 1）CONTENT ANALYZER（生图前必须）

读用户文章 / 主题（有 `article.md` 就读全文）。  
按 `card-content-analysis.md` 产出：类型、核心观点、模块、隐喻、角色动作、**EXACT LABELS（逐字来自原文，禁止空想）**。

多卡：写成 shot list（每张对应文章哪一节/哪几个要点）。  
单卡：一份完整 visual plan。  
**用户确认前不批量生图。**

### 2）LAYOUT + STYLE

按内容类型选版式（`card-layout-system.md`）。  
风格固定层不动（`card-style-system.md`）：米白纯色底、RPG UI、像素 QC。

### 3）CHARACTER

加载 confirmed 角色包。  
决定全身或半身：**看文字互动与排版占位**（见 `card-character-system.md`），不默认某一种。  
生图优先：**以角色包图为底/强参考做 edit**（改姿势、道具、朝向），不要纯文案从零发明一张脸。

### 4）IMAGE-2

组装：固定层 Prompt + 本张【CARD CONTENT】（原文模块必须在）。  
参考图：`clean` + `bust` +（若有）`sheet` + 气质锁（只锁版式，不锁样例身份）。  
可分步：①信息图底板（弱角色/框）→ ②用 bust/clean edit 贴上讲解动作。

**通道规则：** 本流程只能在**能够调用生图/编辑模型**的 Agent 上完整执行（如 GPT-Image-2、Nano Banana 2、Imagen 4、Seedream 5.0 Lite、Qwen-Image-3.0 等，以实际可调为准）。有直连时优先直连：例如 Codex 优先内置 GPT-Image-2。Cursor 需通过 MCP 等桥接挂上生图工具（详见 `SKILL.md`「生图能力要求」）。若一次编辑失败，改为单目标编辑或分步生成，但不能删掉原文模块、身份包或发型锁。

**迭代规则：** 每张图生成后必须打开并做视觉 QA。文字、信息密度、角色比例、角色与文字的动作关系、发型任一项不通过，就只修改该项并继续生成；直到通过 `qa-checklist.md` 才能覆盖正式文件名。

### 5）TEXT RENDERER（二期）

仅当用户要求程序排字，或 Mode A 中文稳不住时开启。  
本 Skill 一期不捆绑排字脚本；开启时 image-2 少画正文，坐标叠字后再出水印。

### 6）水印 + QA

后盖当前角色 watermark。  
先做「角色包对照审核」，再过其余必查。

保存：`.jinger-pixel-assets/cards/<slug>/shotlist.md` + `images/`。内置 image-2 的默认生成目录只作为中间产物，最终文件必须复制到项目 `images/`。

## Shot list 必填（多卡）

- 页型；对应原文段落/小节  
- CONTENT TYPE + LAYOUT CHOICE  
- HERO / 标题  
- MODULES + EXACT LABELS（来自原文，可含 1 句短解释，不只三个碎词）  
- CHARACTER CROP：`none` / `bust` / `fullbody` / `multi-mini` + 选择理由（互动/占位/职能测试）  
- LAYOUT MOLD：`cover-hook` / `qa-metaphor` / `wrong-right-tips` / `two-panel` / `steps-flow` / `cta`  
- CHARACTER ACTION  
- IDENTITY METHOD：`edit-from-package`（默认）或说明为何例外  

## 硬规则

- 先分析原文，再出图；禁止靠模型想象力填知识  
- 编辑式像素信息图；几乎纯色底；字与模块是主角  
- 角色是讲解者；占位服从排版；全身/半身按需  
- 身份来自角色包；优先 edit；出图后对照审核  
- 固定 Style，可变 Layout  
- 水印后盖  
- 禁止 Vox 拼贴、深色 Game Boy 整屏、PPT、复杂房间剧场  
- 禁止「降质求通」交付  
