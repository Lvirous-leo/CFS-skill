#!/usr/bin/env python3
"""Validate the semantic and presentation structure of a financing report."""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
LEVEL_TWO_RE = re.compile(r"^##(?!#)\s+(.+?)\s*$", re.MULTILINE)
PLACEHOLDER_RE = re.compile(
    r"\{\{[^{}]+\}\}|\$\{[^{}]+\}|\[待填写[^\]]*\]|(?:^|[：:]\s*)(?:TBA|待补充|待填写)(?:\s*$|[，。,;；])",
    re.IGNORECASE | re.MULTILINE,
)
USER_TEMPLATE_RE = re.compile(r"用户模板|模板文件\s*[：:].*\.docx|user\s+template", re.IGNORECASE)
SUPPLEMENT_MARKER = "系统补充章节"
TOP10_RE = re.compile(r"Top\s*10|前\s*10", re.IGNORECASE)
OTHER_RE = re.compile(r"其他[（(]\s*\d+\s*项\s*[）)]")
FULL_COUNT_RE = re.compile(r"全量\s*\d+\s*项")
DISPLAY_COUNT_RE = re.compile(r"展示前\s*10\s*项")
FULL_DATA_RE = re.compile(r"全量数据|全量计算")
SORT_DISCLOSURE_RE = re.compile(r"按.+?(?:升序|降序)")


DEFAULT_ALIASES: Dict[str, List[str]] = {
    "operating_overview": ["融资经营分析总览", "融资经营总览"],
    "template_adaptation": ["模板适配说明", "模板适配"],
    "executive_summary": ["高管决策摘要", "管理层摘要", "执行摘要"],
    "decision_requests": ["需决策或协调事项", "决策事项", "协调事项"],
    "financing_structure": ["融资余额与结构", "融资结构", "债务结构"],
    "cost_rate_risk": ["融资成本与利率风险", "融资成本", "利率风险"],
    "credit_liquidity": ["授信与流动性", "授信分析", "流动性分析"],
    "maturity_wall": ["债务到期墙", "到期墙", "偿债压力"],
    "guarantees": ["担保及或有风险", "担保风险", "或有风险"],
    "action_register": ["建议与行动清单", "行动清单", "融资建议"],
}

REQUIRED_BASE = [
    "operating_overview",
    "executive_summary",
    "decision_requests",
    "financing_structure",
    "cost_rate_risk",
    "credit_liquidity",
    "maturity_wall",
    "guarantees",
    "action_register",
]

ANALYSIS_SECTIONS = [
    "financing_structure",
    "cost_rate_risk",
    "credit_liquidity",
    "maturity_wall",
    "guarantees",
    "action_register",
]

EXECUTIVE_THEMES = {
    "credit_management": "授信经营",
    "financing_management": "融资经营",
    "cost_management": "成本经营",
    "risk_matters": "风险事项",
}

CONTENT_BLOCKS = {
    "chart": "图表",
    "table": "明细表",
    "narrative": "分析说明",
}

REQUIRED_KPI_COLUMNS = [
    "指标含币种单位",
    "本期",
    "环比期",
    "环比变化额",
    "环比变化率",
    "同比期",
    "同比变化额",
    "同比变化率",
    "管理判断",
]


def normalize_heading(value: str) -> str:
    value = value.replace(SUPPLEMENT_MARKER, "")
    value = re.sub(r"[（(][^）)]*[）)]", "", value)
    return re.sub(r"[\s\-—_:：、，,。.;；/]+", "", value).lower()


def normalize_table_cell(value: str) -> str:
    return re.sub(r"[\s\-—_:：、，,。.;；/（）()]+", "", value).lower()


def parse_sections(markdown: str) -> List[Dict[str, object]]:
    matches = list(HEADING_RE.finditer(markdown))
    sections: List[Dict[str, object]] = []
    for index, match in enumerate(matches):
        content_start = match.end()
        content_end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        sections.append(
            {
                "level": len(match.group(1)),
                "title": match.group(2).strip(),
                "content": markdown[content_start:content_end].strip(),
            }
        )
    return sections


