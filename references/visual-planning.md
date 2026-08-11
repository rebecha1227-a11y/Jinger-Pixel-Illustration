# Visual Planning

Plan meaning before calling an image tool. Use one plan per image and keep it short enough to audit.

## Required plan

```yaml
asset_id:
source_anchor: "article section, paragraph, or user-provided point"
communication_job: "one sentence: what this image makes understandable"
visual_grammar: scene | process | comparison | timeline | evidence | data | checklist | conclusion
exact_text: []
visual_metaphor:
character_role: required | optional | none
character_action:
character_bindings: []
essential_props: []
composition:
not_this_image: "what another image in this set already covers"
style_lock:
series_lock:
```

`source_anchor` and `exact_text` must be traceable to the supplied source. If the user provides only a topic, ask for the points to teach before inventing modules.

## Choose visual grammar by meaning

| Source need | Grammar | Core structure |
|---|---|---|
| One idea or emotional beat | `scene` | character + object + action + visible result |
| Ordered actions | `process` | numbered nodes with a clear direction |
| Wrong/right or before/after | `comparison` | matched sides and shared criteria |
| Change over time | `timeline` | chronological rail and outcomes |
| Proof or case | `evidence` | central artifact with anchored callouts |
| Numbers or trend | `data` | one truthful chart plus short interpretation |
| Collection of actions | `checklist` | grouped numbered items and completion cues |
| Summary or next step | `conclusion` | takeaway plus optional action |

Do not use a generic person-pointing-at-a-board scene when the source calls for a process, comparison, or data structure.

## Article beats

Read the thesis, emotional arc, concrete examples, and turning points. Select distinct beats that collectively explain the piece. Map each beat to a source anchor and give it a different action, prop, scale, or emotional tone. Do not split mechanically by paragraph.

## Card modules and page count

Extract the thesis, question, definitions, process, comparison, evidence, framework, checklist, and conclusion as separate modules only when each needs its own explanation. Group related modules into pages with one communication job each.

- A focused idea may be one deep-dive card.
- A multi-card series normally uses 3–5 readable modules per page.
- Add a cover for a multi-card series when it helps the reading path.
- Add a conclusion or CTA only when the source contains one or the user asks for it.
- Add pages when text becomes too small; remove pages when a coherent structure fits together.
- Keep the final series at nine cards or fewer unless the user explicitly requests a different production plan.

## Character decision

Use `none` when the table, flow, comparison, or file tree is already self-explanatory. Otherwise state the character's action and its exact binding to a module, object, arrow, or conclusion. If removing the character leaves the information completely unchanged, prefer `none` or redesign the action.

## Text discipline

Copy titles, names, dates, quantities, units, and labels exactly. Shorten a sentence outside the image only after verifying that its meaning is preserved. Never ask the image model to summarize a paragraph inside the image. Use `A / B / C` for alternatives and do not duplicate a label.
