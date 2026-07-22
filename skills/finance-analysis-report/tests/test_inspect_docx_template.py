import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from inspect_docx_template import inspect_docx  # noqa: E402


DOCUMENT_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
 xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <w:body>
    <w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>融资分析</w:t></w:r></w:p>
    <w:p><w:r><w:t>基准日：{{报告基准日}}</w:t></w:r><w:drawing><a:graphic/></w:drawing></w:p>
    <w:tbl>
      <w:tr><w:tc><w:p><w:r><w:t>指标</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>金额</w:t></w:r></w:p></w:tc></w:tr>
      <w:tr><w:tc><w:p><w:r><w:t>融资余额</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>100</w:t></w:r></w:p></w:tc></w:tr>
    </w:tbl>
  </w:body>
</w:document>
"""

HEADER_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:p><w:r><w:t>集团资金管理部</w:t></w:r></w:p>
</w:hdr>
"""

CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"""

RISKY_RELS_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" Target="https://example.com" TargetMode="External"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/oleObject" Target="embeddings/oleObject1.bin"/>
</Relationships>
"""


def write_docx(path: Path, *, risky: bool = False, include_document: bool = True) -> None:
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("[Content_Types].xml", CONTENT_TYPES_XML)
        if include_document:
            archive.writestr("word/document.xml", DOCUMENT_XML)
            archive.writestr("word/header1.xml", HEADER_XML)
        if risky:
            archive.writestr("word/_rels/document.xml.rels", RISKY_RELS_XML)
            archive.writestr("word/embeddings/oleObject1.bin", b"not executed")
            archive.writestr("word/vbaProject.bin", b"not executed")


class InspectDocxTemplateTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir_context = tempfile.TemporaryDirectory()
        self.temp_dir = Path(self.temp_dir_context.name)

    def tearDown(self):
        self.temp_dir_context.cleanup()

    def test_extracts_headings_tables_headers_drawings_and_placeholders(self):
        sample_docx = self.temp_dir / "sample.docx"
        write_docx(sample_docx)

        result = inspect_docx(sample_docx)

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["headings"][0]["text"], "融资分析")
        self.assertEqual(result["headings"][0]["level"], 1)
        self.assertEqual(result["tables"][0]["rows"], 2)
        self.assertEqual(result["tables"][0]["columns"], 2)
        self.assertEqual(result["tables"][0]["headers"], ["指标", "金额"])
        self.assertIn("{{报告基准日}}", result["placeholders"])
        self.assertIn("集团资金管理部", result["headers"])
        self.assertEqual(result["drawing_count"], 1)

    def test_rejects_non_docx_suffix(self):
        invalid_path = self.temp_dir / "template.pdf"
        invalid_path.write_bytes(b"pdf")

        with self.assertRaisesRegex(ValueError, "Only .docx"):
            inspect_docx(invalid_path)

    def test_reports_missing_document_xml(self):
        broken_docx = self.temp_dir / "broken.docx"
        write_docx(broken_docx, include_document=False)

        result = inspect_docx(broken_docx)

        self.assertEqual(result["status"], "error")
        self.assertEqual(result["error_type"], "invalid_docx_structure")

    def test_reports_corrupt_zip(self):
        corrupt_docx = self.temp_dir / "corrupt.docx"
        corrupt_docx.write_bytes(b"not a zip")

        result = inspect_docx(corrupt_docx)

        self.assertEqual(result["status"], "error")
        self.assertEqual(result["error_type"], "invalid_zip")

    def test_flags_external_embedded_and_macro_content(self):
        risky_docx = self.temp_dir / "risky.docx"
        write_docx(risky_docx, risky=True)

        result = inspect_docx(risky_docx)
        warning_types = {item["type"] for item in result["security_warnings"]}

        self.assertIn("external_relationship", warning_types)
        self.assertIn("embedded_object", warning_types)
        self.assertIn("macro_project", warning_types)

    def test_cli_prints_json_and_returns_parse_error_code(self):
        broken_docx = self.temp_dir / "broken.docx"
        write_docx(broken_docx, include_document=False)

        completed = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / "inspect_docx_template.py"), str(broken_docx)],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(completed.returncode, 2)
        self.assertEqual(json.loads(completed.stdout)["error_type"], "invalid_docx_structure")


if __name__ == "__main__":
    unittest.main()
