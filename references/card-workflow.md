# 知识卡片工作流

前提：当前角色 `confirmed`。先读 `style-dna.md`、`card-templates.md`、`concept-visual-language.md`、当前角色 `character-spec.md`。

目标气质对齐 `assets/style-lock/warm-pixel-scene-16x9.png`：角色站在暖色像素场景里，和短文字块一起演戏。  
**不是**小红书那种 HTML 杂志卡。`templates/` 只在没有生图模型时应急，不要当成品标准。

## 数量

默认 6–8 张，**最多不超过 9 张**。封面必有；最后一页默认 `立刻试`。

## 先出 shot list（必须等确认）

每张写清：

- 页型（cover / pain / concept / steps / compare / pitfall / cta）
- 中文标题（封面/强调页可另写短英文像素标题）
- 这一页只讲什么
- 角色在场景里做什么（拿牌、靠着木牌、推开错误一侧、把 CTA 递出来……）
- 这一页的 visual plan：主张 / 比喻 / 动作
- 画面里允许出现的短文字（每条 2–8 字，一张图不超过 6–8 条）
- 1–3 个场景物件

用户确认前不要批量生图。

## 确认后（有生图模型）

1. 每张单独生成一张完整的 3:4 高清像素卡（角色 + 场景 + 短文字一次画完）。
2. 用 `prompt-templates.md` 按模块组装知识卡片 prompt；style-lock 用暖色场景图 + 角色干净参考图。
3. 生成后**只后盖水印**（右下角，当前角色文案）。不要再套 HTML 排版。
4. 中文写错、多字、长段落：重画该张或只修那几处标签，不要改走 HTML 方案。
5. 过 `qa-checklist.md`。
6. 保存到 `.jinger-pixel-assets/cards/<slug>/`：

```text
shotlist.md
images/
```

## 无生图 fallback

只交 shot list + 每张完整 prompt + 参考图路径 + 水印文案。  
只有用户明确说「先用 HTML 看个占位」时，才用 `templates/` 做临时预览，并标明**不是最终画风**。

## 硬规则

- 整张卡是一幅像素插画，不是海报排版
- 角色必须参与画面，不能只贴在空白旁边
- 图内文字要短、少、准；不要说明书正文
- 水印后盖，不让 AI 画
- 不要 Vox 黄黑拼贴，不要深色 Game Boy 整屏，不要 PPT
