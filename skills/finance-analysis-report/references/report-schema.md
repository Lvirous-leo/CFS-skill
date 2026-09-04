# Financing Analysis Report Schema

Use a nine-section report that starts with financing operations, then presents executive decisions and finance-team evidence. If a user Word template is active, map its headings to these semantic modules and preserve every required module.

## Required modules

1. **融资经营分析总览**: one-sentence overall judgment; core operating metrics; reporting date, consolidation scope, reporting currency and unit; metric-level coverage and limitation notices.
2. **模板适配说明**: required only when a user template is used; list template identity, parsing state, retained sections, system additions, local style fallback, ambiguity and ignored unsafe objects.
3. **高管决策摘要**: structured management narrative and comparison-oriented KPI table.
4. **需决策或协调事项**: approval or cross-entity/external coordination, latest decision date and consequence of delay.
5. **融资余额与结构**: entity, lender, product, currency, tenor, fixed/floating structure, concentration, weekly flows and anomalies.
6. **融资成本与利率风险**: weighted cost, cost coverage, fee basis, fixed/floating split, LPR/SOFR/HIBOR exposure and reset timing.
7. **授信与流动性**: effective, used, restricted, direct available, derived available, utilization, facility expiry/conditions and 7/15/30-day coverage.
8. **债务到期墙**: overdue items, 12-month principal/interest, concentration, eligible coverage, residual gap, actions and backups.
9. **担保及或有风险**: remaining exposure, contractual cap, parties, responsibility, dates, counter-guarantee, excess-shareholding status, potential calls and facility use.
10. **建议与行动清单**: evidence-bound recommendations and accountable execution fields.

The standard report has nine numbered business sections because the conditional template-adaptation statement is not numbered as a standard business section.

## Section 1: 融资经营分析总览

Start with the management outcome, not a metadata chapter.

- Give a one-sentence overall judgment.
- Explain the operating meaning of financing balance, weighted financing cost, credit balance and utilization, available credit, 30-day maturities, guarantee exposure and cash-debt ratio when supported.
- State reporting date, consolidation scope, reporting currency and unit compactly in the opening block.
- Put missing, conflicting, stale or partial coverage beside the affected metric or in a limitation note at the end of this section.
- Show `无法计算` and the missing required fields when a metric cannot be calculated. Never convert missing data into zero.

## Section 2: 高管决策摘要

### Management narrative

Use these four subheadings and write each in the sequence current state, comparison, impact and management action:

1. **授信经营**: scale, utilization, drawable reserve, expiry and conditions.
2. **融资经营**: balance, product, tenor, lender/entity structure, new draws, repayments and concentration.
3. **成本经营**: weighted cost, fixed/floating exposure, benchmark exposure and comparable cost movement.
4. **风险事项**: overdue debt, maturity wall, residual liquidity gap, guarantees, currency exposure and material data limitations.

Use `无可比数据` when no validated comparison period exists. Do not infer a trend from one period.

Under each management heading, use numbered points restarting at 1, each in its own paragraph. Start points with a short topic label such as `规模变化` or `管理动作`. Keep evidence and its implication together; do not force separate empty points when information is unavailable. In Word use native numbering, not manual digits separated by soft line breaks.

### Core KPI table

Use exactly these columns:

| 指标（含币种/单位） | 本期 | 环比期 | 环比变化额 | 环比变化率 | 同比期 | 同比变化额 | 同比变化率 | 管理判断 |
|---|---:|---:|---:|---:|---:|---:|---:|---|

