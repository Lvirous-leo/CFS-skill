# Data Integrity and Tool Query Rules

## Runtime parameters

Establish: reporting date, analysis period, consolidation scope, reporting currency, FX source and dates, amount unit, group metric definitions, risk thresholds, historical comparison period, timezone, and tool mappings.

Use this priority: explicit user value, system-injected value, tool-returned value, disclosed missing parameter. Never infer a missing parameter from convention.

## Query domains

Query and retain stable identifiers for:

1. Financing contracts and current balances: borrower, lender, product, currency, contract amount, balance, start and maturity dates, rate structure, benchmark, spread, reset date, cap/floor, fees, security, purpose, and status.
2. Repayment schedules: debt ID, principal/interest, currency, due date, paid/overdue status, and schedule version.
3. Credit facilities: agreement, entity, bank, currency, total/used/restricted/system-available limits, validity, conditions, commitment, revocability, and status.
4. Cash and liquidity: entity, account, currency, cash, restricted or trapped cash, drawable date, and transfer constraints.
5. Guarantees: guarantee ID, guarantor, beneficiary, guaranteed party, amount/remaining exposure, currency, responsibility, dates, linked debt, counter-guarantee, ownership percentage, approval status, and facility usage.
6. FX and benchmarks: rate, direction, rate type, date, source, and LPR/SOFR/HIBOR observations.
7. Master data: entity hierarchy, ownership, consolidation flag, normalized institution, product class, currency, and region.

## Query metadata

Retain source, query time, data time, filters, entity coverage, currency, unit, pagination status, and return status for every query.

Distinguish:

- success with records;
- success with an empty result;
- confirmed numeric zero;
- permission denied;
- timeout;
- tool or interface failure.

Treat a successful empty result as unknown unless the source contract explicitly defines it as a confirmed zero. Never substitute zero, prior-period data, market memory, or a reasonable assumption for a missing fact.

## Validation

- Confirm reporting date, entity scope, currency, unit, data freshness, page completeness, and stable identifiers.
- Detect duplicate contracts, negative or malformed balances, missing currencies or maturity dates, expired debt with balance, and unmapped entities or institutions.
- Link repayment, facility, guarantee, and cash records using stable identifiers where available.
- Compare repayment principal with financing balance and explain version or scope differences.
- Compare facility total, used, restricted, direct available, and derived available amounts without assuming they must reconcile.
- Do not assume facility usage equals financing balance; letters of credit, guarantees, bills, and other products may create valid differences.
- Treat missing maturity dates as a maturity-analysis coverage gap while retaining the debt in total balance.
- Check consolidation and internal elimination rules before removing intercompany financing, guarantees, or transfers.

## Conflicts and partial coverage

When sources conflict, show each value and its provenance, quantify the difference, and limit affected conclusions. Do not select the favorable or adverse value without an authorized source hierarchy.

When data covers only part of the group, state the included entities and denominator. Avoid “group total,” “no exposure,” and “no risk” claims unless full coverage is verified.

Calculate valid subsets only when the subset and excluded balance are disclosed. Required-field absence yields “无法计算,” not a zero or estimated value.

## Traceability

Every reported fact must trace to a tool result. Every derived value must trace to source fields, the applied formula, currency conversion, reporting date, and included population. Retain financing, facility, guarantee, and entity IDs in the appendix where allowed.
