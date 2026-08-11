# Prompt Contracts

Write prompts in English when the active image model handles English more reliably. Keep the source plan and exact Chinese text in the prompt. Replace every bracketed field with the current job.

## Reference handling

Pass the current confirmed clean anchor, bust, optional sheet, and short identity lock as identity references. Pass only the selected style-lock as a style reference. State explicitly that the style reference supplies pixel density or layout mood only and must not supply its sample character's identity.

Do not pass a draft character, a rejected output, or an unrelated sample as an identity reference. Do not ask the model to draw a watermark.

## Assembly order

```text
OUTPUT
IDENTITY
STYLE
SOURCE IDEA / PAGE JOB
STRUCTURE
CHARACTER / ACTION / BINDINGS
PROPS
COMPOSITION
EXACT TEXT
SERIES CONTINUITY
NEGATIVE CONSTRAINTS
```

## Shared identity lock

```text
IDENTITY: Use the provided confirmed character package as the authoritative identity.
Preserve the fixed face, expression, hair or head shape, signature silhouette,
colors or markings, proportions, outfit, and identifying accessories. Change only
the approved pose, gaze, activity, crop, and scene props. Do not redesign or
substitute a generic character. Do not copy the identity of any style reference.
```

## 16:9 article cover

```text
OUTPUT: Create one 16:9 HD retro-pixel article cover.
IDENTITY: [shared identity lock]
STYLE: [shared pixel contract] + warm simple pixel scene; use the cover style-lock
for mood and scene simplicity only.
SOURCE IDEA: [article topic and one core message]
STRUCTURE: one clear visual metaphor, one character action, one to three relevant props.
COMPOSITION: readable subject and title area, warm simple background, no dense room.
EXACT TEXT: [short title and labels, copied exactly, or none]
NEGATIVE: no paragraphs, invented labels, unrelated props, photorealism, 3D,
chunky 8-bit, neon HUD, PPT poster, or watermark.
```

## 16:9 article body

```text
OUTPUT: Create one 16:9 HD retro-pixel article body illustration.
IDENTITY: [shared identity lock]
STYLE: [shared pixel contract] + the approved article-body series master.
PAGE JOB: [one sentence]
GRAMMAR: [scene / process / comparison / timeline / evidence / checklist]
STRUCTURE: [one action and visible result, or numbered/matched information nodes]
CHARACTER: [required/optional/none, crop, action, module binding]
PROPS: [one to three essential objects]
COMPOSITION: [reading direction, whitespace, label placement]
EXACT TEXT: [exact short labels, or none]
NEGATIVE: no generic pointing pose, unrelated decoration, paragraphs, tiny text,
identity drift, style-lock sample identity, or watermark.
```

## 3:4 knowledge card

```text
OUTPUT: Create one 3:4 editorial knowledge card.
IDENTITY: [shared identity lock]; prefer editing the supplied package image.
STYLE: [shared pixel contract] + the card design contract + approved card look-lock.
PAGE JOB: [one communication job]
LAYOUT: [layout mold and top-to-bottom reading order]
MODULES: [source-grounded information blocks]
CHARACTER: [none/bust/fullbody/multi-mini, reserved slot, footprint, action, bindings]
EXACT TEXT: Render only this exact text, with no extra words: [manifest]
SERIES CONTINUITY: [frame, paper, typography, panel, palette, and pixel rules]
NEGATIVE: no invented facts, labels, tips, chart values, paragraphs, unreadable text,
large decorative mascot, room scene, HTML collage, PPT SmartArt, or watermark.
```

## Character creation

```text
OUTPUT: Create a clean HD retro-pixel character anchor on a plain light background.
IDENTITY: [visible, user-confirmed traits only]
STYLE: use the character pixel references for clusters, density, and shading only.
POSE: front-facing full-body or complete head/body anchor, relaxed and readable.
COMPOSITION: generous margin; no border, labels, palette, unrelated props, or watermark.
PRESERVE: [fixed traits and signature silhouette].
DO NOT INVENT: [unknown traits].
```
