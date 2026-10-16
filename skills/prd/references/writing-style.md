# PRD Writing Style

Use this reference for the compact, field-oriented Chinese PRD style learned from the maintained enterprise PRD.

## 0. 用户原文的风格对齐（优先于下述默认写法）

依据：用户于2026-10-16明确要求，相同或相近逻辑尽量沿用其文字风格和描述方式；样本为用户编写的《保理优化》第五章反向保理。以下用于该用户的类似企业PRD任务；新任务提供其他样例或明确要求时，以新样例和最新要求为准。只学习表达，不将样本中的业务规则、未完成条目或矛盾推广为通用规则。

### 表达与粒度

- 先读用户提供的完整相关模块及最接近的人工章节，识别页面分行、字段顺序、编号、句式和信息密度。相同逻辑优先沿用原句结构并替换确有差异的业务对象，不重新组织成另一套产品文档。
- 沿用“原型图／需求分析”等现有列名，一行对应一个页面、抽屉、弹窗或相关改造模块；按原文使用 `1.` → `a.` → `i.` 分层。字段归在“基本信息”等所属模块内，不把原来有层级的条目改成长段平铺。
- 直接写功能和操作：`列表包含……`、`过滤……`、`点击……，打开／进入……`、`若……，则……`、`当……时，通知……更新……`。一条说明一个动作或一组紧密关联的规则；需要展开时用下一层编号。
- 字段使用原文的紧凑表达，如 `机构类型：默认银行，可修改，必填`。保留用户的字段名、业务术语、默认值和“置灰不可修改”等明确用语；字段契约作为完整性核对清单，不强制重排原文词序，也不为每个字段机械补齐全部维度。
- 与现有功能一致时，写 `与××相同`、`复用××`；只有差异时，写 `在××基础上，增加／剔除……`、`仅将“××”更名为“××”（不支持修改）`。引用应能定位到具体功能或模块，差异要明确；实际有重要差异或来源不明时，不能笼统写“同现有逻辑”。
- 简短补充可沿用括号和 `注：`；保留已明确的P0/P1，不自行分配优先级。不要复制样本中的人员提及、空编号、笔误或未完成内容。

### 分析与正文分开

- 业务分析可以充分，PRD正文优先保留可执行的字段、动作、条件、结果和联动。不要把分析过程、概念辨析、设计理由、反复声明、通用风控清单和交付状态说明逐条塞进需求单元格。
- 必要的金额、权限、异常和闭环规则用原文粒度写入所属条目；共用规则集中说明一次，其他模块描述差异或引用。不能为了简短省略已知关键条件，也不能仅为显示完整而扩展页面或流程。
- 未知规则集中到“待确认项”，简要写清缺什么及影响；当前任务无关的远期问题不追加。同一未定事项不在每一行重复解释。发现原文冲突时说明位置与后果，不因模仿风格沿用矛盾规则。

### 原文句式示例（仅示范表达）

- 布局：`保理提款页面为左侧提款卡片，右侧应付列表。`
- 操作：`点击左侧提款卡片的编辑，进入保理融资编辑页面。`
- 字段：`提款单融资组织＝应付单付方组织，置灰不可修改，必填。`
- 复用：`占用授信：与提款中占用授信列表相同。`
- 差异：`列表字段与票据配单页面相同，仅将“交易金额”更名为“融资金额”（不支持修改）。`
- 联动：`当保理状态为已提款-待还款时，通知应付单更新状态为已认领，创建认领关系。`

交付前，将新增模块与最接近的用户原文并排核对：结构、句式、术语和信息密度是否一致；是否仅展开真实差异；是否将必要补充写成了过长的解释。不要将此前助手生成的长篇章节当作用户写作风格样本。

## 1. Module-Level Order

When no maintained sample establishes a different order, use the following as a fallback. For a form or detail module, write in this order when applicable:

1. module purpose and supported actions;
2. fields, in visual order;
3. add, edit, delete, associate, query, or submit behavior;
4. validation and boundary conditions;
5. totals and formulas;
6. linkage to downstream modules;
7. state, permission, feedback, and recovery rules.

For a list page, prefer:

1. page entry;
2. query conditions;
3. page-level buttons;
4. list fields;
5. row operations;
6. document and approval statuses;
7. status-to-operation permissions;
8. pagination and empty state;
9. data-scope permissions.