- Put currency and unit in the metric name, for example `融资余额（人民币万元）`.
- Do not include separate `币种/单位` or `定义/覆盖` columns.
- Use the explicitly configured prior-month/comparable-period basis for 环比 and the same date or comparable period in the prior year for 同比; state both comparison dates and ensure metric definitions, scope, currency and units are consistent. Do not silently label a previous weekly report or an unequal flow interval as monthly 环比.
- If either comparison base is unavailable, use `无可比数据` in that base's value, absolute-change and change-rate cells without suppressing the other valid comparison.
- Put formula, definition, coverage and limitations in a table note or the related narrative.
- Include these eight core metrics: financing total, weighted all-in financing cost, future 30-day maturity principal, unconditionally available credit, 30-day confirmed funding gap, guarantee balance, excess-shareholding guarantee amount and cash-debt ratio. Show `无法计算` with the missing inputs beside an unsupported metric rather than omitting it or substituting zero.
- Distinguish future 30-day principal from overdue principal, interest and the combined gross funding requirement. Do not use these as interchangeable comparison series.
- For rate metrics, label absolute changes as percentage points or BP; relative change remains a percentage. Calculate from full-precision inputs, not the displayed rounded values. Use the same inputs and formulas in Excel and narrative.
- Keep all nine KPI columns legible. In Word prefer an appropriate landscape section or deliberate column widths and repeated table headers over shrinking the text excessively. Preserve a supplied template where feasible.

## Section 3: 需决策或协调事项

Include only items requiring management approval, cross-entity coordination or external confirmation. Use columns: item, evidence, decision/coordination required, latest decision date, accountable party and consequence of delay.

## Sections 4-9: 图表—明细表—分析说明

Use the following ordered subheadings in every standard-report section from 融资余额与结构 through 建议与行动清单:

1. **图表**
2. **明细表**
3. **分析说明**

### Chart requirements

- Put the most decision-useful trend, structure, concentration or coverage relationship first.
- Include subject, currency/unit and reporting date in the chart title or immediate caption.
- State scope, coverage and relevant limitations below the chart.
- Reconcile every chart value to the following detail table.
- Pair each visual with its matching table and then its explanation. For multiple dimensions, repeat this local pairing or clearly label each chart/table pair; do not put unrelated tables beneath a chart without explaining the additional dimension.
- Use actual quantitative charts for quantitative findings. A generic flowchart is not a substitute for a financing balance, cost or maturity chart. Where rendering is unavailable, provide the chart data and explicitly disclose that limitation.
- When rendering is unavailable, provide structured chart data and the recommended chart type.
- When data is insufficient for a meaningful chart, keep the chart subsection and write `数据不足，未生成图表` with the exact missing fields. Never create illustrative values.

Use these chart choices when supported:

- **融资余额与结构**: entity, lender, product or currency structure and concentration.
- **融资成本与利率风险**: comparable cost/benchmark trend; otherwise fixed/floating or benchmark exposure structure.
- **授信与流动性**: facility composition and 7/15/30-day liquidity coverage.
- **债务到期墙**: 12-month principal maturity wall with eligible coverage sources.
- **担保及或有风险**: guarantee exposure by guarantor, beneficiary, type or excess-shareholding status.
- **建议与行动清单**: action status, due-date or amount distribution.

### Detail-table requirements

- Show the records or grouped values needed to reproduce the chart.
- Preserve source identifiers for material debts, facilities, guarantees and actions.
- Keep original currency beside reporting-currency values when cross-currency conversion occurs.
- State totals and coverage so chart/table reconciliation can be checked.

### Top 10 and Other aggregation

Calculate all metrics and risk conclusions from the full validated dataset. Apply Top 10 only to presentation:

- If an applicable display dimension has 10 or fewer valid items, show all items and do not create “其他”.
- If it has more than 10 valid items, show the first 10 and one “其他（N项）” row in both chart and detail table.
- Sum additive balances, principal, interest, limits, exposure and counts from the remaining raw rows.
- Recalculate rates, costs and tenors for “其他” using the applicable raw-row weights. Show “无法计算” when required inputs are incomplete.
- Calculate Top 1, Top 5, Top 10 and HHI from uncollapsed full-data categories. Never treat “其他” as one HHI category.
- Use a stable final tie-breaker such as entity name, facility ID, debt ID or guarantee ID.
- Disclose: “全量 N 项，展示前 10 项，其余 M 项汇总为其他”, the sorting rule, and that all statistics use full data.

Use these domain rankings:

