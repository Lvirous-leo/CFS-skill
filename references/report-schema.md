# Financing Analysis Report Schema

Use a dual-layer report: executive decision information first, then finance-team evidence, detail, and actions. If a user Word template is active, map its headings to these semantic modules and preserve every required module.

## Required modules

1. **报告信息与数据质量**: report date, period, scope, reporting currency, unit, timezone, source/query times, coverage, return-state summary, formulas, FX and threshold sources, and limitations.
2. **模板适配说明**: required only when a user template is used; list template identity, parsing state, retained sections, system additions, local style fallback, ambiguity, and ignored unsafe objects.
3. **高管决策摘要**: overall judgment in no more than three sentences, core KPI table, three to five material concerns, coverage measures, residual issues.
4. **需决策或协调事项**: approval or cross-entity/external coordination, latest decision date, and consequence of delay.
5. **融资余额与结构**: entity, lender, product, currency, tenor, fixed/floating structure, concentration, weekly flows, anomalies.
6. **融资成本与利率风险**: weighted cost, cost coverage, fee basis, fixed/floating split, LPR/SOFR/HIBOR exposure and reset timing.
7. **授信与流动性**: effective, used, restricted, direct available, derived available, utilization, facility expiry/conditions, and 7/15/30-day coverage.
8. **债务到期墙**: overdue items, 12-month principal/interest, concentration, eligible coverage, residual gap, actions and backups.
9. **担保及或有风险**: remaining exposure, contractual cap, parties, responsibility, dates, counter-guarantee, excess-shareholding status, potential calls and facility use.
10. **建议与行动清单**: evidence-bound recommendations and accountable execution fields.
11. **可视化图表**: structure, maturity/coverage, facility composition, cost trend when comparable, and concentration.
12. **方法、来源与数据限制附录**: formulas, FX, units, tool metadata, conflicts, exclusions, IDs and traceability.

## Executive KPI table

Include financing total, weighted financing cost, 30-day maturities, unconditionally available credit, 30-day residual coverage/gap, and guarantee balance. Columns: current, comparison, change, currency/unit, definition/coverage. Use `无可比数据` when comparable history is unavailable.

## Action register

Use columns: priority, debt/issue, amount and currency, due date, proposed path, accountable entity/person, latest completion date, prerequisites, status, backup.

## Charts

Generate only from validated data:

- financing structure stacked bar; use a donut only for few clear categories;
- 12-month maturity wall with eligible coverage;
- effective/used/restricted/available facility composition;
- financing cost and benchmark trend only with comparable history;
- lender, entity, product or currency concentration.

Every chart must show title, unit, currency basis, reporting date, coverage and limitations. Reconcile chart values to tables. If rendering is unavailable, provide structured chart data and the recommended chart type. Never create illustrative values.

## Final self-check

1. Remove any fact or number that lacks a tool result or traceable calculation.
2. Distinguish empty, zero, denied, timeout, failure, stale, conflict and partial coverage.
3. Attach date, scope, currency, unit, definition and coverage to key metrics.
4. Disclose financing-cost fee basis and included-balance coverage.
5. Preserve original currency and dated FX provenance.
6. Stop cross-currency aggregation when a rate is missing.
7. Pair maturity warnings with cash, facility validity/conditions, and committed refinancing.
8. Prevent repeated use of one liquidity source.
9. Remove qualitative risk labels without authorized thresholds.
10. Apply evidence gates to 借新还旧, 内部调拨 and 动用授信.
11. Complete every required action-register field or label the item `待核实`.
12. Reconcile charts and tables and remove illustrative data.
13. Keep unconfirmed plans out of committed coverage.
14. Disclose how data quality limits the conclusions.
