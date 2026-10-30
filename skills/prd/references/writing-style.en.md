# PRD Writing Style Reference

Use this reference for concise, field- and action-oriented Chinese enterprise PRDs. The [Chinese edition](writing-style.md) is the default. Both editions contain the same rules; this edition is for English reading and does not change the requested deliverable language. Update both editions together rather than maintaining separate policies.

## 0. Match the User's Maintained Document Before Applying Defaults

Basis: on 2026-10-16, the user explicitly requested that similar logic follow their wording and description style. The sample is the user-authored reverse-factoring chapter, Chapter 5 of the factoring improvement document. Apply this profile to similar enterprise PRD tasks for this user. New samples and explicit instructions take precedence. Learn the expression, not universal business rules; do not propagate unfinished entries or contradictions from the sample.

On 2026-10-30, the user further specified that generated PRDs must match their logic, language, structure, and wording, and accepted 34 budget-folder files as samples. Full text was obtained for 32; two were unavailable. Apply the [logic and expression profile](author-profile.en.md) for structure selection, decomposition, sentence patterns, and source anchors when writing or rewriting. Screenshot-only content does not establish field rules.

### Expression and Detail

- Read the complete relevant module and the closest user-authored chapter. Identify row boundaries, field order, numbering, sentence patterns, and information density. For matching logic, reuse the sentence structure and replace only business objects that actually differ; do not reorganize it into a different document style.
- Preserve existing column labels, such as Prototype / Requirements Analysis. Use one row per page, drawer, dialog, or related modification module. Retain the sample's hierarchy, including `1.` → `a.` → `i.` or nested numeric numbering, and its three-column, two-column, or item-based structure. Keep fields under their owning modules, such as Basic Information; do not flatten nested entries into long paragraphs.
- State functions and actions directly: "The list includes...", "Filter...", "Click... to open/enter...", "If..., then...", and "When..., notify... to update...". Each item describes one action or a tightly related group of rules. Use the next numbering level when elaboration is necessary.
- Use compact field descriptions, such as "Institution type: defaults to Bank; editable; required." Preserve exact source field names, business terms, defaults, and explicit restrictions such as disabled and non-editable. Treat the field contract as a completeness checklist, not a mandatory word order or a demand to expand every dimension for every field.
- For identical behavior, write "Same as..." or "Reuse...". For differences, write "Based on..., add/remove..." or "Only rename... to... (not editable)." References must identify a specific function or module, and differences must be explicit. Do not write "same as existing logic" when important behavior differs or the source is unknown.
- Use parentheses and brief notes for short additions. Preserve established P0/P1 priorities without assigning new ones. Do not copy mentions of people, empty numbering, typos, or unfinished content.

### Separate Analysis from Requirements

- Analyze the business thoroughly, but keep the PRD focused on actionable fields, actions, conditions, results, and linkage. Do not fill requirement cells with reasoning history, conceptual essays, design justifications, repeated declarations, generic risk checklists, or delivery-status commentary.
- Write necessary amount, permission, exception, and completion rules at the sample's level of detail in their owning entries. State shared rules once; describe differences or reference them elsewhere. Brevity must not omit known critical conditions, and apparent completeness must not expand pages or workflows unnecessarily.
- Consolidate unknown rules under Pending Items, briefly naming the missing decision and its impact. Do not add unrelated future issues or repeat the same uncertainty in every row. When the source contradicts itself, identify locations and consequences rather than reproducing the contradiction as style.

### Source Sentence Patterns, Translated for This Edition

- Layout: "The factoring drawdown page has drawdown cards on the left and a payable list on the right."
- Action: "Click Edit on a drawdown card to open the factoring financing edit page."
- Field: "Drawdown financing organization = payable payer organization; disabled and non-editable; required."
- Reuse: "Credit utilization: same as the credit utilization list in Drawdown."
- Difference: "List fields are the same as the bill-matching page; only rename Transaction Amount to Financing Amount (not editable)."
- Linkage: "When factoring reaches Drawn–Awaiting Repayment, notify the payable to update its status to Matched and create the matching relation."

These examples illustrate expression only. When authoring an actual PRD, preserve the original labels and terms rather than importing these English translations. Before delivery, compare new modules with the closest user-authored sample for structure, sentence patterns, terminology, information density, actual differences, and unnecessarily long explanations. Do not treat an earlier assistant-generated chapter as the user's writing sample.

