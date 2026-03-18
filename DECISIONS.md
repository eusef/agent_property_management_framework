# Decision Log

All significant decisions are logged here in reverse chronological order (newest first). Append-only — never delete entries.

---

### YYYY-MM-DD: Set maintenance auto-approve threshold at $500

**Context:** Evaluating how much autonomy the AI agent should have for approving maintenance expenses.
**Decision:** Set approval threshold at $500 for maintenance expenses.
**Rationale:** Balances staying informed on larger repairs while not bottlenecking routine fixes like faucet repairs or minor plumbing. Aligns with common property management practice.
**Impact:** Maintenance < $500 agent recommends and owner approves; >= $500 requires multiple quotes and owner approval.

---

### YYYY-MM-DD: Use markdown + CSV as sole data format

**Context:** Evaluating how to store property management data. Options included databases, spreadsheets, or flat files.
**Decision:** All data stored as markdown and CSV in a git repository. No external databases or cloud dependencies.
**Rationale:** Portable, human-readable, version-controlled, works offline, no vendor lock-in. Owner can read and edit files with any text editor. Works with any AI tool.
**Impact:** Entire system design builds on this. All financial tracking uses CSV. All documentation is markdown.

---

### YYYY-MM-DD: Self-manage properties with AI assistance

**Context:** Owner considering whether to use a property management company (8-10% of rent) or self-manage.
**Decision:** Build an AI-assisted self-management system to replace the PM company.
**Rationale:** At $1,850/mo rent, PM fees would be $1,776-$2,220/year per property. Self-management with AI assistance eliminates this cost while providing better control and tenant responsiveness.
**Impact:** This entire framework exists because of this decision.

---

### YYYY-MM-DD: Review-then-send mode for all communications

**Context:** Deciding how much autonomy the AI agent should have for tenant and vendor communications.
**Decision:** AI drafts all communications; owner reviews and sends everything.
**Rationale:** In early phases, the owner wants to maintain direct control over all outbound messaging. This can be relaxed over time as trust is established.
**Impact:** No automated sending of notices, emails, or vendor dispatches. Agent always drafts, owner always sends.

---

### YYYY-MM-DD: Scaffold directory structure per product definition

**Context:** Product definition approved. First deliverable is folder structure creation.
**Decision:** Created full directory structure with example property, templates, compliance docs, and vendor database.
**Rationale:** Establishes the data layer foundation so all subsequent work (property onboarding, financial tracking, compliance monitoring) has a home.
**Impact:** All workflows can now proceed. New properties follow the property-template pattern.
