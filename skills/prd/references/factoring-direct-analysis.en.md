# Factoring Bank-Connectivity Analysis: Mapping and Manual-Draft Alignment

## Scope

Use only for factoring bank-connectivity analysis, mapping bank APIs to platform standard interfaces, and incremental updates to those analysis documents. Do not activate this reference for ordinary factoring PRDs, screen design, other financing modules, or other interface analysis merely because they mention factoring or APIs. Its workbook shape, project decisions, and scene codes are not general PRD rules.

Basis: the 2026-11-06 manual edits to Bank of Communications connectivity analysis and subsequent explicit user corrections; on 2026-11-26 the user requested skill retention and limited its use to factoring connectivity analysis. The Agricultural Bank of China manual final draft and retrospective provide additional examples. Use the decisions confirmed for each project when specifying parties, product codes, defaults, and statuses.

## 1. Select the Standard Object Before Mapping Fields

Confirmed for this project: **the business results from financing-status pushes, financing-result queries, and repayment-result queries all map to the platform factoring result-query standard response, `FactoringFinancingResultResponse`.**

| Content | Standard object |
| --- | --- |
| Financing application request | `FactoringFinancingApplyRequest` |
| Synchronous application acknowledgment | `FactoringFinancingApplyResponse` |
| Financing-result and repayment-result query parameters | `FactoringFinancingResultRequest` |
| Business results in financing-status pushes and responses to financing-result and repayment-result queries | `FactoringFinancingResultResponse` |

- A push labeled Request in the bank contract does not select the platform application-request schema. Select the target from the bank → platform → business-system data flow, rather than the API name or HTTP direction alone.
- For each bank interface, identify direction, trigger, target standard object, and role in the flow. Analyze any prerequisite customer-code lookup according to its in-scope purpose. Record bank business status, synchronous acceptance, and callback acknowledgment with their own codes and actions.
- Use the exact English field names and Chinese meanings from the platform definition. A source field such as `accountsPayNum` may appear as a labeled lookup key in a maintained worksheet. State the path from bank `billNo` to original submission, source payable, and original financing record. Recover `askNumber` and `finBizDocCode` from the associated original business. Output only fields declared in the selected platform response.
- In this project, financing results use `financingScene=LOAN` and repayment results use `financingScene=REPAY`. Verify meaning within the scene before reusing a response field. Its English name alone does not make it exclusive to one scene; a shared response does not make repayment total, principal, and actual interest interchangeable.
- Check schema membership, business meaning, and data sourcing separately. Do not invent English fields, force unsupported matches, or promote suggestions into confirmed rules when definitions, associations, or enums are missing. Other projects use their current approved schemas rather than copying these class names and codes mechanically.

## 2. Analyze the Actual In-Scope Data Sourcing

The earlier failure was turning a mapping table into a field-by-field review, filling rows with missing-standard, cannot-substitute, and pending labels while obscuring concrete sources and scope. Instead:

- Establish document perspective, party roles, and record granularity first. In the Agricultural Bank of China example, the platform buyer's payable names the supplier as payee and creditor. The bank sees that obligation as the supplier's receivable. Carry the same relationship through customer-code lookup, financing submission, and callback matching.
- Map each collection together with its child fields. State the source collection and how each entry is produced, then fill the standard group, English name, Chinese name, and necessary logic for each child. In the example, `billList` takes the payables linked to the current financing application, with one bank receivable per source record. Put supported fields such as payer organization name and payable date on their own rows. Source contracts and invoices from the links for that record.
- State each field's role on its row. Fill the corresponding field for direct sourcing. For lookup or validation, state that purpose and the actual source of the transmitted value. Write generation, defaults, and conditional conversion in the logic column. For example, use `accountsPayNum` to link the source payable and generate the bank `billNo` by the confirmed rule. Use the contract and invoice names as sources for seller names and use the payable payee fields to verify the supplier.
- Unestablished mappings may remain blank. **Blank does not mean omit, inapplicable, or optional at the bank.** Preserve original requiredness, type, length, and notes, and identify gaps that block this integration.
- Treat manual changes to parties, amounts, dates, and defaults as specific business decisions, not merely shorter wording. For example, this manual draft sourced borrower details from the payable payer and defaulted voucher type to 0. Neither becomes a default for other banks or every factoring scenario. Trace actual shared-field impacts without turning an application source into a response field.
- Distinguish direct bank values, platform recovery from the original document, platform calculations, and undefined data. A missing direct bank field does not authorize fabricating a value or automatically require extending the standard. Reuse or propose an extension only after checking business and schema meaning.

## 3. Follow the Latest Maintained Wording and Structure

- Let mapping columns express equivalent fields; do not repeat take the corresponding field. Use short processing statements such as aggregate invoice amounts or take the payable payer-account name. Do not repeat rejected alternatives in every row.
- This manual sample uses 12 columns: eight bank-original columns followed by standard group, standard English field, standard Chinese field, and sourcing/conversion/processing. When following this sample, do not restore removed standard-object, mapping-conclusion, and source columns. Preserve other maintained structures rather than imposing 12 columns universally.
- After the user reduces the workbook to integration scope plus individual interfaces, do not restore a long overview, coverage-check sheet, or status-explanation sheet. Internal verification does not automatically become another deliverable surface.
- Organize unresolved items within the current user-selected structure. If the user removed a consolidated pending sheet, use brief notes only on necessary fields rather than restoring it to satisfy a generic template. Blank cells must not conceal critical integration blockers.
- Removing generic acknowledgments from the application sample does not remove responses from every interface. Preserve financing and repayment business results needed for queries and pushes. Incremental edits retain bank originals and unaffected manual content.

## 4. Focused Pre-Save and Post-Save Checks

- Inspect current sheets, columns, and manual edits before writing. Old snapshots support comparison, not restoration of intentionally removed content. Separate style mismatches, earlier mapping errors, newly disclosed user decisions, and remaining unknowns.
- Review bank requests, callback acknowledgments, and platform business results against their respective contracts. Check field membership and actual value sources for the platform response. Check labeled lookup and validation fields according to their purpose. Verify the meaning and codes of same-named fields across interfaces.
- Walk through in-scope success, failure, and duplicate notices. Describe the established writeback actions and distinguish the source payable, bank submission, and financing record. Where resubmission after invalidation is supported, identify the old and new submission identifiers, their association with the source, and the handling of late notices. Verify successful repayment, settlement criteria, and actual principal before specifying plan updates or record creation.
- Focus review on gaps that affect integration testing, such as missing sources for mandatory fields, date defaults that differ from bank definitions, missing product-code conversions, whether a loan application number is also a loan reference, and unresolved status or amount meanings. Preserve decisions in the maintained draft and identify the effect of each remaining contract question.
- Change only affected mapping and processing columns. Read back bank originals, preserved manual content, updated fields, and removal of superseded explanations. Preserve concurrent user edits rather than restoring an old baseline or claiming those edits as the agent's work.
