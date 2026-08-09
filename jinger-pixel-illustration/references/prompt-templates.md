# 生图提示词骨架

把方括号换成具体内容。每张单独生成。始终带上当前角色的干净全身参考图。

非 Jinger 角色时，额外传入 Jinger 半身+全身作 **style-lock only**，并写明不要复制 Jinger 的脸和衣服。

## 从照片 / 现成 IP 创建角色

```text
Create a high-definition pixel-art character turnaround sheet, portrait orientation.
Style lock: detailed indie-game HD pixel art (fine pixels, light volume, not chunky 8-bit, not doodle, not 3D vinyl toy, not photorealistic). Match the pixel density and coloring of the style-lock reference images only. Do NOT copy the style-lock character's face, hat, or outfit.

Identity lock from the user's photo/IP reference only:
[face, hair, skin, body, outfit, shoes, signature accessories]

Output: one main full-body pose plus front / left / back / right views on a light sheet. Keep identity consistent across all views. No extra people, no watermark, no photo background.
```

干净全身：

```text
Same HD pixel character as the sheet. Single full-body figure, plain white or transparent background, no title, no border, no turnaround labels, no color palette, no extra props. Identity unchanged. This will be the clean identity reference for later illustrations.
```

半身：

```text
Same HD pixel character, bust/head-and-shoulders, plain white or transparent background. Lock the face and head accessories. No text.
```

## 长文封面 16:9（暖色简单像素场景）

```text
16:9 HD pixel illustration, warm simple pixel scene (cream paper / light wood desk / cork board, optional dark-brown pixel frame). Style reference: the warm scene lock image for mood and desk only — do not copy its dense term-cards or long Chinese paragraphs.

Character (identity reference): [locked outfit and face]. The character must perform a clear action related to the article hook, not stand as a sticker.

Scene: [1–3 desk props]. One core idea: [封面钩子].
Little or no in-image text (2–6 character labels max). No watermark. No photoreal background, no neon HUD, no PPT.
```

## 长文正文 16:9（白底迷你剧场）

流程拆解：

```text
16:9 HD pixel article illustration. Pure white background with only a tiny pixel ground or contact shadow. Mini theater, generous margin, subject about 50–65%.

Same locked character may appear as 3–5 clones, left to right, each doing a different step of: [流程].
One idea only. 1–3 props per node. In-image labels at most 2–6 characters, on objects. No big title, no paragraph text, no watermark, no full room, no PPT flowchart look.
```

核心动作：

```text
16:9 HD pixel article illustration. Pure white background with only a tiny pixel ground or contact shadow.

One locked character + one core object + one action + one visible result.
Core idea: [观点].
If the character were removed, the picture would not make sense.
Almost no in-image text. No watermark. No photoreal scene.
```

## 知识卡片 3:4（整张一次画完）

```text
3:4 HD pixel knowledge card, a complete illustration (not a typeset poster, not HTML layout, not a character sticker on blank paper).
Warm simple pixel scene: cream paper / light wood desk / cork board, optional dark-brown pixel frame. Match the mood of the warm scene style-lock, but keep this card less crowded.

Locked character lives inside the scene and performs: [具体动作].
Page type: [cover/pain/concept/steps/compare/pitfall/cta].
One idea: [这一页只讲什么].
Props: [1–3 物件].

In-image text only, short and exact:
[EN short title if any]
[ZH labels, each 2–8 characters, at most 6–8 labels]

Readable Chinese, no paragraphs, no tiny essay, no watermark, no PPT, no magazine collage.
```

## 修图

轮廓/画风偏了：

```text
Redraw in HD pixel art matching the identity reference. Keep the same pose and idea. Do not switch to 8-bit, doodle, or 3D toy. Do not change hair, outfit, or face.
```

误画成 Jinger（当前角色不是 Jinger 时）：

```text
Keep HD pixel density but replace the character with the identity reference. Do not use the style-lock girl's face, eee hat, or outfit.
```