## 1. Module-Level Order

When no maintained sample establishes a different order, use the following defaults. For a form or detail module, write the applicable items in this order:

1. module purpose and supported actions;
2. fields in visual order;
3. add, edit, delete, associate, query, or submit behavior;
4. validation and boundary conditions;
5. totals and formulas;
6. downstream linkage;
7. states, permissions, feedback, and recovery.

For a list page, prefer:

1. page entry;
2. query conditions;
3. page-level buttons;
4. list fields;
5. row operations;
6. document and approval statuses;
7. permitted operations by status;
8. pagination and empty state;
9. data-scope permissions.

Do not force empty subsections. Include only rules supported by the prototype, existing PRD, or an explicit decision.

## 2. Field Contract

When no maintained sample establishes different phrasing, describe fields in this order. Otherwise, use it as a completeness checklist without rewriting the sample's word order:

`Field: requiredness, component/display; source/options; default and editability; format, range, precision, and unit; linkage or exception rules.`

Examples, translated for this edition:

- "Planning organization: required, single-select dropdown; uses organizations within the current user's data permissions."
- "Planned amount: required, numeric input; meets the business minimum, uses two decimal places, and displays the unit for the selected currency."
- "End date: required, date control; derived from start date and period type; not editable."
- "Status: read-only; displays the current document status; options and transitions are defined under States and Permissions."

Cover the applicable dimensions:

- **Requiredness:** required, optional, conditionally required, or system-generated.
- **Component:** text input, numeric input, single-select or multi-select dropdown, date control, read-only text, switch, attachment component, or action entry.
- **Source:** master data, organization permissions, linked documents, configuration, system calculation, or user input.
- **Options:** list all confirmed values in display order; put incomplete definitions under Pending Items.
- **Editability:** editable, non-editable, or conditionally editable; do not state only a visual appearance such as grayed out.
- **Format:** data type, known length limit, amount or percentage range, decimal precision, date format, and unit.
- **Linkage:** trigger, affected field/module, effective timing, and reset behavior.
- **Empty/error behavior:** confirmed handling for missing values, invalid input, unavailable sources, and failed calculations.

Do not leave descriptions incomplete, such as a field name alone or "Planning status: single-select dropdown" without available source or option information.

## 3. Lists and Operations

Describe list fields in visual order. For editable columns, state requiredness, input type, options/source, constraints, and editability. For calculated or read-only columns, state the source or formula.

Describe operations separately after the fields:

- trigger: what the user clicks or changes;
- precondition: status, permission, or data requirement;
- result: added row, drawer, dialog, navigation, relation, deletion, or submission;
- feedback: button-state change, message, count refresh, save status, or error;
- cancellation/recovery: whether it can be reversed and its downstream impact.

For association actions, specify the selectable business object, single/multiple selection, filters, echoed fields, occupied amount or relationship meaning, cancellation, and invalidation. Unknown dimensions belong under Pending Items.

## 4. Calculations, Units, and Thresholds

Write formulas explicitly using business names, for example:

- `Resource coverage = Total planned resources / Total financing demand × 100%.`
- `Projected balance = Current balance + Additions during the period − Reductions during the period.`

Then state:

- input scope and point in time;
- currency conversion or organization base-currency rule;
- rounding and display precision;
- handling of zero denominators, missing data, and calculation failures;
- recalculation triggers and downstream fields;
- threshold outcome and whether it blocks the workflow.

Use units consistently in labels or descriptions. Do not mix base currency units, ten-thousand units, and hundred-million units in one calculation without an explicit conversion rule. Use BP for basis-point differences and pct for percentage-point differences only when that convention is confirmed.

## 5. States and Permissions

Separate business document status from approval status when both exist.

Describe the following in a compact hierarchy:

1. status groups and allowed transitions;
2. available row/page operations in each status;
3. organization or role scope;
4. prohibited repeat actions;
5. submission, withdrawal, rejection, voiding, deletion, and effective-version behavior.

Use observable language, such as "During approval, only viewing is allowed; editing, deletion, and resubmission are prohibited." Do not write only "controlled by permissions" without identifying the permission dimension.

## 6. Data Sources and Empty Values

When known, name the business source, scope, and aggregation rule, for example:

"Current resources: aggregates valid resources by planning organization and planning period; non-editable; displays 0.00 when no data exists."

Do not infer database tables, APIs, or storage design from a visible label. Include technical mappings only when required by the user or an approved specification.

