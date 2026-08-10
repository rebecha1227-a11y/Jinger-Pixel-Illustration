# 生图 Prompt 组装

给模型的 prompt 用英文（模型更稳）。方括号换成这一张的具体内容。

不要把整份 character-spec 粘进 prompt。按模块拼，每张单独生成。

## 参考图怎么传（身份 vs 画风）

**身份（当前 confirmed 角色包，能带尽带）：**

1. `character-reference-clean.png` — 全身比例与整套服装  
2. `character-bust.png` — 脸/发型/头配件近景（必须）  
3. `character-sheet.png` — 若有：三视图、配饰特写、配色（必须带）  
4. 另从 `character-spec.md` 提炼短 Character Lock 句子  

禁止只传一张全身。冲突时：clean/bust/sheet/spec 互相印证；画风锁永远让路给身份。

**画风/气质（按成品选，勿盖身份）：**

- 长文封面 → `assets/style-lock/warm-pixel-scene-16x9.png`  
- 长文正文 → `assets/style-lock/article-body-editorial-16x9.png`  
- 知识卡 → `assets/style-lock/knowledge-card-editorial-3x4.png`  
- 创建角色时的像素密度 → `assets/character/` 半身+全身（style-lock only）  

当前角色不是画风锁示范身份时，写明：不要复制画风锁图里那个人的脸、帽、衣服。

水印**不要写进生图 prompt**。每张成品右下角后盖，文案来自当前角色 spec。

## 组装顺序

1. 画幅与背景模式  
2. Character lock（短）  
3. Pixel style lock（短）  
4. 这一张的 visual plan（插哪段 / 只讲什么 / 精确文案 / 构图）  
5. 构图  
6. 图内文字限制  
7. 禁止项  

## 生图前的 visual plan（Agent 内部，中文即可）

想不清就不要调生图。计划写完再拼 prompt。细则见 `concept-visual-language.md`。

```text
visual_plan:
  insert_after:        # 插在文章哪一段后面（封面=文首标题下）
  job:                 # 这一张只让人看懂什么（一句话）
  not_this_image:      # 不要和本套其他图讲同一件事
  visual_metaphor:
  character_budget:    # none / 1 accent / 1 hero
                       # 说明图默认 none 或 1 accent；迷你剧场才用 1 hero
  character_action:    # budget=none 时可空
  supporting_objects:  # 1–3
  environment:         # 封面可独立底色；正文图跟本套统一底/边框
  composition:
  exact_labels:        # 要画的中文，连标点；禁止同义改写
```

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

## 流程说明图 16:9 / 3:4（列步骤、清点、对比）

不要用迷你剧场模板。先读 `explainer-workflow.md`。  
图内中文用 visual plan 的 `exact_labels`，不要同义改写。

```text
[16:9 or 3:4] HD pixel instructional illustration, warm cream paper / light wood / cork board, optional dark-brown pixel frame. Not a blank white mini-theater. Not a PPT SmartArt. Not an HTML poster.
[CHARACTER LOCK]
[PIXEL STYLE LOCK]

PAGE JOB: [one sentence from visual_plan.job]
TITLE (large, readable): [exact title]
LAYOUT: numbered steps top-to-bottom OR left-vs-right with ONE large pixel arrow.

INFORMATION DESIGN FIRST:
- each step = number + complete short Chinese phrase (6–16 characters) + its OWN cell
- 1:1 mapping. Never send three arrows into one collage.
- large nameplates on the matching objects; each phrase once
- if listing alternatives, write spaced slashes: A / B / C
- if using ①②③④, those numbers appear ONCE on the page, not repeated in every row
- any wide/tall preview inside a cell sits fully inside the box with padding

CHARACTER: optional small accent (visual_plan.character_budget).
Prefer large readable labels + icons. Do not put the character in every cell.
If the character appears: not standing still pointing at a board; not identical clones that only change hands.

SHAPE LOCK:
- a wide product must look like a wide landscape frame, never a square headshot or closed book
- a tall card must look tall, with content visible inside
- a user photo / sticker / manuscript must look like photo/sticker/paper, NOT a finished pixel portrait

TEXT: large pixel lettering. 5–12 text blocks max. Write exact_labels exactly. No paragraphs. No tiny unreadable Chinese. No watermark.
```

介绍**本 skill 自己**时，可用下面短句当示例（别的文章不要照抄，按那一篇的 exact_labels 写）：

```text
左右对照示例：
左：真人照 / 宠物 / 表情包 ；文章 / 知识观点 ；Logo / 场景描述
右：固定的像素风个人IP角色 ；16:9长文配图 ；3:4知识分享卡片图

纵向清单示例：
①1张角色锚点
②可选三视图
③16:9长文套图
④3:4知识卡片
⑤换主题还能继续用
```

## 知识卡片 3:4（固定层 + 内容层）

细则见 `card-style-system.md` / `card-layout-system.md` / `card-character-system.md` / `card-content-analysis.md`。  
气质锁：`assets/style-lock/knowledge-card-editorial-3x4.png`（只锁版式气质，身份以当前角色参考为准）。

