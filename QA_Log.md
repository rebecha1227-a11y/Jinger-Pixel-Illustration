# QA Log

## 2026-08-10

### 问题
总原则为什么要分成默认和非默认？具体按什么模式出图应该靠 prompt 和大模型理解啊！

### 答案核心
- 「默认/非默认」是错误框架：那是给 Agent 设开关，不是出图逻辑。
- 对的做法：读懂这一张要让人看懂什么 → 把构图、动作、字写进 prompt → 生图模型照画。模板只是现成写法，不是模式选择器。
- 生图模型不会自己「选模式」；它只画 prompt 里写清的东西。所以关键是 prompt 写具体，不是先分类再套模板。

### 相关引用
- `SKILL.md` 第三步、`explainer-workflow.md` 开篇、`style-dna.md`

## 2026-08-10

### 问题
不一定每次都生成流程图，也可能是介绍某个东西、画一系列动作。为什么别人（如 Fish）能生成排版好看、文字和图片配合刚刚好的图？

### 答案核心
- 流程图/说明图不是默认；动作序列和概念介绍应走迷你剧场，人小、留白、每拍换姿势。
- Fish 好看是因为画风本身就是「白纸+手写+小图标」，字和图是同一种材料；每个字下面紧贴对应图标；角色 mini，留白当版面。
- 高清像素把字当外来物，中文容易糊；不能指望像素图达到钢笔 doodle 那种「手写即排版」。可学：图文成对、角色变小、分色分块、动作序列不要密字。

### 相关引用
- EverettFish「我锁定的画风」「这个 Skill 是干嘛的？」；`style-dna.md` 角色占比；`explainer-workflow.md` 非默认

## 2026-08-10

### 问题
根据多次试跑反馈，当前 skill 里的生图 prompt 要怎么优化，才能达到最佳预期？

### 答案核心
- 像素画风锁和角色身份锁已经够用，不要再加厚；真正失败的是「模式路由 + 构图合同」。
- 模型更听具体几何和反例（一行一格、16:9 必须是扁横图、禁止右侧大号站立人），不听空泛禁止（不要 PPT）。
- visual_plan 要改成 ASCII 构图草图并写进 prompt；说明图 / 迷你剧场 / 知识卡必须分模板，互不污染。
- 禁止项改成「我们真实翻车过的样子」；平台水印（豆包）不要再写进 prompt。

### 相关引用
- 试跑 A/B 说明图、`references/prompt-templates.md`、`references/explainer-workflow.md`

## 2026-08-10

### 问题
试跑后：image-2 流程图内容太少、没箭头；豆包按 skill 出的知识卡/长图文字过少、人呆站。Fish 的 skill 为什么能把「最终你会拿到什么」讲清楚？我们差在哪、还要改哪？

### 答案核心
- Fish 赢在**信息设计**（编号、箭头、完整短句、每步一个小场景），不在 doodle 画风。
- 我们把「说明图」误用成「迷你剧场概念图」：规则禁止箭头/流程图、图内只准 2–6 字 → 模型忠实地画出看不懂的图。
- 应增加第三种模式：流程说明图。迷你剧场仍给文章观点用；怎么用/提供得到必须走说明图。知识卡步骤页改为 6–14 字完整短句+编号，禁止呆站指板子。

### 相关引用
- `references/explainer-workflow.md`、EverettFish「最终你会拿到什么」说明图

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
