# Acceptance and Consistency Review

Use for full PRDs, reviews, and changes to behavior, amounts, relationships, states, or permissions. For an incremental change, check the modified rule and actual dependencies only.

## Derive Observable Scenarios

For each consequential rule, try to express:

`前置业务状态/数据/角色 → 用户或系统动作 → 可观察的结果及关联影响。`

Use the approved rule as the expected outcome. When no outcome is established, record the missing decision; do not choose one to make the scenario complete. Select representative normal and adverse cases proportional to the change. Generated scenarios are not executed tests.

Inspect only relevant counterexamples:

| Rule | Useful probes |
|---|---|
| Amounts and aggregation | Duplicate links, partial fulfillment, invalidated records, currency and time scope |
| Lifecycle | Rejection, withdrawal, repeated submission, changes after execution |
| Associations | Source changes or deletion, unlinking, historical validity |
| Permissions | Organization scope, role operations, visibility versus editing rights |
| Concurrency | Competing actions on the same limited amount or record, when the process permits them |
| AI-generated options | Missing inputs, regeneration, manual edits, adopted versus candidate versions |

Example: a requirement has two linked applications and one is withdrawn. Check the documented impact on requested amount, remaining amount, and fulfillment status. If occupancy timing is undecided, those expected amounts remain pending; no default release policy is implied.

## Compare Decisions, PRD, and Prototype

For each material change, compare the applicable user decision, the exact PRD rule, and the relevant visible prototype behavior. Record evidence locations during work; do not force new IDs or source tables into the user's PRD.

Classify differences as nonconflicting additions, explicit conflicts, or unknowns using the source rules in SKILL.md. Absence of a rule from a screen does not prove absence of that business requirement.

Trace changed inputs through actual dependencies: local totals, linked modules, status/risk results, submission eligibility, and downstream actions. When removing something, check surviving references, formulas, status rules, screenshots, and pending items. Verify only applicable links; do not invent a new downstream process.

## Close the Review

Incorporate supported clarifications into their owning requirement rows. Put unresolved expectations into the consolidated pending items with their impact. Produce a standalone acceptance table only when requested; include objective, preconditions, role, steps, and expected outcomes then.

Distinguish business-rule verification from implementation verification. Reading a PRD or prototype cannot prove server-side enforcement. Inspect code only when implementation review is requested and code is available; cite both requirement and code evidence. Do not mark software acceptance complete from document review or static inspection alone.
