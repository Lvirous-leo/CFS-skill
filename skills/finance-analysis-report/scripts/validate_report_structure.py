#!/usr/bin/env python3
"""Validate semantic sections and supplementation markers in a financing report."""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
PLACEHOLDER_RE = re.compile(
    r"\{\{[^{}]+\}\}|\$\{[^{}]+\}|\[待填写[^\]]*\]|(?:^|[：:]\s*)(?:TBA|待补充|待填写)(?:\s*$|[，。,;；])",
    re.IGNORECASE | re.MULTILINE,
)
USER_TEMPLATE_RE = re.compile(r"用户模板|模板文件\s*[：:].*\.docx|user\s+template", re.IGNORECASE)
SUPPLEMENT_MARKER = "系统补充章节"


DEFAULT_ALIASES: Dict[str, List[str]] = {
    "metadata_data_quality": ["报告信息与数据质量", "报告信息", "数据质量"],
    "template_adaptation": ["模板适配说明", "模板适配"],
    "executive_summary": ["高管决策摘要", "管理层摘要", "执行摘要"],
    "decision_requests": ["需决策或协调事项", "决策事项", "协调事项"],
    "financing_structure": ["融资余额与结构", "融资结构", "债务结构"],
    "cost_rate_risk": ["融资成本与利率风险", "融资成本", "利率风险"],
    "credit_liquidity": ["授信与流动性", "授信分析", "流动性分析"],
    "maturity_wall": ["债务到期墙", "到期墙", "偿债压力"],
    "guarantees": ["担保及或有风险", "担保风险", "或有风险"],
    "action_register": ["建议与行动清单", "行动清单", "融资建议"],
    "charts": ["可视化图表", "图表", "可视化"],
    "methodology_sources": ["方法、来源与数据限制附录", "方法与来源", "数据限制附录"],
}

REQUIRED_BASE = [
    "metadata_data_quality",
    "executive_summary",
    "decision_requests",
    "financing_structure",
    "cost_rate_risk",
    "credit_liquidity",
    "maturity_wall",
    "guarantees",
    "action_register",
    "charts",
    "methodology_sources",
]


def normalize_heading(value: str) -> str:
    value = value.replace(SUPPLEMENT_MARKER, "")
    value = re.sub(r"[（(][^）)]*[）)]", "", value)
    return re.sub(r"[\s\-—_:：、，,。.;；/]+", "", value).lower()


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


def validate_report(markdown: str, aliases: Dict[str, List[str]]) -> Dict[str, object]:
    if not isinstance(markdown, str):
        raise TypeError("markdown must be a string")
    merged_aliases = _merged_aliases(aliases)
    sections = parse_sections(markdown)
    detected: Dict[str, Dict[str, object]] = {}
    warnings: List[str] = []
    errors: List[str] = []

    for section in sections:
        key = _semantic_key(str(section["title"]), merged_aliases)
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

    metadata = detected.get("metadata_data_quality")
    if metadata:
        metadata_text = "%s\n%s" % (metadata["title"], metadata["content"])
        if not re.search(r"报告基准日|基准日|reporting\s+date", metadata_text, re.IGNORECASE):
            errors.append("missing_reporting_date")
        if not re.search(r"币种|本位币|currency", metadata_text, re.IGNORECASE):
            errors.append("missing_currency")
        if not re.search(r"单位|unit", metadata_text, re.IGNORECASE):
            errors.append("missing_unit")

    adaptation = detected.get("template_adaptation")
    adaptation_text = ""
    if adaptation:
        adaptation_text = "%s\n%s" % (adaptation["title"], adaptation["content"])
    for key, section in detected.items():
        first_line = _first_nonempty_line(str(section["content"]))
        is_supplemented = SUPPLEMENT_MARKER in str(section["title"]) or SUPPLEMENT_MARKER in first_line
        if not is_supplemented:
            continue
        if not uses_user_template:
            warnings.append("supplement_marker_without_user_template:%s" % key)
        aliases_for_section = merged_aliases.get(key, []) + [str(section["title"])]
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
