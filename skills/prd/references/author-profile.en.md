# User PRD Logic and Expression Profile

Read this when authoring or rewriting this user's PRDs. Match their business decomposition, structure, language, wording, and level of detail. Check business completeness and stylistic fidelity separately; more content cannot compensate for a different writing style.

## Evidence and Limits

On 2026-10-30, the user identified a budget folder, confirmed documents created by either Li Jinglun or Wu Mingzhi as their own work, then accepted all 34 files as writing samples. Full-content receipts were obtained for 32; two were unavailable and excluded. Creator fields were absent, so attribution comes from the user's confirmation.

Source anchors:

- [Recurring items](https://alidocs.dingtalk.com/i/nodes/Qnp9zOoBVBZ9egmAHPrNlAMGV1DK0g6l): list, basic information, details, generation mappings, and task linkage.
- [Budget preparation redesign](https://alidocs.dingtalk.com/i/nodes/gwva2dxOW4K7yr36Hqyw6NgN8bkz3BRL): full-module structure, navigation/buttons, three-column design, and differences between screen states.
- [May 2026](https://alidocs.dingtalk.com/i/nodes/gvNG4YZ7JnegbYlNcqopB0O0V2LD0oRE): affected pages/actions, field placement, branches, related pages, and historical data.
- [June 2026](https://alidocs.dingtalk.com/i/nodes/AR4GpnMqJzM5YjZ0faRrP1p4VKe0xjE3): query and list-field tables, exports, common rules, and differences.
- [September 2026](https://alidocs.dingtalk.com/i/nodes/mExel2BLV540yRpAIPg6PanxWgk9rpMq): requests/responses, validation, processing, and related changes.
- [November 2026](https://alidocs.dingtalk.com/i/nodes/QOG9lyrgJP3ljRGMtlo1jP1jVzN67Mw4): sequential filtering, deduplication, utilization, asynchronous feedback, and action restrictions.

These establish writing and decomposition patterns, not universal business policies. The budget feature introduction consists mainly of screenshots. Text retrieval does not establish fields inside images, typography, or interaction; do not claim visual replication from text alone.

## 1. Choose the Matching Document Shape

Use the current maintained document, then the task's designated sample, then a recent comparable user chapter, then these references. Select structure separately from business-rule precedence: an older format can be reused without reinstating old rules.

| Task | Sample shape | Application |
|---|---|---|
| Existing PRD edit | Existing headings, columns, numbering, field order, and row boundaries | Edit in place; retain three columns when present; do not normalize all documents. |
| Monthly collection/local improvement | Existing sequence/title/DevOps index; functional headings; two-column prototype/analysis or nested items | Preserve real links; do not invent links or create a monthly collection for a single edit. |
| Complete module redesign | Title, change record, functional structure/process, navigation/buttons, list headers, functional design, related changes | Use only when established by the current document or chosen sample; functional design can have prototype/function/detail columns; no empty flow diagrams. |
| Configuration/form | Owning prototype module, basic information, details, buttons, rules | Follow the actual closest sample order. Combine identical create/edit/view behavior; split actual differences. |
| Interface/scheduled processing | Interface name, requests, responses, validation, processing, related changes; or trigger/source/processing | Do not invent screens or screenshots. Preserve existing single-column analysis tables too. |

Keep the existing nested numbering, whether `1.`/`a.`/`i.` or nested numeric lists. Exported consecutive numbers may conceal indentation; recover hierarchy from nesting and ownership. Name headings after the function/change, without promotional language.

## 2. Follow the User's Business Decomposition

These guide analysis; they are not mandatory output chapters:

1. Locate the menu, affected screens/actions, and the concrete existing problem when needed; do not begin with a generic vision.
2. Place the change in the existing model: unchanged, added, renamed, removed, or adjusted. Reference shared behavior and describe real differences.
3. Specify field placement/order, requiredness, selection, options/source, default/editability, and evidence-supported conditional display/disable/reset behavior.
4. Expand branches by object, configuration, state, organization, or source using explicit if/then rules; do not hide the decision behind automatic matching or smart validation.
5. For data rules, trace trigger → state/scope filters → organization/date/subject matching → amount field → deduplication/aggregation/utilization → result/linkage. State applicable fallback order without turning a field-specific fallback into universal source priority.
6. Check actual impacts on create/edit/view/approval, queries/header filters, sorting, import, export/custom export, interfaces, and historical records. Do not convert this inspection list into automatic scope.
7. Verify relevant organization hierarchies, duplicates, empty values, amounts/periods, cancellation, and failure. Preserve established special branches; put missing decisions in Pending Items instead of adding approvals, drafts, versions, or reapproval.

Explain motivation only where needed. Complex data rules may be detailed; a simple column addition may need only one or two items. Combine identical behavior and separate differing sources, editability, or state restrictions.

## 3. Language and Sentence Patterns

Write direct Chinese statements using 新增／增加／调整为／更名为／去除, 默认……，可改, 置灰不可修改, 若……，则……, 否则提示, 同步调整, and 其余逻辑同…….

- Compact fields can follow requiredness, control, single/multiple selection, options, default/editability, while retaining current phrasing. Do not append empty contract dimensions.
- If the module uses a field-name/requiredness/type/business-rule table, retain that table and groups such as basic information/contracts/invoices rather than converting everything to colon sentences. January and April 2026 contain this shape.
- Name positions explicitly: below a field, after a column, or at the end of a list. Separate page-specific editability.
- Queries state field, operators, control/options, and sorting. Preserve established query-table column labels rather than replacing them with a generic data dictionary.
- Actions specify enable/disable conditions and single/batch selection, then the screen/result and necessary messages. Preserve sourced quoted text and parameters.
- Use business names in formulas. Briefly distinguish calculation/display units, times, precision, and empty values where relevant. Examples explain hard cases, not every item.
- Preserve exact state labels and supplied enum codes; do not invent codes or rename them.
- Retain source label delimiters, concise statements, semicolons, parentheses, and useful notes/emphasis. Do not copy typos, empty numbers, personal mentions, chasing language, or export corruption.

Avoid consulting-style essays or generic declarations about safety, consistency, and lifecycle capability. State the object, condition, action, and result directly.

## 4. Short Source Examples and Transfer

The Chinese edition preserves short Chinese examples because delivery remains Chinese. Business rules apply only to their source contexts.

- Field placement/default pattern, June 2026: “预算模板”字段下方新增“预算币种”字段：必填，下拉框，单选，下拉枚举为所有币种.
- Batch modification, August 2026: state selection and disabled conditions; require matching transaction direction; open the edit dialog; synchronize the modified statement information.
- Retrospective utilization, November 2026, summarized: trigger on budget execution; identify valid rules; filter by organization/date/payment method/subject/state; deduplicate payables and their payment documents; exclude already utilized documents; process the remainder. Learn the decomposition, not a universal utilization-without-control policy.

Illustrative rewrite, not a user quotation: replace a generic statement about efficiency and data consistency with “列表左下角新增‘批量修改’按钮；未勾选数据时置灰。点击后打开批量修改弹窗，修改后同步更新关联流水。” This is valid only if the target task establishes those positions, actions, and objects.

## 5. Historical Revisions and Unresolved Content

- Interpret strikethrough, color, highlights, P0/P1, version notes, and deferred items in context. Strikethrough may mean canceled, replaced, or completed; it does not prove implementation. Do not merge struck alternatives with their replacement.
- Separate draft options/questions/suggestions from detailed approved requirements. If authority is unclear, record the missing choice; do not build both alternatives automatically.
- Months and modification times help locate evidence but do not prove supersession. Check each rule. Carried-forward text is not independent evidence of multiple stylistic choices.
- November 2026 counterparty control includes conflicting non-struck branches for a missing counterparty: subject-level control versus no validation. Identify the conflict instead of inventing one default.
- Keep format learning separate from business judgment: neither reproduce contradictions for style nor change the user's style to add necessary controls. Write established corrections in their phrasing and keep unknowns pending.

## 6. Compare in Both Directions

Compare against the closest user chapter for decomposition order, headings/columns, row size, numbering, field order, terms, sentences, density, and references; then check fields, actions, amounts, exceptions, and linkage for omissions.

Repair changed structure, excess explanation, full plans for small edits, inconsistent phrasing across similar modules, or missing special branches. Keep this internal unless a report is requested. Without user feedback on actual generated PRDs, report skill/sample checks only; do not claim perfect equivalence.

## 7. Calibration from the Factoring Comparison

On 2026-10-30, compare the maintained Chapter 4 with the independent Chapter 6 in [Factoring optimization](https://alidocs.dingtalk.com/i/nodes/ydxXB52LJq7pexNrIM9NE9pGWqjMp697). The independent version intentionally excluded Chapter 4 at the user's request; newly disclosed project decisions were not knowable in advance. Learn the methods below without generalizing this project's amount basis, requiredness, or bank-connectivity scope into universal policy.

- **Keep a page together:** Prefer one row for a page's basic information, details, components, linkage, and buttons, using its existing groups and numbering. Split only actual independent screens, flows, or differing states; do not spread one form across generic rule chapters.
- **Reuse before expanding differences:** When an existing component covers the behavior, retain a locatable component reference and describe the actual additions or changes rather than redefining its internals. If the user asks to copy an adjacent chapter's corresponding wording, copy it and verify target objects and differences; a vague same-as-Chapter-5 reference is insufficient. Valid references to established components remain acceptable.
- **Check field behavior together:** Reconcile source, default, editability, linkage, and requiredness, especially for the same field on different screens. Do not invent a required field, turn a disabled amount into an input, or equate an account-opening bank with a financing institution. Keep missing decisions unresolved.
- **Trace generated objects:** Within the owning page, identify source document → generated document → downstream processing object and result. Amount distinctions or financing-is-not-collection statements do not replace concrete mappings. Separate source and generated document responsibilities without inventing extra registers or amount dimensions for completeness.
- **Preserve confirmed actions and inspect impacts:** If the user allows editing or voiding in a particular state, retain the action and inspect affected fields, linked documents, utilization, and plans. Keep unspecified handling pending rather than prohibiting the action from generic practice or claiming its effects are settled.
- **Length does not prove coverage:** Check card fields, drawer filters, amount basis, options, buttons, mobile support, and actually affected interfaces. Long conceptual explanations cannot compensate for missing established functionality. Do not claim coverage of screenshot content that was not inspected.
- **Attribute feedback correctly:** Separate style mismatches, omissions of previously known rules, newly disclosed project decisions, and gaps in the maintained draft. Retain reusable methods without copying typos, incomplete conditions, or unverified contradictions.
