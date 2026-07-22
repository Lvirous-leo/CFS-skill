import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from validate_report_structure import validate_report  # noqa: E402


COMPLETE_REPORT = """# 集团债务与融资分析报告

## 报告信息与数据质量
报告基准日：2026-07-22；币种：人民币；单位：万元；数据范围：集团主体。

## 高管决策摘要
总体判断基于已查询范围。

## 需决策或协调事项
无。

## 融资余额与结构
按机构和品种展示。

## 融资成本与利率风险
展示全口径成本。

## 授信与流动性
展示可用授信和现金。

## 债务到期墙
展示未来十二个月到期金额与覆盖。

## 担保及或有风险
展示担保余额。

## 建议与行动清单
列示责任主体和时限。

## 可视化图表
提供图表数据。

## 方法、来源与数据限制附录
列示工具来源和计算公式。
"""

REPORT_WITHOUT_MATURITY_WALL = COMPLETE_REPORT.replace(
    "## 债务到期墙\n展示未来十二个月到期金额与覆盖。\n\n", ""
)

REPORT_WITH_ALIASES = COMPLETE_REPORT.replace("## 债务到期墙", "## 偿债高峰分析")

USER_TEMPLATE_WITH_DISCLOSED_ADDITION = """# 集团债务与融资分析报告

## 报告信息与数据质量
用户模板：custom.docx；报告基准日：2026-07-22；币种：人民币；单位：万元。

## 模板适配说明
系统补充章节：债务到期墙。补充原因：原模板缺失。

## 高管决策摘要
总体判断。

## 需决策或协调事项
无。

## 融资余额与结构
结构分析。

## 融资成本与利率风险
成本分析。

## 授信与流动性
授信分析。

## 债务到期墙（系统补充章节）
到期覆盖分析。

## 担保及或有风险
担保分析。

## 建议与行动清单
行动分析。

## 可视化图表
图表数据。

## 方法、来源与数据限制附录
方法和来源。
"""

REPORT_WITH_UNDISCLOSED_ADDED_SECTION = USER_TEMPLATE_WITH_DISCLOSED_ADDITION.replace(
    "系统补充章节：债务到期墙。补充原因：原模板缺失。", "系统补充章节：无。"
)


class ValidateReportStructureTests(unittest.TestCase):
    def test_complete_standard_report_passes(self):
        result = validate_report(COMPLETE_REPORT, aliases={})

        self.assertTrue(result["valid"])
        self.assertEqual(result["missing_sections"], [])
        self.assertEqual(result["errors"], [])

    def test_missing_maturity_wall_fails(self):
        result = validate_report(REPORT_WITHOUT_MATURITY_WALL, aliases={})

        self.assertFalse(result["valid"])
        self.assertIn("maturity_wall", result["missing_sections"])

    def test_added_section_requires_adaptation_disclosure(self):
        result = validate_report(REPORT_WITH_UNDISCLOSED_ADDED_SECTION, aliases={})

        self.assertFalse(result["valid"])
        self.assertIn("missing_adaptation_disclosure:maturity_wall", result["errors"])

    def test_added_section_with_two_markers_passes(self):
        result = validate_report(USER_TEMPLATE_WITH_DISCLOSED_ADDITION, aliases={})

        self.assertTrue(result["valid"])

    def test_alias_map_satisfies_semantic_section(self):
        result = validate_report(REPORT_WITH_ALIASES, aliases={"maturity_wall": ["偿债高峰分析"]})

        self.assertNotIn("maturity_wall", result["missing_sections"])
        self.assertTrue(result["valid"])

    def test_unresolved_curly_placeholder_fails(self):
        result = validate_report(COMPLETE_REPORT + "\n{{融资总余额}}", aliases={})

        self.assertIn("unresolved_placeholder", result["errors"])
        self.assertFalse(result["valid"])

    def test_user_template_requires_adaptation_statement(self):
        report = COMPLETE_REPORT.replace(
            "报告基准日：2026-07-22", "用户模板：custom.docx；报告基准日：2026-07-22"
        )

        result = validate_report(report, aliases={})

        self.assertIn("template_adaptation", result["missing_sections"])

    def test_cli_uses_alias_json_and_returns_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            report_path = temp_path / "report.md"
            aliases_path = temp_path / "aliases.json"
            report_path.write_text(REPORT_WITH_ALIASES, encoding="utf-8")
            aliases_path.write_text(
                json.dumps({"maturity_wall": ["偿债高峰分析"]}, ensure_ascii=False),
                encoding="utf-8",
            )

            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_DIR / "validate_report_structure.py"),
                    str(report_path),
                    "--aliases",
                    str(aliases_path),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(completed.returncode, 0)
        self.assertTrue(json.loads(completed.stdout)["valid"])


if __name__ == "__main__":
    unittest.main()
