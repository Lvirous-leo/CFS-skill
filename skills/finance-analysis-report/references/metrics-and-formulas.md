# Metrics and Formulas

For every metric disclose reporting date, scope, currency, unit, required inputs, formula, excluded records, and included-balance coverage. If a required field is missing or a denominator is zero, report `无法计算` and the reason.

## Financing balance and structure

`financing_total = Σ valid outstanding balance converted to reporting currency`

Show balance and share by entity, lender, product, currency, region, tenor, and fixed/floating rate. Retain original-currency values. Exclude an FX-missing currency from reporting-currency totals and disclose the excluded original amount.

## Weighted all-in financing cost

`weighted_all_in_cost = Σ(balance_i × annualized_all_in_cost_i) ÷ Σ(balance_i)`

Define whether each instrument cost includes contract interest, fees, underwriting, guarantees, hedging, and other charges. Do not combine incomparable cost bases. Separate interest and other costs when harmonization is unavailable. Disclose included financing balance and its share of total financing.

For floating debt, show benchmark plus spread, current observation date, next reset, cap/floor, and hedge status. Do not assume future LPR, SOFR, HIBOR, or any other benchmark.

## Credit facilities

- `effective_total_credit = facilities valid on the reporting date under the group definition`
- `credit_utilization = used_credit ÷ effective_total_credit`
- `derived_available_credit = effective_total_credit − used_credit − restricted_or_unavailable_credit`

Show direct system-available and derived available values together. Explain differences rather than overwriting either one. For liquidity coverage, use only facilities that remain valid through the target date, match or can convert currency, have satisfiable draw conditions, and meet the group definition of committed/drawable credit.

## Concentration

- `top_one_share = largest category balance ÷ total financing balance`
- `top_five_share = sum of five largest category balances ÷ total financing balance`
- `HHI = Σ(category_share_i²)`

State whether HHI uses a 0–1 or 0–10,000 scale. Calculate lender, product, entity, and currency concentration where inputs are complete. Apply qualitative labels only with authorized thresholds.

## Period flows

### Historical comparisons

- Retain a dated snapshot for each current, month-on-month and year-on-year base, with consistent entity scope, currency/FX policy and metric definition.
- `absolute_change = current − comparison`; `relative_change = absolute_change ÷ comparison` for a positive comparison base. If the base is confirmed zero, show the amount change and `不适用（基期为0）` for the rate. Missing is `无可比数据`, not zero. Explain any negative-base convention before calculating a relative rate.
- For rates stored as fractions, percentage-point change is `(current − comparison) × 100` and BP change is `(current − comparison) × 10000`. If stored as percentage numbers, use the difference directly for percentage points and multiply by 100 for BP. Never mix storage conventions.
- Preserve source precision through all calculations and round only for display; the workbook, chart, KPI table and narrative must share the same calculation inputs.
- For stocks, label the exact as-of dates. A midmonth-to-prior-month-end comparison must be labeled as such, not represented as two completed months. For flows, compare equivalent durations (for example month-to-date against the same elapsed prior-month/prior-year interval), not a partial month against a full month.
- Historical maturity and availability metrics require what was known and eligible at each historical date; do not back-project today's repayment or facility status as historical truth.

- Weekly new financing uses actual draw/start date within the configured period and valid status under the group definition.
- Weekly repayment uses actual principal payment date within the period. Show interest separately.
- A scheduled payment without actual-payment status is not a completed repayment.

Reconcile opening balance, draws, principal repayments, FX movement, restructuring or scope movement, and closing balance when these components are available.

## Near-term maturities and maturity wall

Aggregate unpaid principal and reliably available interest for the next 7, 15, and 30 calendar days from the reporting date, unless the group specifies a different day convention. Build at least 12 monthly buckets thereafter. Show principal and interest separately. Show overdue unpaid debt separately, and list debt with missing maturity dates as excluded coverage.

## Guarantees

`guarantee_balance = remaining responsibility on guarantees effective at the reporting date`

Separate contractual maximum from remaining exposure. Calculate excess-shareholding guarantees only using the group formula, ownership percentage, and responsibility allocation. If any is missing, show guarantee exposure but report excess-shareholding guarantee as `无法计算`.

## Cash-debt ratio

Use only the group-provided numerator and denominator. Without that definition, show available cash and relevant debt base components but do not label a self-selected ratio as “现金负债比”.

## Multi-currency rules

- Show original currency and reporting currency together.
- Use the approved rate source, rate type, date, and conversion direction.
- Use reporting-date rates for stocks and the approved accounting/management rate for period flows.
- Never add different currencies without valid conversion rates.
- Separate currency exposure, natural hedge, and derivative hedge. Do not claim coverage when operating cash-flow or hedge data is absent.
