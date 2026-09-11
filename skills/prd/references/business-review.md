# Business Review for Enterprise PRDs

Use for new functionality, cross-module rule changes, or substantive review. Focus on decisions that change the specification; skip questions already answered and dimensions irrelevant to the request.

## Problem and Scope

Identify the actor, situation, underlying problem, expected outcome, and constraints from supplied evidence. Distinguish a requested feature from the problem it addresses, while respecting solutions the user has already chosen. Compare alternatives only when there is a material unresolved tradeoff. Do not require a fixed number of options, numeric scoring without inputs, or a measurable growth target for every enterprise requirement.

For multi-customer requests, group common problems and identify which differences justify configuration, a shared capability, or a separate extension. Do not assume that every variation should become configurable.

## Business Objects and Ownership

Before relying on screen boundaries, identify the relevant business objects and their responsibilities:

- What fact or decision does each object own? Who creates and maintains it?
- Which relationships are one-to-one, one-to-many, or many-to-many, if known?
- Which data is authored, referenced, snapshotted, or aggregated? Distinguish these only where the behavior depends on it.
- Are two modules independently maintaining the same fact? Is the apparent duplicate actually a different time, stage, version, or business meaning?
- When the source changes, is withdrawn, or becomes invalid, what happens to linked records and downstream results?

If a module is removed or merged, account for each displaced responsibility: explicitly retired, retained elsewhere, or unresolved. Do not infer database tables or APIs from this analysis.

Example: removing a financing arrangement section may affect plan expression, amount summaries, and execution links. Check where those responsibilities go; do not prescribe a universal financing workflow or assume the user wants every responsibility retained.

## Challenge Critical Assumptions

Identify assumptions whose failure would change the chosen scope or break the core process. State the strongest supported rationale before challenging it. For a consequential uncertainty, give the precise failure condition, evidence needed, and smallest useful verification step. Recommend stop/change criteria only when relevant, and label unapproved thresholds as proposals.

Use qualitative priority when likelihood or impact cannot be supported. A conceivable risk is not an established defect. A sound decision need not acquire a criticism merely to fill a report.

## Findings That Can Be Acted On

Classify each finding:

- **明确矛盾:** Cite both established rules and explain why they cannot coexist in the applicable scenario.
- **规则缺失:** Name what the materials do not establish and the resulting implementation or acceptance uncertainty. Add it to the consolidated pending items.
- **优化建议:** Explain an optional improvement and its tradeoff; do not promote it to a requirement without a decision.

Include the concrete section, field, action, or screen, the consequence, and a specific correction or decision needed. Consolidate duplicate findings. State sound aspects and evidence limits where useful. Fit explanations into the existing PRD structure; output a separate review only when that is the requested deliverable.
