---
name: prd
description: Create or update Chinese enterprise PRDs from OpenDesign prototypes, existing PRD samples, and user decisions. Use when the user asks for PRD生成、PRD更新、根据交互稿写需求、补充字段说明，or wants future PRDs to follow an established document style.
---

# PRD

Write implementation-oriented Chinese PRDs that preserve the user's established document style and decisions.

## Source Priority

Use sources in this order:

1. the user's latest explicit decision;
2. the latest manually edited PRD;
3. the latest OpenDesign artifact and visible interaction states;
4. earlier PRD samples and approved adjacent documents;
5. clearly labeled inference.

Never overwrite a newer manual edit merely because the prototype or an earlier draft differs. When updating an existing PRD, read the complete relevant section first and preserve unaffected content.

## Required Working Method

1. Read the current PRD and identify its actual headings, table structure, numbering, terminology, units, and level of detail.
2. Read the relevant OpenDesign files and inspect every page, module, list, drawer, dialog, empty state, view mode, and responsive state that affects the requirement.
3. Build a focused change list: added, changed, removed, and unchanged content.
4. Update only the affected rows or sections. Keep approved user-authored wording unless it conflicts with a newer explicit decision.
5. Put unresolved business rules in `待确认项`; do not silently invent data sources, formulas, permissions, or lifecycle behavior.
6. Before reporting completion, verify row order, field coverage, formulas, screenshots, and save state.

## Default Document Shape

When the existing sample uses the same format, write `2. 需求分析` as a two-column table:

- `原型`: one page, module, dialog, flow, or major state per row. Keep the module title and add the corresponding cropped OpenDesign screenshot below it.
- `需求分析`: describe observable fields, actions, rules, calculations, states, permissions, feedback, and exceptions for that row.

Use one row per coherent module. Do not create rows for purely internal implementation details. For a non-screen process such as approval, use an available flow diagram or confirmed process artifact; do not fabricate a UI screenshot.

Use the current document's hierarchical numbering. The preferred enterprise-document pattern is `1.` → `a.` → `i.`. Keep items concise enough to scan, but complete enough for design, development, and testing.

## Writing Fields and Rules

Read [references/writing-style.md](references/writing-style.md) whenever the PRD contains forms, lists, calculations, states, permissions, attachments, associations, or screenshots. Follow its field contract and module ordering.

For each field, cover only the dimensions that matter, but do not omit a known constraint:

`字段名：必填性，组件/展示方式；数据来源或枚举；默认值与可编辑性；格式、范围、精度和单位；联动与异常规则。`

Keep field description, calculation rule, and action behavior separate. A field list says what data is shown or entered; later numbered items explain how it changes, aggregates, links, validates, and recovers.

## Update Discipline

- Treat the current PRD as the style authority, not a generic software PRD template.
- Do not introduce `REQ-001`, user-story tables, evidence levels, or GO/HOLD sections unless the user asks for that format.
- Do not remove user-added fields, options, statuses, or wording because they are absent from an older prototype.
- If OpenDesign changed, update the corresponding row, dependent formulas, downstream linkage, risks, and `待确认项`; do not rewrite unrelated rows.
- If a field disappears from the prototype, verify whether the PRD or a user decision intentionally retains it before removing it.
- Use exact business terms consistently across labels, formulas, actions, and status rules.

## Prototype Images

- Add one relevant image to every populated `原型` cell when the user requests screenshots.
- Prefer a readable crop of the exact page section over a full-page image.
- Use a list screenshot for list rules, a module crop for field rules, and a dialog/drawer/flow screenshot for its behavior.
- Reuse a screenshot only when several rows genuinely describe the same visible surface.
- Preserve existing text in the cell and place the image below the title.
- Verify the image finished uploading and the remote document is saved.

## Final Quality Gate

Confirm that:

- every visible field has an explanation or a deliberate exclusion;
- field descriptions include known requiredness, type, source/options, editability, format, and linkage;
- actions include trigger, result, feedback, and failure or cancellation behavior when relevant;
- totals, formulas, thresholds, units, and rounding are explicit and internally consistent;
- list empty states, pagination, states, and permissions are covered when applicable;
- cross-module changes identify downstream recalculation or status impact;
- unknowns are consolidated in `待确认项` rather than disguised as facts;
- screenshots match their rows and existing manual edits remain intact.