def parse_level_two_sections(markdown: str) -> List[Dict[str, str]]:
    matches = list(LEVEL_TWO_RE.finditer(markdown))
    sections: List[Dict[str, str]] = []
    for index, match in enumerate(matches):
        body_end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        sections.append(
            {
                "title": match.group(1).strip(),
                "body": markdown[match.end() : body_end].strip(),
            }
        )
    return sections


def _split_table_row(line: str) -> List[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _is_separator_row(line: str) -> bool:
    cells = _split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def markdown_table_headers(body: str) -> List[List[str]]:
    lines = body.splitlines()
    headers: List[List[str]] = []
    for index, line in enumerate(lines[:-1]):
        if "|" in line and _is_separator_row(lines[index + 1]):
            headers.append(_split_table_row(line))
    return headers


def _merged_aliases(custom: Dict[str, List[str]]) -> Dict[str, List[str]]:
    merged = {key: list(values) for key, values in DEFAULT_ALIASES.items()}
    for key, values in custom.items():
        if key not in merged:
            raise ValueError("Unknown semantic section in aliases: %s" % key)
        if not isinstance(values, list) or not all(isinstance(value, str) and value.strip() for value in values):
            raise ValueError("Aliases for %s must be a non-empty string list" % key)
        merged[key].extend(values)
    return merged


def _semantic_key(title: str, aliases: Dict[str, List[str]]) -> Optional[str]:
    normalized_title = normalize_heading(title)
    matches: List[Tuple[int, str]] = []
    for key, names in aliases.items():
        for name in names:
            normalized_name = normalize_heading(name)
            if normalized_name and normalized_name in normalized_title:
                matches.append((len(normalized_name), key))
    return max(matches)[1] if matches else None


def _first_nonempty_line(content: str) -> str:
    for line in content.splitlines():
        if line.strip():
            return line.strip()
    return ""


def _has_subheading(body: str, title: str) -> bool:
    pattern = r"^#{3,6}\s+(?:\d+(?:\.\d+)*[.、]?\s*)?%s(?:\s|$)" % re.escape(title)
    return bool(re.search(pattern, body, re.MULTILINE))


def _content_block_offset(body: str, title: str) -> Optional[int]:
    pattern = r"^#{3,6}\s+(?:\d+(?:\.\d+)*[.、]?\s*)?%s(?:\s|$)" % re.escape(title)
    match = re.search(pattern, body, re.MULTILINE)
    return match.start() if match else None


def _validate_overview(body: str, errors: List[str]) -> None:
    if not re.search(r"报告基准日|基准日|reporting\s+date", body, re.IGNORECASE):
        errors.append("missing_reporting_date")
    if not re.search(r"币种|本位币|currency", body, re.IGNORECASE):
        errors.append("missing_currency")
    if not re.search(r"单位|unit", body, re.IGNORECASE):
        errors.append("missing_unit")


def _validate_executive_summary(body: str, errors: List[str]) -> None:
    for key, title in EXECUTIVE_THEMES.items():
        if not _has_subheading(body, title):
            errors.append("missing_executive_theme:%s" % key)
            continue
        theme = re.search(
            r"^#{3,6}\s+(?:\d+(?:\.\d+)*[.、]?\s*)?%s\s*\n(.*?)(?=^#{3,6}\s|\Z)" % re.escape(title),
            body, re.MULTILINE | re.DOTALL,
        )
        points = re.findall(r"^\s*(\d+)[.、]\s+\S", theme.group(1), re.MULTILINE) if theme else []
        if not points:
            errors.append("missing_numbered_executive_points:%s" % key)
        elif [int(n) for n in points] != list(range(1, len(points) + 1)):
            errors.append("invalid_executive_numbering:%s" % key)

    headers = markdown_table_headers(body)
    kpi_header = next(
        (
            header
            for header in headers
            if any("指标" in normalize_table_cell(cell) for cell in header)
        ),
        None,
    )
    if kpi_header is None:
        errors.append("missing_kpi_table")
        return

    normalized = [normalize_table_cell(cell) for cell in kpi_header]
    if not all(required in normalized for required in REQUIRED_KPI_COLUMNS):
        errors.append("invalid_kpi_columns")
    if any("定义" in cell or "覆盖" in cell for cell in normalized):
        errors.append("legacy_kpi_column:definition_coverage")


def _validate_analysis_layout(body: str, semantic_key: str, errors: List[str]) -> None:
    offsets: Dict[str, Optional[int]] = {}
    for block_key, title in CONTENT_BLOCKS.items():
        offsets[block_key] = _content_block_offset(body, title)
        if offsets[block_key] is None:
            errors.append("missing_content_block:%s:%s" % (semantic_key, block_key))

    if all(offset is not None for offset in offsets.values()):
        if not offsets["chart"] < offsets["table"] < offsets["narrative"]:
            errors.append("invalid_content_order:%s" % semantic_key)


def _validate_top10_disclosure(body: str, semantic_key: str, errors: List[str]) -> None:
    if not TOP10_RE.search(body):
        return
    checks = (
        OTHER_RE.search(body),
        FULL_COUNT_RE.search(body),
        DISPLAY_COUNT_RE.search(body),
        FULL_DATA_RE.search(body),
        SORT_DISCLOSURE_RE.search(body),
    )
    if not all(checks):
        errors.append("incomplete_top10_disclosure:%s" % semantic_key)


def validate_report(markdown: str, aliases: Dict[str, List[str]]) -> Dict[str, object]:
    if not isinstance(markdown, str):
        raise TypeError("markdown must be a string")
    merged_aliases = _merged_aliases(aliases)
    level_two_sections = parse_level_two_sections(markdown)
    detected: Dict[str, Dict[str, str]] = {}
    warnings: List[str] = []
    errors: List[str] = []

    for section in level_two_sections:
        key = _semantic_key(section["title"], merged_aliases)
        if key:
            if key in detected:
                warnings.append("duplicate_section:%s" % key)
            else:
                detected[key] = section

    required = list(REQUIRED_BASE)
    uses_user_template = bool(USER_TEMPLATE_RE.search(markdown))
    if uses_user_template:
        required.append("template_adaptation")
    missing_sections = [key for key in required if key not in detected]

    if PLACEHOLDER_RE.search(markdown):
        errors.append("unresolved_placeholder")

    overview = detected.get("operating_overview")
    if overview:
        _validate_overview(overview["body"], errors)

    executive = detected.get("executive_summary")
    if executive:
        _validate_executive_summary(executive["body"], errors)

    for semantic_key in ANALYSIS_SECTIONS:
        section = detected.get(semantic_key)
        if section:
            _validate_analysis_layout(section["body"], semantic_key, errors)
            _validate_top10_disclosure(section["body"], semantic_key, errors)

    adaptation = detected.get("template_adaptation")
    adaptation_text = ""
    if adaptation:
        adaptation_text = "%s\n%s" % (adaptation["title"], adaptation["body"])
    for key, section in detected.items():
        first_line = _first_nonempty_line(section["body"])
        is_supplemented = SUPPLEMENT_MARKER in section["title"] or SUPPLEMENT_MARKER in first_line
        if not is_supplemented:
            continue
        if not uses_user_template:
            warnings.append("supplement_marker_without_user_template:%s" % key)
        aliases_for_section = merged_aliases.get(key, []) + [section["title"]]
        disclosed = any(
            normalize_heading(name) in normalize_heading(adaptation_text)
            for name in aliases_for_section
            if normalize_heading(name)
        )
        if not adaptation or not disclosed:
            errors.append("missing_adaptation_disclosure:%s" % key)

    errors = list(dict.fromkeys(errors))
    warnings = list(dict.fromkeys(warnings))
    return {
        "valid": not errors and not missing_sections,
        "missing_sections": missing_sections,
        "errors": errors,
        "warnings": warnings,
        "detected_sections": sorted(detected.keys()),
        "uses_user_template": uses_user_template,
    }


def _load_aliases(path: Optional[Path]) -> Dict[str, List[str]]:
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Alias JSON must be an object")
    return data


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="Markdown financing report")
    parser.add_argument("--aliases", type=Path, help="JSON map of semantic keys to heading aliases")
    parser.add_argument("--pretty", action="store_true", help="Indent JSON output")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        markdown = args.report.read_text(encoding="utf-8")
        aliases = _load_aliases(args.aliases)
        result = validate_report(markdown, aliases)
    except (OSError, UnicodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
        result = {"valid": False, "error_type": "input_error", "message": str(exc)}
        print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
