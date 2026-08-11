# 3:4 Knowledge-Card Workflow

Use this route for an educational card, article summary, process card, comparison, framework, timeline, or data story. Read `visual-planning.md`, `card-design-contract.md`, `style-contracts.md`, `prompt-contracts.md`, and `qa-repair.md` as needed.

## Pipeline

```text
source -> content modules -> page jobs -> layout mold -> design contract
-> character slot -> prompt -> one-page generation -> visual QA -> delivery
```

Read the source before designing. If only a topic is available, ask for the knowledge points. Never invent a list of tips, pros/cons, dates, facts, or chart values.

## Page planning

For each page, record:

```text
PAGE: number / slug
SOURCE SECTION:
PAGE JOB: one communication task
TITLE / SUBTITLE: exact text
MODULES: 1–5 source-grounded blocks, each with a short explanation when needed
LAYOUT MOLD: cover-hook / definition-dashboard / architecture-tree / qa-metaphor
              wrong-right-tips / two-panel / steps-flow / cta
READING ORDER:
EXACT LABELS:
CHARACTER CROP: none / bust / fullbody / multi-mini
CHARACTER SLOT / FOOTPRINT:
CHARACTER BINDINGS:
```

Use one cover only for a multi-card series. Use a CTA only when the source or user asks for an action. A short source may become one deep-dive card. For a series, group related modules into pages of roughly 3–5 readable modules, add pages when text becomes cramped, and keep the final set at nine cards or fewer unless explicitly overridden.

For multi-card work, show the shot list before generating when the user has asked for a plan or when page boundaries are uncertain. If the user clearly asks to execute directly and the source is complete, proceed after the internal plan.

## Select the layout

Choose a mold by content, then adapt it:

| Content | Mold |
|---|---|
| cover or hook | `cover-hook` |
| definition or framework | `definition-dashboard` |
| hierarchy or file structure | `architecture-tree` |
| concept or misconception | `qa-metaphor` |
| wrong/right comparison | `wrong-right-tips` |
| conflict or story introduction | `two-panel` |
| ordered steps | `steps-flow` |
| source-grounded action | `cta` |

Build the title, vertical bands, text grid, and module slots before placing the character. The layout must remain clear if the character is removed.

## Character role

Use `none` when the information structure is self-explanatory. When present, make the character inspect, connect, compare, operate, carry, point to, or complete one concrete module. Declare its crop, reserved slot, footprint, and binding before generation. Prefer edit-from-package; if identity is unstable, generate the card base first and edit the package character into its reserved slot.

## Generate and deliver

Generate one page at a time. After the first page passes, use it as the series look lock. Keep the same frame, paper surface, type roles, panel line language, pixel density, and accent family. Preserve exact text and truthful relationships. Save the shot list and images under `.jinger-pixel-assets/cards/<slug>/`, then run the shared and card-specific checks in `qa-repair.md`.
