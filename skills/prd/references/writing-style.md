# PRD Writing Style

Use this reference for the compact, field-oriented Chinese PRD style learned from the maintained enterprise PRD.

## 1. Module-Level Order

For a form or detail module, write in this order when applicable:

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

Describe fields with a stable sequence:

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

## 9. Language and Formatting

- Use short declarative sentences and exact product labels.
- Use Chinese punctuation consistently; end complete rules with `。`.
- Use semicolons to separate component, source/options, constraints, and linkage.
- Preserve the document's numbering style: `1.` → `a.` → `i.`.
- Avoid generic filler such as `优化体验`, `支持相关操作`, or `系统自动处理`.
- Avoid duplicating the same formula or status rule in multiple rows; keep the full rule in the owning module and reference its effect elsewhere.
- Preserve user wording when it expresses an approved business decision, even if a more polished synonym exists.