For standard components such as attachments, cover confirmed selection scope, file constraints, association type, organization mapping, summary information, preview/download/delete behavior, and storage mapping. Put missing limits and persistence rules under Pending Items.

## 7. Cross-Module Linkage

When an input changes, trace:

`Input change → Local totals → Linked modules → Risk/status → Submission or task result`

State only confirmed links, but inspect at least:

- count and amount totals;
- resource coverage or plan balance;
- calculated cost and risk indicators;
- submission eligibility;
- generated downstream task data;
- association validity after source changes.

## 8. Pending Items

Use one consolidated Pending Items row. Each item names the business object and missing decision, for example:

- selectable source objects and single/multiple selection;
- exchange-rate source and conversion date;
- calculation baseline and failure handling;
- threshold source and blocking policy;
- attachment limits and deletion rules;
- approval lifecycle and version retention.

Do not repeat questions already resolved in the PRD. When the user decides an item, remove it from the pending list and update its owning requirement at the same time.

For each item, state the object and missing decision; affected rules/modules; and what can proceed versus what depends on confirmation. Keep simple items short. Do not invent a recommended rule or silently treat a proposed answer as approved.

Example: "The credit utilization timing for financing applications is pending: submission or approval; this affects available amounts, concurrent over-limit checks, and release on withdrawal. Field descriptions can proceed; related calculations and acceptance outcomes remain unresolved." The alternatives illustrate an open choice, not a default financing policy.

## 9. Prototype Screenshots and Document Inspection

Use this procedure when adding or replacing screenshots.

### 9.1 Map Requirement Rows to Screenshots

Before capture, record at least:

`Requirement row → OpenDesign page → Functional region → Interaction state → Screenshot count`

The screenshot must support the visible fields, actions, feedback, and states described in that row. Do not capture full pages first and assign them to requirement rows afterward.

### 9.2 Capture the Exact Functional Region

- **Lists and queries:** include relevant query conditions, summaries, page actions, columns, row operations, pagination, or empty state; exclude unrelated areas.
- **Forms and fields:** capture the owning form module with labels, controls, required marks, defaults, and visible linkage.
- **Dialogs, drawers, and details:** capture the opened surface in the relevant state; use a dedicated image when the background is unnecessary.
- **Comparisons and risk rules:** capture the comparison table or risk/recommendation panel itself; sharing a page does not justify reusing a full-page image.
- **Non-screen processes:** use an existing, confirmed flow artifact; do not invent a UI screenshot.

The functional region should occupy most of the image. Exclude unrelated navigation, browser chrome, and large blank areas. Split long modules into ordered images if a single screenshot would make text too small.

Reuse screenshots only when rows describe the same visible region and interaction state. A shared source page is insufficient.

### 9.3 Preserve Image Quality

- Prepare the prototype state before capture: expose the relevant module, dialog, drawer, error, empty state, or selected result, and remove avoidable obstructions.
- Prefer lossless or high-quality originals. Do not enlarge a low-resolution full-page image instead of recapturing the functional region.
- Judge readability after insertion, not just source dimensions. At the remote document's normal reading scale, labels, buttons, statuses, and key values must be distinguishable without opening the image separately.
- Preserve the prototype-cell title and user-authored text. Place images below the matching title and keep multiple images in reading order.

### 9.4 Verify Each Affected Row

After upload, inspect each populated Prototype cell for:

`Content match | Accurate functional crop | Readable text | Correct placement | Upload complete | Document saved`

All six checks must pass before reporting completion. An image node, completed upload, or saved-state indicator proves only technical persistence; it does not prove correct content, crop, readability, or placement.

If any content, crop, readability, or placement check fails, recapture and replace the image, wait for upload and save completion, and repeat the row-level inspection.

## 10. Language and Formatting

- Use short declarative sentences and exact product labels.
- Use Chinese punctuation consistently in Chinese deliverables; end complete rules with a full stop.
- Use semicolons to separate component, source/options, constraints, and linkage.
- Preserve existing numbering, including `1.` → `a.` → `i.` or nested numeric lists; do not normalize it.
- Avoid generic filler such as "improve the experience", "support related actions", or "the system handles it automatically".
- Do not repeat the same formula or status rule in multiple rows. Keep the full rule in its owning module and reference its effect elsewhere.
- Preserve user wording for approved business decisions rather than replacing terms for stylistic polish.
