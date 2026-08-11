# Card Design Contract

This file defines the fixed visual and layout contract for 3:4 cards. The source plan supplies the changing content.

## Information hierarchy

Use this order unless the chosen mold requires a justified variation:

```text
hero title -> short intro/question -> main modules -> character interaction
-> key takeaway or action
```

Use a 3%–5% safe margin. Divide the canvas into vertical bands before composing. Keep module spacing larger than the line spacing inside a module. Do not shrink text to accommodate a character.

## Layout molds

| Mold | Structure |
|---|---|
| `cover-hook` | title + short hook + theme object or expressive bust |
| `definition-dashboard` | definition + three to five concept modules + conclusion |
| `architecture-tree` | root node + branches + paired short explanations |
| `qa-metaphor` | question/answer + central metaphor object + takeaway |
| `wrong-right-tips` | matched wrong/right columns + source-grounded takeaway |
| `two-panel` | conflict or pain point + transition to the subject |
| `steps-flow` | numbered steps, one cell per step, clear direction |
| `cta` | source-grounded action sentence + completion cue |

Do not use a fixed mold for every article. Do not turn a page into a collection of identical floating cards.

## Visual surface

Use a nearly solid warm ivory surface, one continuous rounded pixel frame, dark cocoa structure, and one muted accent family. Use a retro pixel display face for the hero title or keyword, bold clear module labels, and readable Chinese sans-serif body text. Use solid primary containers and dashed secondary annotations consistently.

Avoid complex rooms, shelves, landscapes, HTML magazine collage, PPT SmartArt, neon HUD, deep full-screen Game Boy treatment, broad gradients, and decorative objects without a source relationship.

## Character slot

Declare one of `none`, `bust`, `fullbody`, or `multi-mini`.

- `none`: tables, flows, comparisons, and trees that already explain themselves.
- `bust`: text-heavy cards where expression, gesture, or a held object explains a module.
- `fullbody`: a meaningful stance, walk, comparison, or action slot with enough width reserved.
- `multi-mini`: several steps or modules where each small figure has a distinct binding.

Judge painted footprint and text clearance, not height alone. Keep a fullbody figure narrow in a reserved column, a bust inside a module or takeaway band, and the total multi-mini footprint subordinate to the information. If removing the character changes nothing, use `none` or redesign the action.

## Text contract

Use only source-grounded titles, labels, names, quantities, dates, units, and short explanations from the page plan. Never ask the model to write a paragraph or invent a tip. Exact text must be copied into the prompt. Split the page if exact text becomes unreadable.

## Series contract

The first approved page establishes the frame thickness, paper, typography roles, panel line language, pixel density, and accent treatment. Reuse that page as a look-lock for later pages. Change the layout mold and content only when the page job requires it.