| Analysis | Primary order | Secondary order | Stable tie-breaker |
|---|---|---|---|
| Entity, lender, product, currency | reporting-currency balance descending | share descending | name ascending |
| Individual financing | reporting-currency balance descending | maturity date ascending | debt ID ascending |
| Cost contribution | annualized cost contribution descending; use balance when unavailable | contract rate descending | debt ID ascending |
| Facility | available amount descending | expiry date ascending | facility ID ascending |
| Overdue and repayment | overdue first; otherwise due date ascending | due amount descending | debt ID ascending |
| Guarantee | excess-shareholding or missing-share records first | guarantee exposure descending | guarantee ID ascending |
| Action | P0, P1, P2 | latest completion date ascending | issue/debt ID ascending |

Do not invent missing sort values. Retain the record, use available fields and disclose the limitation.

For time series, preserve chronology instead of ranking by amount. When more than 10 periods are displayed, show the decision-relevant continuous 10 periods and aggregate the remainder as “其他期间（起始期—结束期）”. Full-period calculations and risk judgments remain unchanged.

Risk priority overrides amount ranking. If more than 10 risk-priority records exist, disclose the number, amount and earliest date of risk records inside “其他”; do not silently hide them.

Prefer scripts/top10_aggregation.py for deterministic additive totals, weighted values and full-data HHI when records are locally available.

### Narrative requirements

Conclude after the table using: current state, comparison, cause, impact and recommendation. Separate observed facts from inference. Bind every recommendation to the relevant evidence.

Reflect both available comparison dimensions in relevant operating narratives, not just the KPI table. Two positive comparisons alone do not establish a continuous trend; reserve statements such as `持续上升` for a supporting time series. A zero residual gap means the stated coverage assumptions close the modeled requirement, not that maturity or execution risk has disappeared.

## Action register

Use columns: priority, debt/issue, amount and currency, due date, proposed path, funding source/channel, accountable entity/person, latest completion date, prerequisites, status and backup. Link funding sources to cash accounts, facilities or refinancing arrangements where identifiers are available.

Use only these status meanings:

- `已落实`: documentary or system evidence confirms completion.
- `推进中`: an evidenced process has started but is not complete.
- `待核实`: required confirmation is missing.
- `备用方案`: contingency only; do not count it as committed liquidity.

## Local disclosure after removing the appendix

Do not create standalone data-quality or methodology/source sections. Preserve these disclosures beside the affected content:

- reporting date, consolidation scope, currency, unit and formula coverage for each key metric;
- source/query time, data time, filters, pagination and entity coverage in relevant notes;
- FX rate source/date beside cross-currency tables;
- threshold source beside every qualitative risk label;
- empty, zero, denied, timeout, failure, stale, conflict and partial coverage as distinct states;
- exclusions and source identifiers in table notes or delivery statements.

## Final self-check

1. Remove any fact or number that lacks a tool result or traceable calculation.
2. Distinguish empty, zero, denied, timeout, failure, stale, conflict and partial coverage.
3. Attach date, scope, currency, unit, definition and coverage to key metrics where they appear.
4. Disclose financing-cost fee basis and included-balance coverage.
5. Preserve original currency and dated FX provenance.
6. Stop cross-currency aggregation when a rate is missing.
7. Pair maturity warnings with cash, facility validity/conditions and committed refinancing.
8. Prevent repeated use of one liquidity source.
9. Remove qualitative risk labels without authorized thresholds.
10. Apply evidence gates to 借新还旧, 内部调拨 and 动用授信.
11. Complete every action-register field or label the item `待核实`.
12. Reconcile every section 4-9 chart, detail table and narrative.
13. Keep unconfirmed plans out of committed coverage.
14. Confirm the KPI comparison basis or use `无可比数据`.
15. Confirm that the standard report has no standalone data-quality, visualization or methodology appendix.
16. Disclose locally how data quality limits each affected conclusion.
17. Confirm that every applicable dimension above 10 items uses Top 10 + “其他（N项）” in both chart and table.
18. Confirm that Top 10 changed presentation only and that all totals, weighted metrics, HHI and risk judgments use full data.