Do not force empty subsections. Include only rules supported by the prototype, existing PRD, or an explicit decision.

## 2. Field Contract

When no maintained sample establishes a different phrasing, describe fields with this sequence; otherwise use it as a completeness checklist without rewriting the sample’s word order:

`字段名：必填性，组件或展示方式；数据来源/枚举；默认值与可编辑性；格式、范围、精度和单位；联动或异常规则。`

Examples:

- `规划组织：必填，下拉单选；取当前用户有权限的组织数据。`
- `计划金额：必填，数字输入；金额应满足业务下限，保留两位小数；单位随所选币种展示。`
- `结束日期：必填，日期控件；由系统根据开始日期和周期类型带出，不可编辑。`
- `状态：只读；展示当前单据状态，枚举及流转规则见状态与权限。`

Apply these dimensions deliberately:

- **必填性**: 必填、非必填、条件必填、系统生成。
- **组件**: 输入框、数字输入、下拉单选、下拉多选、日期控件、只读文本、开关、附件组件、操作入口。
- **来源**: 基础数据、组织权限范围、关联单据、配置项、系统计算、用户录入。
- **枚举**: list all confirmed values in the display order. If incomplete, move the missing definition to `待确认项`.
- **编辑性**: 可编辑、不可编辑、条件可编辑; avoid using only the visual phrase `置灰`.
- **格式**: data type, length when known, amount or percentage range, decimal precision, date format, and unit.
- **联动**: triggering field/action, affected field/module, timing, and reset behavior.
- **empty/error**: empty display, invalid input, unavailable source, or failed calculation behavior when confirmed.

Avoid incomplete descriptions such as `规划组织：` or `规划状态：下拉单选；` with no source or options when that information is available.

## 3. Lists and Operations

Write list fields in visible order. For each editable column, state requiredness, input type, options/source, constraints, and editability. For calculated or read-only columns, state the source or formula.

After the field list, describe operations separately:

- trigger: what the user clicks or changes;
- precondition: status, permission, or data requirement;
- result: added row, drawer, dialog, navigation, relation, deletion, or submission;
- feedback: button-state change, toast, refreshed count, saved status, or error;
- cancellation/recovery: whether the action can be reversed and its downstream impact.

For association actions, specify the selectable business object, single/multiple selection, filters, echo fields, occupied amount or relation semantics, cancellation, and invalidation. Unknown dimensions belong in `待确认项`.

## 4. Calculations, Units, and Thresholds

Write formulas explicitly with business names:

- `资源覆盖率=规划资源合计÷融资需求合计×100%。`
- `预计余额=当前余额+本期新增金额-本期减少金额。`

Then state:

- input data scope and time point;
- currency conversion or organization-base-currency rule;
- rounding and display precision;
- zero denominator, missing data, and calculation failure behavior;
- recalculation trigger and downstream fields;
- threshold result and whether it blocks the workflow.

Use one unit consistently in the field name or field description. Do not mix `元`, `万元`, and `亿元` across the same calculation without an explicit conversion rule. Use `BP` for basis-point differences and `pct` for percentage-point differences only when that convention is confirmed.

## 5. States and Permissions

Separate business document status from approval status when both exist.

State rules in a compact matrix-like hierarchy:

1. status groups and allowed transitions;
2. available row/page operations for each status;
3. organization or role scope;
4. prohibited repeat actions;
5. submit, withdraw, reject, void, delete, and effective-version behavior.

Use observable language: `审批中仅允许查看，不允许编辑、删除或重复提交。` Avoid vague phrases such as `按权限控制` without identifying the permission dimension.

## 6. Data Sources and Empty Values

Name the business source, scope, and aggregation rule when known:

`当前资源：系统按规划组织和规划周期汇总有效资源；不可编辑；无数据时展示0.00。`

Do not infer a database table, API, or technical storage design from a visible label. Include technical mappings only when the user or an approved specification requires them.

For standard components such as attachments, cover confirmed selection scope, file constraints, association type, organization mapping, summary information, preview/download/delete behavior, and storage mapping. Put missing limits and persistence details in `待确认项`.

## 7. Cross-Module Linkage

Whenever an input changes, follow the impact chain:

