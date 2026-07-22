#!/usr/bin/env python3
"""Inspect a .docx template structurally without executing embedded content."""

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from typing import Dict, List, Optional, Sequence
from xml.etree import ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"w": W_NS, "pr": REL_NS}
W_VAL = "{%s}val" % W_NS
W_GRID_SPAN = "{%s}gridSpan" % W_NS
W_V_MERGE = "{%s}vMerge" % W_NS
PLACEHOLDER_RE = re.compile(r"\{\{[^{}]+\}\}|\$\{[^{}]+\}|\[\[[^\[\]]+\]\]")
HEADING_RE = re.compile(r"(?:heading|标题)\s*([1-9])", re.IGNORECASE)


def _text(element: ET.Element) -> str:
    return "".join(node.text or "" for node in element.findall(".//w:t", NS)).strip()


def _style(paragraph: ET.Element) -> Optional[str]:
    style = paragraph.find("./w:pPr/w:pStyle", NS)
    return style.get(W_VAL) if style is not None else None


def _heading_level(style: Optional[str]) -> Optional[int]:
    if not style:
        return None
    match = HEADING_RE.fullmatch(style.replace("_", " "))
    if match:
        return int(match.group(1))
    compact_match = re.fullmatch(r"Heading([1-9])", style, re.IGNORECASE)
    return int(compact_match.group(1)) if compact_match else None


def _parse_xml(archive: zipfile.ZipFile, member: str) -> ET.Element:
    try:
        return ET.fromstring(archive.read(member))
    except KeyError:
        raise
    except ET.ParseError as exc:
        raise ValueError("Malformed XML in %s: %s" % (member, exc)) from exc


def _inspect_paragraphs(root: ET.Element) -> Dict[str, object]:
    paragraphs: List[Dict[str, object]] = []
    headings: List[Dict[str, object]] = []
    placeholders = set()
    for index, paragraph in enumerate(root.findall(".//w:body/w:p", NS)):
        text = _text(paragraph)
        style = _style(paragraph)
        item = {"index": index, "text": text, "style": style}
        paragraphs.append(item)
        level = _heading_level(style)
        if level and text:
            headings.append({"index": index, "level": level, "text": text, "style": style})
        placeholders.update(PLACEHOLDER_RE.findall(text))
    return {
        "paragraphs": paragraphs,
        "headings": headings,
        "placeholders": sorted(placeholders),
    }


def _inspect_tables(root: ET.Element) -> List[Dict[str, object]]:
    tables: List[Dict[str, object]] = []
    for table_index, table in enumerate(root.findall(".//w:tbl", NS)):
        matrix: List[List[str]] = []
        merged_cells: List[Dict[str, object]] = []
        for row_index, row in enumerate(table.findall("./w:tr", NS)):
            row_values: List[str] = []
            for column_index, cell in enumerate(row.findall("./w:tc", NS)):
                row_values.append(_text(cell))
                grid_span = cell.find("./w:tcPr/w:gridSpan", NS)
                vertical_merge = cell.find("./w:tcPr/w:vMerge", NS)
                if grid_span is not None or vertical_merge is not None:
                    merged_cells.append(
                        {
                            "row": row_index,
                            "column": column_index,
                            "column_span": int(grid_span.get(W_VAL, "1")) if grid_span is not None else 1,
                            "vertical_merge": vertical_merge.get(W_VAL, "continue") if vertical_merge is not None else None,
                        }
                    )
            matrix.append(row_values)
        tables.append(
            {
                "index": table_index,
                "rows": len(matrix),
                "columns": max((len(row) for row in matrix), default=0),
                "headers": matrix[0] if matrix else [],
                "cells": matrix,
                "merged_cells": merged_cells,
            }
        )
    return tables


def _part_texts(archive: zipfile.ZipFile, prefix: str) -> List[str]:
    values: List[str] = []
    for member in sorted(name for name in archive.namelist() if name.startswith(prefix) and name.endswith(".xml")):
        values.append(_text(_parse_xml(archive, member)))
    return values


def _security_warnings(archive: zipfile.ZipFile) -> List[Dict[str, str]]:
    warnings: List[Dict[str, str]] = []
    names = archive.namelist()
    for member in sorted(name for name in names if name.endswith(".rels")):
        root = _parse_xml(archive, member)
        for relationship in root.findall("./pr:Relationship", NS):
            rel_type = relationship.get("Type", "")
            target = relationship.get("Target", "")
            if relationship.get("TargetMode") == "External":
                warnings.append({"type": "external_relationship", "member": member, "target": target})
            if "oleObject" in rel_type or "package" in rel_type or "embeddings/" in target:
                warnings.append({"type": "embedded_object", "member": member, "target": target})
    for member in sorted(name for name in names if name.startswith("word/embeddings/")):
        if not any(item["type"] == "embedded_object" and item.get("target", "").endswith(Path(member).name) for item in warnings):
            warnings.append({"type": "embedded_object", "member": member, "target": member})
    if any(name.lower().endswith("vbaproject.bin") for name in names):
        warnings.append({"type": "macro_project", "member": "word/vbaProject.bin", "target": "not executed"})
    return warnings


def _error(path: Path, error_type: str, message: str) -> Dict[str, object]:
    return {"status": "error", "file_name": path.name, "error_type": error_type, "message": message}


def inspect_docx(path: Path) -> Dict[str, object]:
    path = Path(path)
    if path.suffix.lower() != ".docx":
        raise ValueError("Only .docx templates are supported")
    if not path.is_file():
        return _error(path, "file_not_found", "Template file does not exist or is not readable")

    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            if "EncryptionInfo" in names or "EncryptedPackage" in names:
                return _error(path, "encrypted_document", "Encrypted or password-protected Word templates are unsupported")
            if "word/document.xml" not in names or "[Content_Types].xml" not in names:
                return _error(path, "invalid_docx_structure", "Required OOXML document parts are missing")
            try:
                root = _parse_xml(archive, "word/document.xml")
                paragraph_result = _inspect_paragraphs(root)
                result: Dict[str, object] = {
                    "status": "success",
                    "file_name": path.name,
                    "headings": paragraph_result["headings"],
                    "paragraphs": paragraph_result["paragraphs"],
                    "tables": _inspect_tables(root),
                    "headers": _part_texts(archive, "word/header"),
                    "footers": _part_texts(archive, "word/footer"),
                    "placeholders": paragraph_result["placeholders"],
                    "drawing_count": len(root.findall(".//w:drawing", NS)) + len(root.findall(".//w:pict", NS)),
                    "security_warnings": _security_warnings(archive),
                }
                return result
            except (ET.ParseError, ValueError) as exc:
                return _error(path, "malformed_xml", str(exc))
    except zipfile.BadZipFile:
        return _error(path, "invalid_zip", "File is not a valid OOXML ZIP package")
    except PermissionError:
        return _error(path, "permission_denied", "Template file cannot be read with current permissions")
    except OSError as exc:
        return _error(path, "read_error", str(exc))


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Path to a .docx template")
    parser.add_argument("--pretty", action="store_true", help="Indent JSON output")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        result = inspect_docx(args.path)
    except ValueError as exc:
        result = _error(args.path, "unsupported_format", str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if result.get("status") == "success" else 2


if __name__ == "__main__":
    sys.exit(main())