每次生成：**整段固定层可复用**，只替换【CARD CONTENT】。

```text
Create a premium editorial knowledge card / educational infographic from the personal character reference.
IMAGE FORMAT: Vertical 3:4. High-resolution. Clean FLAT solid warm ivory/cream background (subtle pixel grain OK). One coherent editorial poster, not sticker collage, not HTML magazine, not a busy room scene.

CHARACTER REFERENCE — IDENTITY LOCK
The provided character image is PRIMARY and AUTHORITATIVE.
Same face, hairstyle, proportions, signature outfit/accessories, palette, cute-intelligent-fashion personality.
Do NOT redesign into a generic anime girl. Do NOT change clothing/hair/accessories absent from the reference unless requested.
Same recurring IP mascot across the series.

CHARACTER AS VISUAL EXPLAINER
The character must demonstrate / explain / point / hold / operate / compare / react.
Never only decorate the corner. Never the same forever laptop pose.
Scale: about 1/4–1/3 of the frame if single figure; or multiple smaller explainer figures inside modules. Text/modules dominate. Do NOT let the character fill the poster.

VISUAL STYLE
Premium retro pixel-art editorial illustration — sophisticated modern pixel art, NOT photo, NOT semi-real anime, NOT 3D, NOT 8-bit chunky.
Feel: "editorial infographic from a beautiful retro indie-game / RPG UI."

PIXEL ART QUALITY CONTROL
Construct the character as pixel art from the start. Do NOT paint anime then add a pixel filter.
Visible intentional pixel clusters in hair, eyes, face, clothes, accessories, shadows, highlights, outlines.
Hair = grouped pixel strands. Faces = few careful pixel clusters. Edges = controlled stair-stepping.

COLOR SYSTEM
Warm ivory/cream, light beige, cocoa brown, dark espresso, muted peach, dusty pink, subtle gray.
Anchor on the character's existing colors. Avoid neon.

LAYOUT SYSTEM
Clear editorial hierarchy with intentional negative space and clean margins.
Use 1–5 information modules for this card (series cards: usually 1–2; single deep card: up to 4–7).
Hierarchy: HERO TITLE → short intro → main modules → character interaction → key takeaway box → tiny pixel UI accents only if helpful.
Choose layout by content type (concept / compare / process / framework / tutorial / list / etc.). Do NOT force one template for every topic.
RPG-style UI frames, panels, numbered blocks, arrows, folder icons OK.

TYPOGRAPHY
Large retro pixel type for main title / key English terms / numbers.
Highly readable modern sans for Chinese explanations.
Strong hierarchy. No decorative pixel fonts for long paragraphs. No tiny body text. No overcrowding.

TEXT ACCURACY
Preserve exact terminology (SKILL.md, Cursor, Claude, Codex, AI, API, GitHub, etc.).
No invented facts. All visible text intentional, correctly spelled, legible.
Short sentences only — not article paragraphs pasted onto the canvas.

INFORMATION DESIGN
Viewer understands in 2–3 seconds via: title → character demo → main diagram → takeaway.
Transform content into visual architecture (metaphor, flow, compare, modules). Do NOT typeset the article.

BACKGROUND
Simple solid warm ivory/beige. No photographic rooms, shelves, cork walls, landscapes, busy environments.

FINAL AESTHETIC
Cute + intelligent + fashionable + slightly nerdy + retro + editorial + tech.
Another page from the same personal knowledge universe.

Before drawing, internally analyze: core question, takeaway, content type, modules, metaphor, character action, best layout. Then compose.

【CARD CONTENT】
PAGE TYPE: [cover/pain/concept/steps/compare/pitfall/cta]
CONTENT TYPE: […]
CORE QUESTION: […]
HERO / TITLE: […]
MODULES / EXACT LABELS: […]
CHARACTER ACTION: […]
VISUAL METAPHOR: […]
KEY TAKEAWAY: […]
No watermark in the image.
```

## 多图一致性

同一篇文章 / 同一套卡片：

Keep the same confirmed character reference for every image.
Keep signature features, silhouette, colors/markings, pixel density, outline treatment, and palette logic consistent.
Only change pose, expression, action, environment, and article-specific objects.
Every image should feel like another scene from the same pixel-art universe.

ARTICLE SERIES LOOK:
- Cover may use a different background color/scene from the body images (same is also OK).
- All non-cover illustrations in the SAME article must share one background, one border treatment, and one pixel style.
- After the first body image passes, use it as the look lock for the remaining body images.

## 修图

轮廓/画风偏了：

```text
Redraw in HD pixel art matching the identity reference. Keep the same pose and idea. Do not switch to 8-bit, doodle, or 3D toy. Do not change hair, outfit, or face.
```

误画成画风锁示范角色（当前角色不是该示范时）：

```text
Keep HD pixel density but replace the character with the identity reference. Do not copy the style-lock reference character's face, hat, or outfit.
```
