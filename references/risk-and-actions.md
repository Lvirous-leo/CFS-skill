# Risk Assessment and Action Rules

## Threshold hierarchy

Apply, in order:

1. Formal group risk appetite or treasury policy.
2. Thresholds injected for the current run.
3. Objective values, rankings, trends, and gaps without high/medium/low labels.

Identify the threshold source in the report. Do not introduce industry thresholds unless the user explicitly requests and authorizes a benchmark comparison distinct from group risk classification.

## Maturity wall and liquidity closure

For 7/15/30 days and at least 12 monthly buckets, show principal, reliably available interest, share of total financing, eligible cash, unconditionally drawable credit, committed refinancing, total coverage, and residual gap.

- `eligible_coverage = drawable_cash + unconditionally_drawable_credit + committed_refinancing_available_before_due_date`
- `residual_gap = maturity_principal_and_included_interest − eligible_coverage`

Distinguish gross maturity pressure from residual uncovered pressure. Do not call a large maturity uncontrollable when eligible coverage closes it.

Exclude restricted or trapped cash, facilities expiring before the debt due date, unmet draw conditions, revocable limits outside the group definition, currency-incompatible funds without a conversion path, and financing that is only discussed or “principally agreed.”

Allocate each liquidity source once. For cumulative windows, subtract resources already assigned to earlier debt or state a documented allocation order. Do not double-count the same cash, facility, or refinancing across debts or periods.

## Other risk dimensions

Assess lender, product, entity, currency and tenor concentration; fixed/floating structure and reset timing; facility utilization, expiry and conditions; guarantees, excess-shareholding exposure and contingent calls; term and currency mismatch; and data quality.

Tie every risk statement to facts, thresholds, coverage and remaining uncertainty.

## Action evidence gates

Every action must include: linked debt or issue, amount, currency, due date, funding source or channel, accountable entity/person, latest completion date, prerequisites, current status, and backup.

### 借新还旧

Recommend only when a viable channel exists, approval/facility path is identifiable, expected proceeds precede maturity, currency is matched or convertible, and cost, tenor and security are acceptable. Count it as coverage only when committed and key conditions are met.

### 内部调拨

Recommend only when internal cash is genuinely drawable by the target date after restrictions, minority interests, tax, FX, cross-border pooling, related-party and governance constraints. A subsidiary cash balance is not automatically group-drawable cash.

### 动用授信

Recommend only when the facility remains valid, amount is actually available, draw conditions can be met, currency is usable, and proceeds can arrive before maturity. Disclose commitment, revocability, cost, conditions and future facility headroom.

## Status vocabulary

- `已落实`: signed or approved, key conditions met, amount and timing verifiable.
- `推进中`: owner and milestones exist, but some conditions remain.
- `待核实`: critical facts or conditions are missing.
- `备用方案`: activated only if the primary path fails.

Never describe `推进中` or `待核实` funding as committed liquidity.
