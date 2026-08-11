# 16:9 Article Workflow

Prerequisite: the current character is `confirmed`. Read `visual-planning.md`, `style-contracts.md`, `prompt-contracts.md`, and `qa-repair.md` as needed.

## Input and image count

Use the user's article, Markdown file, or supplied outline. Select distinct visual beats from the thesis, emotional arc, examples, and turning points. Do not assign one image per paragraph.

Always include one cover. Choose the body-image count from information density and article length. A short article may need one to three body images; a long article may need more, but never add an image whose job duplicates another. Keep the body set within eight images unless the user explicitly requests more.

## Storyboard

Before generation, write one row per image:

```text
IMAGE: 00-cover / 01-topic
SOURCE ANCHOR: exact section or idea
JOB: one sentence this image makes understandable
GRAMMAR: scene / process / comparison / timeline / evidence / checklist
SCENE: one concrete action or visual metaphor
CHARACTER: role, action, expression, crop
PROPS: one to three essential objects
EXACT TEXT: exact title or labels, or none
NOT THIS IMAGE: responsibility reserved for another image
```

For ordinary ideas, use `scene`: one character, one core object, one action, and one visible result. For ordered actions, lists, comparisons, or structure, use an explainer grammar with readable labels, numbered nodes, arrows, or matched columns. Do not force a character into every node.

## Cover

Use the warm cover style-lock. Create a simple warm pixel setting, a clear topic signal, one useful character action, and no paragraph text. The cover may use a different background from body images.

## Body continuity

Use the article body style-lock for every non-cover image. Once the first body image passes, use it as the body series master. Keep its background, border treatment, pixel density, palette logic, and type roles across the remaining body images. Change the job, scene, action, and relevant props.

## Identity and generation

Pass the current clean anchor, bust, optional sheet, and short spec-derived identity lock. Never use a style-lock sample character as the user's character. Generate each image separately and inspect it immediately.

When a user selects an accepted image as the preferred base, edit that image or its corresponding series master. Do not restart the whole set from zero.

## Text and delivery

Keep labels short and exact. Use almost no text for a mini scene; use complete short phrases for steps and comparisons. Do not render paragraphs, invented labels, or a watermark in the image model. Save to `.jinger-pixel-assets/illustrations/<slug>/` and run `qa-repair.md` before delivery.
