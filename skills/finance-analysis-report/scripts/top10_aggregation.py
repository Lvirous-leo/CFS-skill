#!/usr/bin/env python3
"""Build Top-N display rows while retaining full-data financial calculations."""

from decimal import Decimal
from typing import Any, Callable, Dict, Iterable, Mapping, Optional, Sequence, Tuple


def _decimal(value: Any) -> Decimal:
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def aggregate_top_n(
    records: Iterable[Mapping[str, Any]],
    *,
    label_field: str,
    additive_fields: Sequence[str],
    sort_key: Callable[[Mapping[str, Any]], Any],
    weighted_fields: Optional[Mapping[str, Tuple[str, str]]] = None,
    limit: int = 10,
) -> Dict[str, Any]:
    """Return sorted display rows, an optional Other row, and full-data totals.

    The caller supplies a domain-aware stable sort key whose final component
    should be a unique identifier or label. Missing required values raise
    instead of being interpreted as zero.
    """

    if limit < 1:
        raise ValueError("limit must be positive")

    rows = [dict(record) for record in records]
    weighted_fields = weighted_fields or {}
    ordered = sorted(rows, key=sort_key)
    full_totals = {
        field: sum((_decimal(row[field]) for row in rows), Decimal(0))
        for field in additive_fields
    }

    top_rows = ordered[:limit]
    other_rows = ordered[limit:]
    display_rows = list(top_rows)

    if other_rows:
        other: Dict[str, Any] = {label_field: "其他（%d项）" % len(other_rows)}
        for field in additive_fields:
            other[field] = sum((_decimal(row[field]) for row in other_rows), Decimal(0))
        for output_field, (value_field, weight_field) in weighted_fields.items():
            denominator = sum(
                (_decimal(row[weight_field]) for row in other_rows),
                Decimal(0),
            )
            other[output_field] = (
                sum(
                    (
                        _decimal(row[value_field]) * _decimal(row[weight_field])
                        for row in other_rows
                    ),
                    Decimal(0),
                )
                / denominator
                if denominator
                else None
            )
        display_rows.append(other)

    return {
        "display_rows": display_rows,
        "full_count": len(rows),
        "top_count": min(len(rows), limit),
        "other_count": len(other_rows),
        "full_totals": full_totals,
    }


def full_data_hhi(records: Iterable[Mapping[str, Any]], value_field: str) -> Decimal:
    """Calculate HHI from uncollapsed full-data categories."""

    values = [_decimal(row[value_field]) for row in records]
    if any(value < 0 for value in values):
        raise ValueError("HHI values must be non-negative")
    total = sum(values, Decimal(0))
    if total == 0:
        raise ValueError("HHI total must be non-zero")
    return sum(((value / total) ** 2 for value in values), Decimal(0))
