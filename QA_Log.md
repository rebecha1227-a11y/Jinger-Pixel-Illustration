# QA Log

## 2026-08-10（补充）

### 问题
Jinger 像素图能不能继续当画风锁和示范？要不要学 EverettFish 加可选三视图？生图 prompt 能不能继续用英文？

### 答案核心
- Jinger 像素图可同时当 style-lock + 公开示范（不是真人照片，也不提供「试用 Jinger」）。
- Mina 只先放文字示例；示范图以后用本 skill 创建角色 prompt 从普通平面角色生成。
- 创建像素 IP 之后加**可选**三视图/设定板；确认不依赖它。必须资产仍是干净全身 + 半身 + spec。
- 生图 prompt 用英文给模型没问题；给静儿/Agent 看的说明继续中文。

### 相关引用
- `references/ip-builder.md`、`references/prompt-templates.md`、`scripts/character_registry.py`（`attach-sheet`）

## 2026-08-10

### 问题
ChatGPT 重新设计了四个 md（character-spec / concept-visual-language / prompt-templates / qa-checklist），并建议公开仓库用 Core + Private Profile 分层（Jinger IP 本地私有、公开只留虚构 Example Character）。这些优化改动是否值得采纳？

### 答案核心
- **架构方向值得采纳**：公开 Skill 核心 vs 用户本地角色资产分层；公开仓库不要把真人/真实 IP 写成 Character Bible。
- **四个文件不能整包照贴**：英文过长、会冲掉已锁定的封面/正文背景分工、水印规则、中文优先、卡片上限等产品决策。
- **最该新增的是「概念→画面」方法**，不是再写一本更厚的角色设定书。
- **Style-lock 图不能先删**：没有替代密度参考时，去掉 Jinger 像素图会让别人创建角色时画风锁不住。
- **落地原则**：收「原则 + 短模块」，不收「百科全书式英文模板」。

### 相关引用
- `SKILL.md`、`references/character-spec.md`、`references/prompt-templates.md`、`references/qa-checklist.md`、`references/style-dna.md`、`LICENSE-ASSETS`、`.gitignore`（已忽略 `.jinger-pixel-assets/`）
