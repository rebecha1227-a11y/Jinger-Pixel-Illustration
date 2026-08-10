---
name: jinger-pixel-illustration
description: 高清复古像素个人 IP 插图 Skill：可从真人照、宠物、表情包、动漫角色、品牌 IP 或现成形象创建并确认角色，再生成 16:9 长文配图（必含封面+正文）或 3:4 可分享知识卡片（整张由生图模型画出，角色生活在像素场景里）。Use when 用户提到个人 IP、像素配图、角色设定、宠物像素、表情包 IP、品牌吉祥物、长文插图、16:9、知识卡片、3:4、小红书卡片、Jinger，或要把观点画成固定角色插图。
---

# Jinger Pixel Illustration

把一个**已确认的高清像素角色**做成两种成品。不要默认两套一起出。

项目名是 Jinger Pixel Illustration；**用户画的永远是自己的当前角色**，不是示范角色。

## 每次开始

1. 读本文件路由，再按需读 `references/`，不要一次塞完。
2. 用 `scripts/character_registry.py` 解析当前角色（见 `references/character-package.md`）。
3. 按下面顺序决策，缺一步就停下来问。

### 第一步：这次做什么

用户已经说清（「给这篇文章配图」「做知识卡」「两个都要」）就不要再问。

否则先发引导，**必须问到 1 / 2 / 3**：

```text
欢迎使用 Jinger Pixel Illustration。

这个 Skill 可以把一个固定的高清像素角色，做成下面两种图（先选这次要哪一种，不会默认两套都出）：

1. 16:9 长文配图（必含封面 + 正文图；封面暖色场景，正文默认白底迷你剧场）
2. 3:4 知识卡片（奶油米白，人物和文字一起演戏，可直接发）

请先选这次要做的：
1. 只要长文配图
2. 只要知识卡片
3. 两套都要
```

选 3 才两条都跑。只选 1 或 2 就只做那一条。

### 第二步：画谁

有 `confirmed` 当前角色：报角色名，不要重问 A/B。

没有 confirmed 角色：**先不要配图**。在引导里补上：

```text
如果还没有确认过角色，请再选角色从哪来：
A. 我已经有现成形象（像素图、插画、设定板都行，请发图）
B. 我有参考素材，想做成高清像素角色
   （真人照、宠物、表情包、动漫角色、品牌 IP 都可以）

选 B 的话，请先看「参考素材要求」。
```

不要提供「试用示范角色 / 启用内置角色」入口。

然后读 `references/ip-builder.md`，走 A 导入或 B 从参考素材创建。设定模板见 `references/character-spec.md`。  
先出主锚点 + 半身/头身；**三视图是可选项**，确认不依赖它。停在确认门闩，用户没说「确认 / 定稿 / 就用这个」之前不能出成品。

### 第三步：出图

- 长文 → 读 `references/article-workflow.md` + `style-dna.md` + `concept-visual-language.md` + `prompt-templates.md`
- 知识卡片 → 读 `references/card-workflow.md` + `card-templates.md` + `style-dna.md` + `concept-visual-language.md` + `prompt-templates.md`
- 每张先生一个短 visual plan，再拼 prompt；生成后过 `references/qa-checklist.md`

## 硬规则

- 画风：高清像素。不是 8-bit、简笔画、3D 公仔、写实摄影。
- 每个角色确认后锁死自己的记忆点（神态、剪影、标志色/花纹/服装），第一版不换装、不改认不出。
- 长文一套必须有 **1 张封面 + 若干正文图**。封面 = 暖色简单像素场景；正文 = 默认白底迷你剧场。
- 知识卡片默认 6–8 张，最多 9 张；先出 shot list 等人确认。**整张由生图模型画成像素场景**，角色要生活在画面里和短文字互动，不要做成「HTML 排版 + 角色贴图」。
- 卡片和封面里只允许短标签（中文约 2–8 字，英文大标题短词）。不要往图里塞段落。
- 水印文案来自**当前角色** `character-spec`，不要套用示范角色的水印号。水印后盖，不让模型画。
- 无生图能力时诚实说明，只交 prompt 和保存计划。`templates/` 里的 HTML 只是应急预览，**不是目标气质**。
- 默认不改用户 Markdown；只有用户明确说「插入」才写入，并先备份。
- 不猜年龄、职业、民族等敏感属性；不把用户参考素材上传到公开仓库。

## 画风锁

创建或转换新角色时，用捆绑示范像素图**只锁颗粒、密度、上色**，规则见 `references/style-dna.md` 的「画风锁」。

示范图路径在 `assets/character/` 与 `assets/style-lock/`。设定说明在 `examples/jinger/`。虚构填写示例在 `examples/example-character/`。

画风锁不能盖过当前角色的身份。不要把示范角色设成用户的当前角色。

## 无生图时怎么说

> 现在不能直接生成像素图。我会把完整 prompt、参考图路径和水印计划准备好；有生图能力后再按同一套规范出图。HTML 模板只在你明确要求「先看个占位」时才用，不是成品方向。

## 作者本地

若工作区已有 `.jinger-pixel-assets/` 且当前角色已 `confirmed`，直接配图。  
仅作者可运行 `scripts/bootstrap_jinger.py --i-am-the-author`。开源用户不要跑这个脚本。
