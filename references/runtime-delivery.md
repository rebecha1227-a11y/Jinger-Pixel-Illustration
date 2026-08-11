# Runtime and Delivery

## Image capability

Use a callable image-generation or image-editing tool when one is available in the current Agent. Do not claim that a PNG exists until it has been generated, saved, and opened for inspection. If no image tool is available, deliver the complete prompt package, identity references, visual plans, and save plan instead.

Keep identity and content constraints intact when a tool times out. Switch to a direct route, one-image edit, or bottom-first then character edit workflow. Do not delete identity locks or source modules just to make a request shorter.

## Output locations

Use a runtime root named `.jinger-pixel-assets/`:

```text
.jinger-pixel-assets/
├── characters/<slug>/
├── illustrations/<article-slug>/
│   ├── 00-cover.png
│   └── 01-<topic>.png
└── cards/<slug>/
    ├── shotlist.md
    └── images/01-<page>.png
```

Use lowercase English kebab-case for slugs and filenames. Keep Chinese display names in the shot list or manifest.

## Watermark and Markdown

Read the watermark from the current character's `character-spec.md`. Add it after generation in the bottom-right corner; never ask the image model to draw it. Do not add platform watermarks or the phrase `豆包AI生成`.

Do not edit the user's Markdown by default. If the user explicitly requests insertion, make a backup first, insert only the final verified paths, and report the backup path.

## Local privacy

Keep private reference images and character packages under the local runtime root. Do not upload them to a public repository or place them in bundled examples without permission.

## Author-only bootstrap

Only the repository author may run:

```bash
python3 scripts/bootstrap_jinger.py --i-am-the-author --root <runtime-root>
```

This registers the bundled Jinger package as a confirmed author example. It is not a public trial character.
