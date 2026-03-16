# How It Works -- Architecture Overview

**Purpose:** Explains how the PM Framework is structured and why it works the way it does.

---

## Core Principles

### 1. File-Based, Not Database-Based
Everything lives in plain text files -- markdown (.md) for documents, CSV for structured data, and shell scripts for automation. There is no database to manage, no server to keep running, and no SaaS subscription to pay.

**Why:** Plain text files are portable, version-controllable, human-readable, and will never become obsolete. You can read them with any text editor on any operating system. If every tool you use disappears tomorrow, your data is still accessible.

### 2. Git-Versioned
The entire system lives in a git repository. Every change is tracked, every version is recoverable, and the full history of your property management decisions is preserved.

**Why:** Git provides automatic backup, change tracking, and audit trail. You can see when any file was changed, what changed, and roll back if needed.

### 3. AI-Assisted, Human-Controlled
An AI assistant (Claude or similar) can read these files, help draft communications, analyze financials, and flag compliance deadlines. But every action that affects a tenant, vendor, or legal obligation requires human approval before sending.

**Why:** AI is excellent at processing structured data, drafting from templates, and catching things you might miss. But landlord-tenant interactions have legal and relationship consequences that require human judgment.

### 4. Markdown-Driven
All documentation, templates, checklists, and compliance references are in markdown format. Markdown is simple, readable as plain text, and renders nicely in any markdown viewer.

**Why:** Low friction. Anyone can read and edit markdown without special software.

---

## Directory Structure

```
pm-framework/
├── properties/           # One subfolder per property
│   └── {property-slug}/
│       ├── README.md     # Property overview and key details
│       ├── financials/   # income.csv, expenses.csv
│       ├── maintenance/  # Work orders and history
│       ├── tenants/      # Tenant records
│       └── inspections/  # Inspection reports
├── templates/            # Reusable templates
│   ├── comms/            # Tenant communication templates
│   ├── checklists/       # Inspection and screening checklists
│   └── forms/            # Official form inventory
├── compliance/           # Legal compliance documents
├── examples/             # Worked examples by jurisdiction
├── docs/                 # System documentation
├── vendors/              # Vendor database and performance tracking
├── financials/           # Portfolio-level financials and tax docs
├── continuity/           # Business continuity plan
├── scripts/              # Automation scripts
├── DASHBOARD.md          # Current status overview
├── DECISIONS.md          # Chronological decision log
└── CLAUDE.md             # AI working memory
```

---

## Data Flow

### Rent Collection
1. Tenant pays rent
2. Owner confirms receipt in bank account
3. Payment logged in `properties/{slug}/financials/income.csv`
4. AI (or owner) checks if all rents received and flags any missing

### Maintenance Request
1. Tenant reports issue (email, text, phone)
2. AI drafts acknowledgment using `templates/comms/maintenance-ack.md`
3. Owner reviews and sends acknowledgment
4. Owner contacts vendor from `vendors/README.md`
5. Work scheduled, AI drafts update using `templates/comms/maintenance-update.md`
6. Owner reviews and sends update
7. Work completed, expense logged in `properties/{slug}/financials/expenses.csv`
8. Maintenance record created in `properties/{slug}/maintenance/`

### Compliance Monitoring
1. `compliance/calendar.md` contains all deadlines
2. AI (or `scripts/compliance-check.py`) scans calendar weekly
3. Items due within 30 days appear in `DASHBOARD.md`
4. Items due within 7 days flagged as URGENT
5. Owner takes action based on alerts

---

## Automation Scripts

| Script | Purpose | Frequency |
|--------|---------|-----------|
| `setup.sh` | Initial setup and property scaffolding | One-time |
| `compliance-check.py` | Scan calendar for upcoming deadlines | Weekly |
| `generate-dashboard.py` | Rebuild DASHBOARD.md from current data | Weekly |

---

## AI Integration

The AI assistant works with this system by:

1. **Reading** markdown and CSV files for context
2. **Drafting** communications, reports, and analysis
3. **Scanning** compliance deadlines and flagging upcoming items
4. **Suggesting** actions based on the data (e.g., rent reminder needed, vendor follow-up)
5. **Updating** files after owner approval (CLAUDE.md, DASHBOARD.md, CSVs)

The AI never sends communications directly or makes financial decisions autonomously. The owner reviews and approves every outbound action.

---

## Manual Fallback

If AI is unavailable, the system still works -- it's just more manual. See `docs/manual-fallback.md` for step-by-step procedures for every critical function.
