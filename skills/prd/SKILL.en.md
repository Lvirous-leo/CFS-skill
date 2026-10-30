---
name: prd
description: Create, update, or review Chinese enterprise PRDs from OpenDesign prototypes, maintained documents, and user decisions. Use for PRD authoring, updates, requirement reviews, interaction-to-requirement mapping, field specifications, and business-boundary or acceptance-gap reviews. Preserve established document styles. Excludes standalone market research and code review.
---

# PRD Requirements Documents

Write implementation-oriented Chinese enterprise PRDs matching the user's business decomposition, document structure, language, wording, and detail. Reuse their expression for matching logic and expand actual differences; extra length, completeness, or generic templates cannot replace fidelity.

The [Chinese entrypoint](SKILL.md) and [Chinese writing-style reference](references/writing-style.md) are the defaults. This English edition and its [English writing-style reference](references/writing-style.en.md) contain the same rules for English reading. They do not change the requested deliverable language or create a second skill. Update corresponding editions together; reading both languages for one task is unnecessary.

## Choose the Working Scope

Infer the mode from the request and available context; do not ask the user to choose routinely.

- **Incremental update:** For a field addition, wording correction, or prototype change, inspect the affected section and its actual dependencies. Do not restart discovery, review unrelated pages, or require new goals and alternatives.
- **Full PRD:** For a new feature, establish the known problem, users, objective, scope, constraints, and assumptions. Reuse supplied decisions; put this content into the existing document structure.
- **Business review:** For questions about duplication, module boundaries, or design quality, analyze before recommending changes. A review request alone does not authorize rewriting a live PRD.

Read [references/business-review.md](references/business-review.md) for new functionality, cross-module rule changes, or substantive business review. Read [references/acceptance-review.md](references/acceptance-review.md) for full PRDs, reviews, or updates affecting behavior, calculations, associations, states, or permissions. Plain wording edits need neither reference.

Before expanding flows and exceptions, distinguish additions, existing capabilities to reuse, and explicit exclusions for this release. Adjacent chapters provide reuse evidence, not automatic inheritance of bank connectivity, approvals, or later-stage processing. Industry capabilities do not automatically enter scope. Inspect actual dependencies without turning closure checks into a build list.

Continue work supported by the evidence. Ask only for missing decisions that materially affect correctness; keep dependent rules unresolved while progressing on independent sections.

## Align with a User Sample Before Writing

For authoring, rewriting, or substantive updates, read the [user logic and expression profile](references/author-profile.en.md) and select the current document or a comparable user chapter. Plain typo fixes can follow the current sentence directly.

Establish the sample, decomposition order, headings/columns, row size, numbering, terminology/sentences, density, and shared-rule references before drafting. Keep this working comparison out of the PRD by default. Prefer the current structure; otherwise choose the task-appropriate full-module, monthly-improvement, or interface-rule shape. Do not convert three columns to two, flatten nested items into essays, or expand a local change into a full plan.

When asked to write like the user, check business logic, structure, language/wording, and density together. Preserve known controls and boundaries and keep unknowns pending; copying old rules, contradictions, or incomplete conditions is not fidelity.

## Source Priority

Use sources in this order:

1. the user's latest explicit decision;
2. the latest manually edited PRD;
3. the latest OpenDesign artifact and visible interaction states;
4. earlier PRD samples and approved adjacent documents;
5. clearly labeled inference.

Never overwrite a newer manual edit merely because the prototype or an earlier draft differs. When updating an existing PRD, read the complete relevant section first and preserve unaffected content.

Apply precedence to the particular rule, not the entire document. A manual edit in one paragraph does not make every paragraph newer than the prototype. A visible control establishes appearance, not unshown business behavior.

When reconciling sources:

- Apply new, nonconflicting prototype content within the requested update scope.
- Preserve an explicit user decision unless the user supersedes it. If a prototype conflicts, identify the exact rule and surface involved.
- If authority or recency is unclear, record both versions and their impact in Pending Items; do not silently choose one.
- Before deleting a field or module, inspect intentional retention and dependent references, formulas, states, screenshots, and pending items. An inaccessible source is not evidence of deletion.

## Required Working Method

1. Read the current PRD and closest user sample. Identify actual decomposition, headings, tables, numbering, terms, units, and detail using the expression profile. Check strikethrough, version/deferred notes, and discussion options before merging any historical rules.
2. Read available relevant OpenDesign files and visible states to the depth required by the mode. Inspect affected modules and dependencies; disclose unavailable evidence without inventing screens or blocking independent document work.
3. Build a focused change list: added, changed, removed, and unchanged content.
4. Update only the affected rows or sections. Keep approved user-authored wording unless it conflicts with a newer explicit decision.
5. Put unresolved business rules in Pending Items; name the affected object, missing decision, downstream impact, and which work can proceed. Do not silently invent data sources, formulas, permissions, or lifecycle behavior.
6. Check critical rules through relevant acceptance scenarios. Correct contradictions supported by established decisions; keep unsupported outcomes unresolved. Fold clarified rules into their owning rows rather than adding a test document by default.
7. Before reporting completion, verify affected row order, field coverage, formulas, screenshots when involved, and save state. Distinguish document inspection, visual verification, and executed software tests; report only checks actually performed.

