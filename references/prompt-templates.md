# 生图 Prompt 组装

给模型的 prompt 用英文（模型更稳）。方括号换成这一张的具体内容。

不要把整份 character-spec 粘进 prompt。按模块拼，每张单独生成。

始终带上当前角色的干净全身参考图。  
当前角色不是画风锁示范身份时，额外传入 `assets/character/` 半身+全身作 **style-lock only**，并写明不要复制画风锁图里那个人的脸、帽、衣服。

水印**不要写进生图 prompt**。每张成品右下角后盖，文案来自当前角色 spec。

## 组装顺序

1. 画幅与背景模式  
2. Character lock（短）  
3. Pixel style lock（短）  
4. 这一张的 visual plan（主张 / 比喻 / 动作 / 物件 / 场景）  
5. 构图  
6. 图内文字限制  
7. 禁止项  

## 生图前的 visual plan（Agent 内部，中文即可）

```text
visual_plan:
  topic:
  core_message:
  visual_metaphor:
  character_action:
  supporting_objects:   # 1–3
  environment:          # 封面暖色场景 / 正文白底 / 卡片暖色场景
  composition:
  text_labels:          # 能不加就不加
```

从 `concept-visual-language.md` 的流水线来。计划写完再拼 prompt。

## Character lock

```text
CHARACTER IDENTITY LOCK
Use the provided confirmed character reference as the primary identity.
The subject may be a person, pet, mascot, anime character, brand IP, or meme character.
Preserve: attitude/expression, signature silhouette, colors, markings, proportions, and outfit/accessories if present.
The character may change pose, gesture, activity, and environment.
Do not redesign the character. Do not replace them with a generic anime person or unrelated animal.
Do not copy another reference character's identity. Do not change signature features until unrecognizable.
```

## Pixel style lock

```text
PIXEL STYLE LOCK
High-definition detailed pixel art. Fine pixel clusters, not chunky 8-bit.
Controlled outlines, clustered pixel shading, subtle dithering, selective highlights.
Warm handmade retro indie-game illustration, readable silhouettes, consistent pixel density.
Avoid: chunky 8-bit, low-detail pixel, 3D, plastic toy, photorealism, vector, flat corporate, generic anime, neon HUD, PPT infographic.
```

## 从参考素材 / 现成形象创建角色

先出**干净主锚点**（必做；默认全身，表情包头身 IP 可以是完整头身），再出半身/头身（必做）。三视图是可选，见下一节。

主锚点：

```text
Create a high-definition retro pixel-art character, single subject, portrait-friendly, plain white or transparent background.
[PIXEL STYLE LOCK]
Style-lock references: match pixel density and coloring only. Do NOT copy the style-lock reference character's face, hat, or outfit.
Subject type: [human / pet / mascot / anime / brand / meme]
Identity lock from the user's reference only: [attitude/expression], [signature silhouette], [colors/markings], [body/outfit/accessories visible in the reference]
Capture the memorable vibe and signature features. Do not invent body parts, clothes, or markings that are not in the reference unless the user explicitly asked to complete a full-body design.
No title, no border, no turnaround labels, no color palette, no extra unrelated props, no watermark, no photo background.
This will be the clean identity reference for later illustrations.
```

半身 / 头身：

```text
Same HD pixel character as the clean identity reference. Bust / head-and-shoulders (or head-and-chest for pets/mascots), plain white or transparent background. Lock the face/expression and signature head features. No text, no watermark.
```

## 可选：角色三视图 / 设定板

用户确认或点头「要三视图」之后才生成。不是确认角色的前提。

```text
Create a portrait-orientation HD pixel-art character turnaround / model sheet.
[PIXEL STYLE LOCK]
Same identity as the clean full-body reference. Do not redesign.
Layout on a light sheet: one main full-body plus front / left / back / right views.
Short direction labels only (FRONT / SIDE / BACK). Optional tiny vibe keywords if provided: [vibe].
Keep identity consistent across all views. No extra people, no watermark, no photo background, no dense paragraphs.
```

## 长文封面 16:9（暖色简单像素场景）

```text
16:9 HD pixel article cover.
[CHARACTER LOCK]
[PIXEL STYLE LOCK]
Warm simple pixel scene: cream paper / light wood desk / cork board, optional dark-brown pixel frame.
Style reference: the warm scene lock image for mood and desk only — do not copy its dense term-cards or long Chinese paragraphs.

ARTICLE TOPIC: [topic]
CORE MESSAGE: [core message]
VISUAL METAPHOR: [metaphor]
CHARACTER ACTION: [action — not a sticker]
SUPPORTING OBJECTS: [1–3]
TEXT: short title and 2–6 character labels max. No paragraphs. No watermark in the image.
No photoreal background, no neon HUD, no PPT.
```

## 长文正文 16:9（白底迷你剧场）

流程拆解：

```text
16:9 HD pixel article illustration.
[CHARACTER LOCK]
[PIXEL STYLE LOCK]
Pure white background with only a tiny pixel ground or contact shadow. Mini theater, generous margin, subject about 50–65%.

PROCESS: [step1] → [step2] → [step3] (max 5)
Same locked character may appear as clones, left to right, each doing a different step.
One idea only. 1–3 props per node. In-image labels at most 2–6 characters, on objects.
No big title, no paragraph text, no watermark, no full room, no PPT flowchart.
The image should remain understandable if text is removed.
```

核心动作：

```text
16:9 HD pixel article illustration.
[CHARACTER LOCK]
[PIXEL STYLE LOCK]
Pure white background with only a tiny pixel ground or contact shadow.

One locked character + one core object + one action + one visible result.
CORE IDEA: [one idea]
VISUAL METAPHOR: [metaphor]
CHARACTER ACTION: [action]
If the character were removed, the picture would not make sense.
Almost no in-image text. No watermark. No photoreal scene.
```

## 知识卡片 3:4（整张一次画完）

```text
3:4 HD pixel knowledge card. One complete illustration, not a typeset poster, not HTML layout, not a character sticker on blank paper.
[CHARACTER LOCK]
[PIXEL STYLE LOCK]
Warm simple pixel scene: cream paper / light wood desk / cork board, optional dark-brown pixel frame. Match the warm scene style-lock mood, but less crowded.

PAGE TYPE: [cover / pain / concept / steps / compare / pitfall / cta]
ONE IDEA: [one idea]
VISUAL METAPHOR: [metaphor]
CHARACTER ACTION: [action inside the scene]
PROPS: [1–3]

In-image text only, short and exact:
[EN short title if any]
[ZH labels, each 2–8 characters, at most 6–8 labels]

Readable Chinese, no paragraphs, no tiny essay, no watermark, no PPT, no magazine collage.
```

## 多图一致性

同一篇文章 / 同一套卡片：

Keep the same confirmed character reference for every image.
Keep signature features, silhouette, colors/markings, pixel density, outline treatment, and palette logic consistent.
Only change pose, expression, action, environment, and article-specific objects.
Every image should feel like another scene from the same pixel-art universe.

## 修图

轮廓/画风偏了：

```text
Redraw in HD pixel art matching the identity reference. Keep the same pose and idea. Do not switch to 8-bit, doodle, or 3D toy. Do not change hair, outfit, or face.
```

误画成画风锁示范角色（当前角色不是该示范时）：

```text
Keep HD pixel density but replace the character with the identity reference. Do not copy the style-lock reference character's face, hat, or outfit.
```
