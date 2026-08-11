# Character Workflow

## Goal

Create a reusable, confirmed identity package before making article or card images. The package may represent a human, pet, mascot, meme, anime character, brand IP, or existing illustration.

## Choose an input route

### A. Import an existing character

Use this route when the user already has a pixel character, illustration, model sheet, or approved package. Preserve its visible identity and fill only missing package assets.

### B. Create from reference material

Use this route for a photo, pet image, meme, logo, character illustration, or a written description. Extract only visible or user-confirmed traits:

- face, eyes, skin/fur color, and signature expression;
- hair, ears, headwear, markings, and silhouette;
- body proportion, clothing, shoes, accessories, and signature colors;
- traits that must never change;
- traits that may vary with a scene;
- unclear or conflicting traits that need a user decision.

Ignore captions, QR codes, backgrounds, unrelated props, and guessed age, job, ethnicity, or other sensitive attributes. When references conflict, follow the latest explicit user instruction; otherwise preserve the clearest repeated trait and record the uncertainty in the spec.

## Build the identity set

Generate or collect, in this order:

1. A clean front-facing full-body anchor, or a complete head/body anchor for an IP that has no human body.
2. A face-and-shoulders or head-and-chest bust anchor.
3. An optional turnaround sheet after the user asks for it.
4. A `character-spec.md` using the local template.

Keep clothing, colors, accessories, proportions, and signature expression consistent. Do not put labels, borders, palettes, watermarks, or a reference-sheet layout into clean anchor images.

## Confirmation gate

Store a new package as `draft`. Show the clean anchor and bust and ask the user to confirm. Do not create article or card deliverables until the user says `确认`, `定稿`, `就用这个`, or an equivalent explicit approval. A turnaround sheet is optional and is not required for confirmation.

## Package state

- `draft`: may be inspected or revised; cannot be used for final illustration.
- `confirmed`: may be used for article and card generation.

Use `scripts/character_registry.py` from the Skill root:

```bash
python3 scripts/character_registry.py register \
  --root <runtime-root> --slug <slug> --name "角色名" \
  --clean-reference <clean.png> --bust <bust.png> \
  --spec <character-spec.md> [--sheet <sheet.png>]

python3 scripts/character_registry.py confirm --root <runtime-root> --slug <slug>
python3 scripts/character_registry.py activate --root <runtime-root> --slug <slug>
python3 scripts/character_registry.py resolve --root <runtime-root>
```

`resolve` must return absolute paths for the clean reference, bust, optional sheet, and spec. If the registry is unavailable, preserve the same folder structure and keep the status gate manually.

## Reference precedence during generation

Use the complete package, not one image alone:

- bust decides face, hair, expression, and head accessories;
- clean anchor decides full-body proportion, silhouette, and outfit;
- sheet decides views and accessory details when available;
- spec decides fixed traits, allowed variation, forbidden changes, and watermark.

The style-lock controls pixel construction and layout mood only. It never supplies the user's face, hair, clothing, or identity.
