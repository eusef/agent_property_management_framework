# Records Retention Policy

**Purpose:** Define how long each type of record must be kept, where it's stored, and when it can be purged.
**Applies to:** All records in this repository and any physical/digital records outside the repo.
**Review frequency:** Annually (add to compliance calendar)
**Last updated:** [DATE]

---

## Retention Schedule

| Record Type | Minimum Retention | Start Date | Storage Location | Notes |
|-------------|------------------|------------|-----------------|-------|
| **Tax returns (federal + state)** | 7 years | Date filed | financials/tax/YYYY/ | IRS can audit up to 6 years in some cases |
| **1099-NEC forms** | 7 years | Date filed | financials/tax/YYYY/ | Keep copies of what you sent and received |
| **W-9 forms** | 4 years after last payment | Last payment date | vendors/{vendor-slug}.md or physical file | Required for 1099 reporting |
| **Income records (rent payments)** | 7 years | Date of payment | properties/{slug}/financials/income.csv | Supports tax returns |
| **Expense records (receipts, invoices)** | 7 years | Date of expense | properties/{slug}/financials/expenses.csv + receipts | Supports tax deductions |
| **Bank statements** | 7 years | Statement date | Physical/digital archive | Supports tax returns |
| **Lease agreements** | 6 years after termination | Lease end date | properties/{slug}/tenants/{tenant}/ | [YOUR_STATE] statute of limitations |
| **Lease amendments/addenda** | Same as parent lease | Lease end date | With parent lease | |
| **Security deposit records** | 6 years after return/disposition | Date deposit returned | financials/deposits/ | [YOUR_STATE_STATUTE] |
| **Move-in/move-out inspections** | 6 years after tenant departure | Move-out date | properties/{slug}/inspections/ | Supports deposit disposition |
| **Tenant applications** | 3 years | Application date | Shred after retention period | Fair housing compliance |
| **Tenant screening reports** | 3 years | Report date | Shred after retention period | FCRA compliance |
| **Maintenance requests/work orders** | Life of ownership + 3 years | Date of request | properties/{slug}/maintenance/ | Supports warranty claims, liability defense |
| **Vendor contracts** | 6 years after completion | Contract end date | vendors/{vendor-slug}.md | |
| **Insurance policies** | Life of ownership + 3 years | Policy end date | LEGAL/ + compliance/insurance-tracker.md | Keep expired policies for claims on past events |
| **Insurance claims** | Life of ownership + 3 years | Claim resolution date | compliance/insurance-tracker.md | |
| **Property purchase documents** | Life of ownership + 7 years | Date of sale | LEGAL/ | Supports cost basis for capital gains |
| **Home inspection reports** | Life of ownership | N/A | properties/{slug}/inspections/ | Baseline condition reference |
| **PM agreement** | 6 years after termination | Termination date | LEGAL/ | |
| **Compliance docs (legal summaries)** | Current version only | N/A | compliance/ | Update as laws change |
| **Communication logs (tenant)** | 6 years after tenant departure | Last communication | properties/{slug}/tenants/{tenant}/ | Supports dispute resolution |
| **Decision log** | Life of ownership | N/A | DECISIONS.md | Never purge |
| **LLC formation docs** | Life of entity + 7 years | Dissolution date | LEGAL/ | |
| **Depreciation schedules** | Life of ownership + 7 years | Date of sale | financials/tax/ | Required for cost basis |

---

## Storage Tiers

| Tier | Location | Access | Backup |
|------|----------|--------|--------|
| Active | This git repository | Immediate | Git history preserves all versions |
| Archive | Physical file or cloud archive | Within 24 hours | Annual backup to external drive |
| Continuity | [YOUR_SECURE_LOCATION] | Emergency access only | Key documents only |

---

## Quarterly Archive Process

Run quarterly (add to compliance calendar: Jan 1, Apr 1, Jul 1, Oct 1):

1. Review records that have passed their retention period
2. For digital records past retention: move to an `archive/` directory or delete
3. For physical records past retention: shred (do not just discard)
4. For tenant applications/screening reports past 3 years: shred immediately (PII)
5. Log what was purged in DECISIONS.md
6. Never purge: decision log, property purchase docs, home inspections, insurance policies (keep all expired policies)

---

## Special Rules

**Litigation hold:** If any legal action is pending or reasonably anticipated, do NOT destroy any records related to the dispute regardless of retention schedule. This includes tenant disputes, insurance claims, contractor disputes, or government investigations.

**Tenant PII:** Tenant applications, screening reports, and SSNs should be stored securely and destroyed promptly after the retention period. Do not keep copies in multiple locations.

**Digital records in git:** Git history preserves deleted files. A `git rm` does not truly destroy data. For true destruction of PII, a history rewrite would be needed (rare, only for compliance).

**Tax safe harbor:** When in doubt, keep tax-related records for 7 years. The cost of storing digital records is near zero; the cost of not having them during an audit is high.

---

*This policy should be reviewed by a CPA or attorney to confirm [YOUR_STATE]-specific requirements. Last reviewed: [DATE]*
