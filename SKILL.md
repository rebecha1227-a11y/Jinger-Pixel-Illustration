---
name: jinger-pixel-illustration
description: Create and reuse a confirmed high-definition retro-pixel personal IP character from a person, pet, mascot, meme, anime, brand, or existing illustration. Generate 16:9 article illustration sets or 3:4 editorial knowledge-card series with source-grounded visual planning, consistent identity, exact text controls, and visual QA. Use when the user asks for a personal IP, pixel illustration, character package, character sheet, article visuals, long-form illustrations, knowledge cards, Xiaohongshu cards, 16:9 or 3:4 visual explainers, or wants an idea turned into a recurring character illustration.
---

# Jinger Pixel Illustration

Follow one path for every job:

```text
lock character -> read source -> assign each image one job -> choose visual grammar
-> generate -> compare with identity/style/content contracts -> repair -> deliver
```

The identity belongs to the user's current character. The HD retro-pixel visual language belongs to this Skill. Do not use the bundled example character as a default user identity.

## 1. Route the request

Ask only for information that is genuinely missing. If the user already named the output, start that route directly.

- `character`: create or import a reusable character package.
- `article`: make a 16:9 set with one cover and source-grounded body images.
- `card`: make a 3:4 knowledge-card page or series.
- `both`: run the requested routes separately; never assume both.

If the output type is unclear, ask the user to choose `article`, `card`, or `both`. If no character is confirmed, pause image production and use `references/character-workflow.md`.

Read only the references required by the route:

| Need | Read |
|---|---|
| Create/import/confirm a character | `character-workflow.md`, `character-spec.md` |
| Turn source material into image jobs | `visual-planning.md` |
| 16:9 long-form images | `article-workflow.md`, `style-contracts.md`, `prompt-contracts.md`, `qa-repair.md` |
| 3:4 knowledge cards | `card-workflow.md`, `card-design-contract.md`, `style-contracts.md`, `prompt-contracts.md`, `qa-repair.md` |
| Tool limits, storage, or Markdown insertion | `runtime-delivery.md` |

## 2. Enforce identity state

Resolve the current character with `scripts/character_registry.py`. Only a `confirmed` character may enter an article or card route.

Use the full confirmed package:

1. `character-reference-clean.png`: full-body proportion, silhouette, outfit.
2. `character-bust.png`: face, hair, expression, head accessories.
3. `character-sheet.png`, when present: views, accessory details, palette.
4. `character-spec.md`: fixed traits, allowed variation, forbidden changes, watermark.

Apply this precedence when sources disagree: the user's latest explicit instruction, then the confirmed character package, then the accepted series master image, then the selected style-lock, then layout references. Style-lock and layout references may never replace the user's identity.

Do not generate a final image from a draft package. Do not paste the whole character spec into a prompt; extract a short identity lock from its fixed traits and signature silhouette.

## 3. Plan before generating

Read the source before selecting scenes or pages. Create one `visual_plan` per image using `references/visual-planning.md`.

Every plan must state:

- source anchor and communication job;
- visual grammar and composition;
- exact text, if any;
- essential props and the difference from other images;
- whether the character is required, optional, or absent;
- the action/binding that makes the character informative rather than decorative.

Do not split an article mechanically by paragraph. Do not invent facts, labels, tips, dates, charts, or source modules. When decisive source content is missing, ask before generating.

## 4. Generate by route

### 16:9 article route

Read `article-workflow.md`. Produce one warm scene cover plus as many body images as the article's distinct visual beats require. Use a mini scene for one idea and an explainer grammar for process, checklist, comparison, or structure. Keep non-cover body images visually continuous.

### 3:4 card route

Read `card-workflow.md` and `card-design-contract.md`. Extract information modules first, then group them into pages with one communication job each. Use a cover only for a multi-card series. Use a CTA only when the source or user asks for an action. Permit one focused deep-dive card; do not pad a short source to reach a fixed count. Never shrink text to fit a character.

Use `none`, `bust`, `fullbody`, or `multi-mini` only after the information grid and character bindings are decided. A character is optional on a self-explanatory table, flow, comparison, or file tree.

### Prompt assembly

Use `prompt-contracts.md`. Assemble prompts in this order:

```text
OUTPUT -> IDENTITY -> STYLE -> SOURCE IDEA/PAGE JOB -> STRUCTURE
-> CHARACTER/ACTION -> PROPS -> COMPOSITION -> EXACT TEXT
-> SERIES CONTINUITY -> NEGATIVE CONSTRAINTS
```

Use the relevant style-lock as a style reference only. For cards, prefer edit-from-package or a bottom-first, character-second workflow when identity drift is likely.

## 5. Inspect, repair, and deliver

Open every generated image. Apply `qa-repair.md` in this order:

1. identity and fixed traits;
2. source meaning and exact information;
3. pixel construction and selected style contract;
4. layout, readability, and character footprint;
5. watermark and file delivery.

Repair only the failing page or element and retain accepted pages as continuity references. Do not mark a page PASS after deleting content or identity constraints. If repeated attempts still fail, change the generation strategy and report the unresolved constraint instead of silently lowering the standard.

Save final assets under `.jinger-pixel-assets/`: articles in `illustrations/<slug>/`, cards in `cards/<slug>/images/`. Add the current character's watermark after generation; do not ask the image model to draw it. Do not modify the user's Markdown unless the user explicitly requests insertion, and back it up first.

When image generation is unavailable, read `runtime-delivery.md` and deliver a complete character/visual plan, prompt package, reference paths, and save plan without pretending that PNGs exist.
