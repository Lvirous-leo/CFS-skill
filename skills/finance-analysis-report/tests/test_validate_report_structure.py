import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from validate_report_structure import validate_report  # noqa: E402


ANALYSIS_BLOCKS = """### 图表
结构图。

### 明细表
| 项目 | 金额 |
|---|---:|
| 示例 | 1 |

### 分析说明
现状、变化、原因、影响和建议。
"""

COMPLETE_REPORT = f"""# 集团债务与融资分析报告

## 1. 融资经营分析总览
报告基准日：2026-08-14；汇总币种：人民币；单位：万元；数据范围：集团主体。

## 2. 高管决策摘要
### 授信经营
1. 现状、变化、影响和管理动作。

### 融资经营
1. 现状、变化、影响和管理动作。

### 成本经营
1. 现状、变化、影响和管理动作。

### 风险事项
1. 现状、变化、影响和管理动作。

| 指标（含币种/单位） | 本期 | 环比期 | 环比变化额 | 环比变化率 | 同比期 | 同比变化额 | 同比变化率 | 管理判断 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 融资余额（人民币万元） | 270260 | 无可比数据 | 无可比数据 | 无可比数据 | 无可比数据 | 无可比数据 | 无可比数据 | 保持关注 |

## 3. 需决策或协调事项
无。

## 4. 融资余额与结构
{ANALYSIS_BLOCKS}

## 5. 融资成本与利率风险
{ANALYSIS_BLOCKS}

## 6. 授信与流动性
{ANALYSIS_BLOCKS}

## 7. 债务到期墙
{ANALYSIS_BLOCKS}

## 8. 担保及或有风险
{ANALYSIS_BLOCKS}

## 9. 建议与行动清单
{ANALYSIS_BLOCKS}
"""

REPORT_WITHOUT_MATURITY_WALL = COMPLETE_REPORT.replace(
    f"## 7. 债务到期墙\n{ANALYSIS_BLOCKS}\n", ""
)

REPORT_WITH_ALIASES = COMPLETE_REPORT.replace("## 7. 债务到期墙", "## 7. 偿债高峰分析")

USER_TEMPLATE_WITH_DISCLOSED_ADDITION = COMPLETE_REPORT.replace(
    "报告基准日：2026-08-14；",
    "用户模板：custom.docx；报告基准日：2026-08-14；",
).replace(
    "## 2. 高管决策摘要",
    "## 模板适配说明\n系统补充章节：债务到期墙。补充原因：原模板缺失。\n\n## 2. 高管决策摘要",
).replace(
    "## 7. 债务到期墙",
    "## 7. 债务到期墙（系统补充章节）",
)

REPORT_WITH_UNDISCLOSED_ADDED_SECTION = USER_TEMPLATE_WITH_DISCLOSED_ADDITION.replace(
    "系统补充章节：债务到期墙。补充原因：原模板缺失。", "系统补充章节：无。"
)


class ValidateReportStructureTests(unittest.TestCase):
    def test_complete_standard_report_passes(self):
        result = validate_report(COMPLETE_REPORT, aliases={})

        self.assertTrue(result["valid"])
        self.assertEqual(result["missing_sections"], [])
        self.assertEqual(result["errors"], [])

    def test_legacy_metadata_charts_and_appendix_are_not_required(self):
        result = validate_report(COMPLETE_REPORT, aliases={})

        self.assertTrue(result["valid"])
        self.assertNotIn("metadata_data_quality", result["missing_sections"])
        self.assertNotIn("charts", result["missing_sections"])
        self.assertNotIn("methodology_sources", result["missing_sections"])

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
            "报告基准日：2026-08-14", "用户模板：custom.docx；报告基准日：2026-08-14"
        )

        result = validate_report(report, aliases={})

        self.assertIn("template_adaptation", result["missing_sections"])

    def test_executive_summary_requires_four_management_themes(self):
        report = COMPLETE_REPORT.replace("### 风险事项\n1. 现状、变化、影响和管理动作。\n\n", "")

        result = validate_report(report, aliases={})

        self.assertIn("missing_executive_theme:risk_matters", result["errors"])

    def test_kpi_table_requires_comparison_columns(self):
        report = COMPLETE_REPORT.replace(
            "| 指标（含币种/单位） | 本期 | 环比期 | 环比变化额 | 环比变化率 | 同比期 | 同比变化额 | 同比变化率 | 管理判断 |",
            "| 指标（含币种/单位） | 本期 | 管理判断 |",
        )

        result = validate_report(report, aliases={})

        self.assertIn("invalid_kpi_columns", result["errors"])

    def test_executive_prose_without_numbered_points_fails(self):
        report = COMPLETE_REPORT.replace("1. 现状、变化、影响和管理动作。", "现状、变化、影响和管理动作。", 1)
        result = validate_report(report, aliases={})
        self.assertIn("missing_numbered_executive_points:credit_management", result["errors"])

    def test_each_executive_theme_restarts_numbering(self):
        report = COMPLETE_REPORT.replace("### 融资经营\n1.", "### 融资经营\n2.")
        result = validate_report(report, aliases={})
        self.assertIn("invalid_executive_numbering:financing_management", result["errors"])

    def test_missing_yoy_dimension_fails(self):
        report = COMPLETE_REPORT.replace(" | 同比期 | 同比变化额 | 同比变化率", "")
        result = validate_report(report, aliases={})
        self.assertIn("invalid_kpi_columns", result["errors"])

    def test_kpi_table_rejects_definition_coverage_column(self):
        report = COMPLETE_REPORT.replace(
            "| 指标（含币种/单位） | 本期 | 环比期 | 环比变化额 | 环比变化率 | 同比期 | 同比变化额 | 同比变化率 | 管理判断 |",
            "| 指标（含币种/单位） | 本期 | 环比期 | 环比变化额 | 环比变化率 | 同比期 | 同比变化额 | 同比变化率 | 管理判断 | 定义/覆盖 |",
        )

        result = validate_report(report, aliases={})

        self.assertIn("legacy_kpi_column:definition_coverage", result["errors"])

    def test_analysis_section_requires_chart_table_narrative_order(self):
        report = COMPLETE_REPORT.replace(
            "### 图表\n结构图。\n\n### 明细表",
            "### 明细表\n结构明细。\n\n### 图表",
            1,
        )

        result = validate_report(report, aliases={})

        self.assertIn("invalid_content_order:financing_structure", result["errors"])

    def test_analysis_section_requires_each_content_block(self):
        report = COMPLETE_REPORT.replace("### 分析说明\n现状、变化、原因、影响和建议。", "", 1)

        result = validate_report(report, aliases={})

        self.assertIn("missing_content_block:financing_structure:narrative", result["errors"])

    def test_complete_top_ten_disclosure_passes(self):
        report = COMPLETE_REPORT.replace(
            "结构图。",
            (
                "Top 10 与其他（2项）。全量 12 项，展示前 10 项，其余 2 项汇总为其他；"
                "按金额降序；所有统计分析使用全量数据。"
            ),
            1,
        )

        result = validate_report(report, aliases={})

        self.assertTrue(result["valid"])
        self.assertNotIn("incomplete_top10_disclosure:financing_structure", result["errors"])

    def test_top_ten_requires_other_counts_sort_and_full_data_statement(self):
        report = COMPLETE_REPORT.replace("结构图。", "Top 10。", 1)

        result = validate_report(report, aliases={})

        self.assertIn("incomplete_top10_disclosure:financing_structure", result["errors"])

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
