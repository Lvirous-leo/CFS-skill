# CFS Skills

Reusable Codex Skills managed in one repository. Each Skill lives in `skills/<skill-name>/` and must contain a valid `SKILL.md`.

## Skills

| Skill | Purpose | Path | Status |
|---|---|---|---|
| `finance-analysis-report` | Generate traceable group financing analysis reports from tool-returned data, with debt, credit, maturity, guarantee, multi-currency, and Word-template controls. | [`skills/finance-analysis-report/`](skills/finance-analysis-report/) | Active |
| `product-design-system` | Apply the Product visual system to websites, landing pages, dashboards, product UI, decks, email layouts, newsletters, and posters. | [`skills/product-design-system/`](skills/product-design-system/) | Active |
| `prd` | Create or update Chinese enterprise PRDs from OpenDesign prototypes, existing PRD samples, and user decisions. | [`skills/prd/`](skills/prd/) | Active |

## Install

Copy the required Skill directory into your Codex Skills directory. Install only the Skill subdirectory, not the whole management repository.

```bash
cp -R skills/finance-analysis-report "${CODEX_HOME:-$HOME/.codex}/skills/finance-analysis-report"
cp -R skills/product-design-system "${CODEX_HOME:-$HOME/.codex}/skills/product-design-system"
cp -R skills/prd "${CODEX_HOME:-$HOME/.codex}/skills/prd"
```

## Invoke

```text
$finance-analysis-report
$product-design-system
$prd
```

## Validate

Run the Skill Creator validator against the selected Skill directory and run its unit tests:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/finance-analysis-report
python3 /path/to/skill-creator/scripts/quick_validate.py skills/product-design-system
python3 /path/to/skill-creator/scripts/quick_validate.py skills/prd
python3 -m unittest discover -s skills/finance-analysis-report/tests -p 'test_*.py' -v
```

## Contribute

Use lowercase letters, digits, and hyphens for Skill directory names. Keep one Skill per `skills/<skill-name>/`, include `SKILL.md`, avoid unrelated documentation inside individual Skills, and validate before publishing.

## Migration note

`group-financing-analysis` was renamed to `finance-analysis-report` and moved from the repository root into the multi-Skill layout.