## Document Shape

Preserve actual headings and columns, including three-column Prototype/Function/Detailed Analysis or single-column Requirements Analysis formats. Do not normalize them. Without a current document, choose a comparable shape from the expression profile. Only use the following two-column Requirements Analysis form when the selected sample uses it:

- the Prototype column: one page, module, dialog, flow, or major state per row. Keep the module title and add the corresponding cropped OpenDesign screenshot below it.
- the Requirements Analysis column: describe observable fields, actions, rules, calculations, states, permissions, feedback, and exceptions for that row.

Use one row per coherent module. Do not create rows for purely internal implementation details. For a non-screen process such as approval, use an available flow diagram or confirmed process artifact; do not fabricate a UI screenshot.

Preserve the current hierarchy, whether `1.` → `a.` → `i.` or nested numeric lists; use the former only as a fallback. Keep items concise enough to scan and complete enough for design, development, and testing.

## Writing Fields and Rules

Read [English writing-style reference](references/writing-style.en.md) whenever the PRD contains forms, lists, calculations, states, permissions, attachments, associations, or screenshots, or when matching a user-authored sample. Apply its maintained-document style profile before its fallback field and module ordering. When logic and functionality are substantially the same as the supplied user-authored PRD, reuse its sentence patterns, hierarchy, terminology, and level of detail; describe only the actual differences rather than expanding it into explanatory prose. Preserve required business controls and record unresolved rules separately.

For each field, cover only the dimensions that matter, but do not omit a known constraint:

`Field: requiredness, component/display; source/options; default and editability; format, range, precision, and unit; linkage and exception rules.`

Keep field description, calculation rule, and action behavior separate. A field list says what data is shown or entered; later numbered items explain how it changes, aggregates, links, validates, and recovers.

## Update Discipline

- Treat the current PRD as the style authority, not a generic software PRD template.
- Do not introduce `REQ-001`, user-story tables, evidence levels, or GO/HOLD sections unless the user asks for that format.
- Do not remove user-added fields, options, statuses, or wording because they are absent from an older prototype.
- If OpenDesign changed, update the corresponding row, dependent formulas, downstream linkage, risks, and Pending Items; do not rewrite unrelated rows.
- If a field disappears from the prototype, verify whether the PRD or a user decision intentionally retains it before removing it.
- Use exact business terms consistently across labels, formulas, actions, and status rules.

## Prototype Images

- For any screenshot task, read and follow the prototype screenshot procedure in [English writing-style reference](references/writing-style.en.md).
- Before capture, map each populated prototype row as `PRD row → OpenDesign page → functional region → interaction state → screenshot count`. The image must support the observable content described in that row.
- Add one relevant image to every populated Prototype cell when the user requests screenshots.
- Capture the exact functional region and state. Do not use a full browser viewport when it leaves the relevant content small, preserves unrelated navigation or chrome, or creates large blank areas.
- Use a list/query crop for list rules, a module crop for field rules, and a dedicated dialog, drawer, comparison, risk-panel, or flow crop for its behavior. Split a long module into multiple readable images when one image would make its text too small.
- Reuse a screenshot only when several rows genuinely describe the same visible surface and interaction state.
- Preserve existing text in the cell and place the image below the title.
- After insertion, inspect the remote document at its normal reading scale. Relevant fields, buttons, states, and key values must be readable without opening the image separately.
- Verify content match, functional crop, readability, placement, upload completion, and saved state for each affected row. Upload completion and a saved document alone do not prove that a prototype image is correctly delivered.

## Final Quality Gate

Apply this to the affected scope without turning a small edit into a full-document audit. First check user logic/expression fidelity, then correctness/completeness. Repair either failure; one cannot compensate for the other. Confirm that:

- the selected user sample is matched in decomposition, headings/columns, row size, numbering, field order, sentences, terminology, and density; reused behavior states actual differences and unnecessary explanation is removed;
- actual impacts on queries, filtering, sorting, imports/exports, approval, interfaces, and historical data are checked only for relevant changes; supported changes enter their owning entries, while unknowns are not invented as defaults;
- discussion options, strikethrough, deferred items, and carried-forward history are distinguished without reviving canceled rules or treating document status as implementation evidence;
- every visible field has an explanation or a deliberate exclusion;
- field descriptions include known requiredness, type, source/options, editability, format, and linkage;
- actions include trigger, result, feedback, and failure or cancellation behavior when relevant;
- totals, formulas, thresholds, units, and rounding are explicit and internally consistent;
- list empty states, pagination, states, and permissions are covered when applicable;
- cross-module changes identify downstream recalculation or status impact;
- substantive changes have clear business-object ownership and no unexplained duplicate maintenance;
- critical rules have observable acceptance outcomes, or the missing outcome is explicitly pending;
- review findings separate evidenced contradictions, missing decisions, and optional improvements, with concrete locations and consequences;
- unknowns are consolidated in Pending Items rather than disguised as facts, limited to decisions needed for in-scope delivery rather than questions created by out-of-scope ideas;
- screenshots match their rows, use readable functional crops, remain legible at the remote document's normal reading scale, and existing manual edits remain intact;
- screenshot completion is not reported from image-node existence, upload success, or saved state alone; failed content, crop, readability, or placement checks are recaptured and reverified.