`输入变化 → 本模块合计 → 关联模块 → 风险/状态 → 提交或任务结果`

State only confirmed links, but inspect at least:

- count and amount totals;
- resource coverage or plan balance;
- calculated cost and risk indicators;
- submission eligibility;
- generated downstream task data;
- association validity after source changes.

## 8. Pending Items

Use one consolidated `待确认项` row. Each item must name the object and missing decision, for example:

- selectable source objects and single/multiple selection;
- exchange-rate source and conversion date;
- calculation baseline and failure handling;
- threshold source and blocking policy;
- attachment limits and deletion rules;
- approval lifecycle and version retention.

Do not repeat questions already resolved in the PRD. Remove an item when the user decides it, and update the affected requirement row at the same time.

For each item, state `对象与缺失决策；受影响规则/模块；可继续的工作与依赖确认的部分。` Keep simple items short. Do not invent a recommended rule or silently treat a proposed answer as approved.

Example: `融资申请额度占用时点待确认：提交时还是审批通过时占用；影响可申请金额、并发超额校验和撤回释放规则；页面字段可继续编写，相关计算及验收预期暂不定稿。` The alternatives illustrate an unresolved choice, not default financing policy.

## 9. Prototype Screenshot and Document Inspection

Use this procedure whenever screenshots are added or replaced in a PRD.

### 9.1 Build the Row-to-Screenshot Map

Before capture, record the minimum mapping:

`PRD row name → OpenDesign page → functional region → interaction state → screenshot count`

The screenshot must support the visible fields, actions, feedback, and states described in the corresponding requirement row. Do not capture a full page first and assign it to rows afterward.

### 9.2 Capture the Exact Functional Region

- **List and query rules:** include the relevant query conditions, summary, page actions, list columns, row operations, pagination, or empty state; crop out unrelated application areas.
- **Form and field rules:** capture the owning form module with its labels, controls, required marks, defaults, and visible linkage state.
- **Dialog, drawer, and detail behavior:** capture the opened surface in the state described by the row. Use a separate image when the background page is not needed to explain the behavior.
- **Comparison and risk rules:** capture the comparison table or risk/recommendation panel itself. Do not reuse a full-page image merely because both modules appear on the same page.
- **Non-screen processes:** use an available and confirmed flow artifact; do not invent a UI screenshot.

The functional region must occupy most of the image. Exclude unrelated navigation, browser chrome, and large blank areas. If one long image would make labels or values unreadable, split the module into multiple images and keep their order clear.

Reuse an image only when the rows genuinely describe the same visible region and interaction state. Sharing a source page is not sufficient reason for reuse.

### 9.3 Preserve Image Quality

- Prepare the OpenDesign state before capture: expose the required module, dialog, drawer, error, empty state, or selected result and remove avoidable obstructions.
- Prefer lossless or high-quality source images. Do not enlarge a low-resolution full-page image as a substitute for recapturing the functional region.
- Judge effective readability after insertion, not only source-image dimensions. At the remote document's normal reading scale, relevant labels, buttons, statuses, and key values must be distinguishable without opening the image separately.
- Preserve the prototype-cell title and existing manual text. Place each image below the matching title and keep multiple images in the order used by the requirement description.

### 9.4 Verify Every Affected Row

Check each populated `原型` cell after upload:

`content match | functional crop | readable text | correct placement | upload complete | document saved`

All six checks must pass before reporting the screenshot work complete. Image-node existence, upload completion, or a saved-state indicator proves only technical persistence; it does not prove correct content, crop, readability, or placement.

If any content, crop, readability, or placement check fails, recapture and replace the image, wait for upload completion, confirm the remote document is saved, and repeat the row-level inspection.

## 10. Language and Formatting

- Use short declarative sentences and exact product labels.
- Use Chinese punctuation consistently; end complete rules with `。`.
- Use semicolons to separate component, source/options, constraints, and linkage.
- Preserve the document's numbering style: `1.` → `a.` → `i.`.
- Avoid generic filler such as `优化体验`, `支持相关操作`, or `系统自动处理`.
- Avoid duplicating the same formula or status rule in multiple rows; keep the full rule in the owning module and reference its effect elsewhere.
- Preserve user wording when it expresses an approved business decision, even if a more polished synonym exists.
