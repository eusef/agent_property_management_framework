# Product Definition: Property Management for AI Agents

**Version:** 0.1 (Draft)
**Date:** 2026-03-12
**Status:** Awaiting Phil's review

---

## What This Is

An open-source, downloadable project that gives self-managing landlords a complete AI-assisted property management operating system. A person clones the repo, configures it for their properties, and any AI assistant (Claude, ChatGPT, Copilot, Gemini) immediately has the context, workflows, templates, and compliance structure to help them run their rental business.

**One sentence:** The operating system a landlord and their AI assistant use together to replace a property management company.

---

## The Problem It Solves

| Pain Point | Detail |
|-----------|--------|
| PM companies cost $5,250-$9,900/yr | 8-10% of rent, often with add-on fees for maintenance coordination, lease renewals, etc. |
| Self-managing is overwhelming | Compliance deadlines, maintenance tracking, tenant comms, financial records, vendor management -- too many moving parts |
| AI can help but people don't know how to set it up | 68-89% of small business owners are experimenting with AI; <10% have it in production |
| No "complete system" exists | Plenty of "use AI to write emails" content; zero "here's a complete AI-driven PM operating system" |
| Data lives in 5 different SaaS tools | Scattered across rent collection apps, spreadsheets, email, paper files, PM company portals |

**The gap this fills:** The space between "I know AI can help me manage my properties" and "my properties actually run on AI-assisted workflows."

---

## Who It's For

**Primary user:** Self-managing landlords with 1-10 residential rental units who want to use AI to handle the operational complexity that normally justifies hiring a PM company.

**User profile:**
- Owns 1-10 rental units (sweet spot: 1-4)
- Currently self-managing OR paying a PM company and considering the switch
- Comfortable with basic computer tasks (can use a text editor, navigate folders)
- Willing to use an AI assistant (any tool -- Claude, ChatGPT, etc.)
- Does NOT need to be technical (no coding required)

**Secondary user:** The AI assistant itself. The project is structured so that an AI agent can read the system's files and immediately understand the landlord's properties, obligations, workflows, and decision history. This is the key differentiator -- the framework is designed to be consumed by AI, not just by humans.

---

## Product Name & Positioning

### Recommended Name
**Property Management for AI Agents**

### Why This Name Works
- Flips the script: most products are "AI for X." This says the AI is the operator, you're the owner. Novel positioning.
- SEO-friendly: hits "property management" + "AI agents" -- both high-search terms in 2026
- Accurate: the repo IS designed to be consumed by AI agents
- Memorable and distinct from PM SaaS tools

### GitHub Repo Name Options

| Option | Pros | Cons |
|--------|------|------|
| `property-management-ai-agents` | Descriptive, SEO-friendly | Long |
| `pm-ai-agents` | Short, clean | Less discoverable |
| `ai-property-management` | Clear, searchable | Sounds like a SaaS product |
| `property-management-os` | Echoes CompanyOS (validated concept) | Doesn't signal AI |

**Recommendation:** `property-management-ai-agents`

### Tagline Options
- "The operating system a landlord and their AI run together."
- "Fire your PM company. Hire an AI agent."
- "Everything your AI assistant needs to manage your rentals."

---

## What Ships in v1

### The Install Experience

```
git clone https://github.com/[user]/property-management-ai-agents.git my-properties
cd my-properties
./setup.sh          # Creates venv, installs deps, walks through first-time config
```

**First-time setup prompts the user for:**
- Number of properties (creates property folders)
- Property addresses (populates README templates)
- Owner name(s)
- State/jurisdiction (loads relevant compliance templates)
- Preferred AI tool (generates appropriate agent context file)

After setup, the user opens their AI assistant, points it at the project, and says: "Read the system and help me get started."

### What's Inside

The project ships with five layers:

```
property-management-ai-agents/
│
├── 1. AGENT CONTEXT          ← The AI reads this to understand the system
├── 2. OPERATIONAL BACKBONE   ← Dashboard, tasks, decisions, improvements
├── 3. PROPERTY STRUCTURE     ← Per-property data (templates, ready to fill)
├── 4. KNOWLEDGE BASE         ← Compliance, templates, checklists, procedures
├── 5. WEB APP                ← Visual dashboard when AI isn't available
```

---

## Layer 1: Agent Context (The AI Interface)

This is the most important innovation. The project ships with a structured context file that any AI assistant can read to immediately understand the entire system.

### Design: Tool-Agnostic Agent Context

Instead of a Claude-specific `CLAUDE.md`, the project uses a naming convention any AI tool can consume:

| File | Purpose |
|------|---------|
| `AGENT_CONTEXT.md` | Primary file the AI reads first. System overview, working conventions, property summary, current status, decision history pointer. |
| `AGENT_SETUP.md` | Instructions for the AI on how to work within this system. Workflows, approval thresholds, file conventions, what to update and when. |
| `.claude/CLAUDE.md` | Auto-generated symlink/copy of AGENT_CONTEXT.md for Claude Code users |

### AGENT_CONTEXT.md Structure

```markdown
# Property Management System — Agent Context

## System Overview
[What this system is, how it's organized, where to find things]

## How to Work With the Owner
[Communication preferences, approval thresholds, decision-making process]

## Properties
[Summary of each property — address, type, rent, tenant, key dates, critical systems]

## Current Status
[What's active, what's blocking, upcoming deadlines]

## Key Standing Decisions
[Entity structure, approval thresholds, emergency procedures]

## Where to Find Things
[File map — which folders contain what]
```

### AGENT_SETUP.md Structure

```markdown
# Agent Working Instructions

## Your Role
You are the operational assistant for a self-managing landlord. You help with...

## Core Workflows
[Maintenance requests, rent tracking, compliance checks, tenant comms, vendor mgmt]

## Rules
- Never send communications without owner approval (Phase 1-2)
- Maintenance < $[threshold]: auto-approve. $[range]: owner approves. > $[amount]: multiple quotes.
- Always update AGENT_CONTEXT.md at the end of a working session
- When processing documents, cross-reference existing records and flag conflicts
- Log significant decisions in DECISIONS.md

## File Conventions
[How to name files, where to put things, CSV schemas, markdown formatting]
```

### Why This Works With Any AI Tool

| AI Tool | How It Consumes the Context |
|---------|---------------------------|
| **Claude Code** | Reads CLAUDE.md automatically at session start |
| **Claude (web/app)** | User uploads AGENT_CONTEXT.md to start a conversation, or uses Projects |
| **ChatGPT** | User uploads AGENT_CONTEXT.md or pastes into Custom Instructions |
| **GitHub Copilot** | Reads project files in workspace context |
| **Cursor / Windsurf** | Reads project files in workspace context |
| **Any future AI tool** | The context is plain markdown — universally readable |

---

## Layer 2: Operational Backbone

Root-level files that drive day-to-day operations:

| File | Purpose | Ships With |
|------|---------|-----------|
| `DASHBOARD.md` | At-a-glance system status: property summary, open maintenance, upcoming deadlines, financial snapshot, alerts | Template with example structure |
| `TASKS.md` | Active task list with checkbox tracking | Template with setup tasks pre-populated |
| `DECISIONS.md` | Chronological decision log (append-only) | Template with format guide + example entry |
| `IMPROVEMENTS.md` | Backlog of system improvements with effort/ROI estimates | Template with format guide |

---

## Layer 3: Property Structure

Per-property folders auto-generated during setup:

```
properties/
├── property-1/
│   ├── README.md              # Property master profile (address, type, rent, systems, etc.)
│   ├── documents/             # Lease, insurance, purchase docs, permits
│   ├── maintenance/           # Work orders, repair history
│   ├── tenants/               # Tenant info, communication log
│   ├── financials/
│   │   ├── income.csv         # Rent received (date, amount, method, notes)
│   │   ├── expenses.csv       # All expenses (date, vendor, amount, category, description)
│   │   └── deposits.csv       # Security deposit tracking
│   ├── compliance/            # Property-specific disclosures, permits
│   ├── inspections/           # Inspection reports, photos
│   ├── projects/              # Capital improvement projects
│   └── maintenance-forecast.md # Predicted maintenance by system age
│
├── property-2/
│   └── [same structure]
│
└── property-template/         # Blank template for adding new properties
    └── [same structure with instructions in each file]
```

### Property README.md Template

The property README is the AI's quick-reference card. Ships with clearly marked fields:

```markdown
# [Property Name]

## Overview
- **Address:** [street, city, state, zip]
- **Type:** [single family / duplex / triplex / condo / etc.]
- **Built:** [year]
- **Sq Ft:** [number]
- **Beds/Baths:** [X bed / X bath]
- **Purchase Price:** [amount]
- **Purchase Date:** [date]

## Rental Info
- **Current Rent:** $[amount]/mo
- **Lease Type:** [month-to-month / fixed term]
- **Lease Expiration:** [date]
- **Tenant Move-in:** [date]
- **Security Deposit:** $[amount]
- **Pet Policy:** [yes/no, deposit amount]

## Key Systems (age + condition tracking)
| System | Installed | Age | Expected Life | Condition | Notes |
|--------|-----------|-----|--------------|-----------|-------|
| Roof | | | | | |
| HVAC | | | | | |
| Water Heater | | | | | |
| Electrical Panel | | | | | |
| Plumbing | | | | | |
| Appliances | | | | | |

## Insurance
- **Provider:** [company]
- **Policy #:** [number]
- **Renewal Date:** [date]
- **Dwelling Coverage:** $[amount]

## Mortgage
- **Lender:** [company]
- **Loan #:** [number]

## Key Contacts
| Role | Name | Phone | Email | Notes |
|------|------|-------|-------|-------|

## Owner(s)
- [name(s)]
```

### CSV Schemas

**income.csv**
```
date,property,amount,source,method,reference,notes
```

**expenses.csv**
```
date,property,vendor,amount,category,description,receipt,approved_by
```

**deposits.csv**
```
tenant,property,amount_held,account,date_received,interest_rate,notes
```

---

## Layer 4: Knowledge Base

### Compliance (ships with Oregon templates, structured for any state)

```
compliance/
├── README.md                      # How to use compliance docs + disclaimer
├── landlord-tenant-law.md         # State-level summary
├── fair-housing.md                # Federal + state fair housing obligations
├── eviction-procedures.md         # Step-by-step eviction process
├── security-deposit-rules.md      # Hold, return, deduction rules
├── records-retention-policy.md    # What to keep, how long
├── emergency-procedures.md        # Emergency response protocols
├── insurance-tracker.md           # Policy tracking across properties
└── calendar.md                    # All compliance deadlines in one view
```

**Important:** Ships with Oregon as the default jurisdiction (Phil's expertise). Each file has a clear structure that users in other states can fill in. The compliance README includes a prominent disclaimer: *"These are operational summaries, not legal advice. Have a local attorney review before relying on them."*

**Jurisdiction expansion path:** Future paid compliance packs ($49-$79/state) plug into this same structure.

### Templates

```
templates/
├── comms/                         # Communication templates
│   ├── rent-reminder.md           # Day 3, Day 5, Day 10 escalation
│   ├── maintenance-ack.md         # Standard + emergency acknowledgment
│   ├── maintenance-update.md      # Scheduled, completed, delay notifications
│   ├── lease-renewal.md           # Same terms, adjusted terms, non-renewal
│   ├── move-in-welcome.md         # Welcome letter with property info
│   ├── move-out-notice.md         # Move-out procedures + expectations
│   └── inspection-notice.md       # Routine + repair entry (24hr notice)
│
├── checklists/
│   ├── move-in-inspection.md      # Room-by-room condition + photo checklist
│   ├── move-out-inspection.md     # Comparison checklist + deposit accounting
│   ├── tenant-screening.md       # Income, credit, rental history, background
│   ├── property-acquisition.md    # Due diligence + financial analysis
│   └── annual-review.md          # Year-over-year performance review
│
└── forms/
    └── README.md                  # Links to government forms by state
```

### Documentation

```
docs/
├── getting-started.md             # First-time setup guide (human-readable)
├── how-it-works.md                # System architecture for curious users
├── adding-a-property.md           # Step-by-step: add a new property
├── onboarding-a-tenant.md         # Step-by-step: new tenant workflow
├── emergency-procedures.md        # What to do when things break
├── manual-fallback.md             # Operating without AI access
└── faq.md                         # Common questions
```

### Vendors

```
vendors/
├── README.md                      # Vendor database (name, trade, contact, rating, notes)
└── performance.csv                # Job tracking (date, vendor, property, work, cost, rating)
```

### Financials (portfolio-level)

```
financials/
├── summary.csv                    # Portfolio-level monthly P&L
└── tax/
    └── [year]/
        ├── README.md              # Tax prep checklist
        ├── 1099-tracking.csv      # Contractor payments > $600
        └── estimated-payments.csv # Quarterly estimated tax tracking
```

### Continuity

```
continuity/
├── README.md                      # Succession plan overview
├── successor-letter.md            # "If something happens to me" instructions
└── credentials-checklist.md       # Where accounts/passwords are stored
```

---

## Layer 5: Web App

The FastAPI + HTMX dashboard ships as part of the project. It provides a visual interface for when the AI assistant isn't available or when the user prefers a browser view.

### What It Does

| Feature | Description |
|---------|-------------|
| **Dashboard** | At-a-glance view: open tasks, recent files, property cards, pinned files |
| **File browser** | Navigate the full folder structure, mirrors the repo |
| **Markdown viewer** | Rendered markdown with interactive checkboxes |
| **Markdown editor** | Side-by-side editor with live preview |
| **Search** | Full-text search across all markdown files |
| **Task toggle** | Click checkboxes to toggle task completion |

### What It Doesn't Do

- No database (reads/writes markdown files directly)
- No authentication (local-only, runs on localhost)
- No cloud deployment (intentionally local)
- No automated communications (human-in-the-loop)

### Startup

```bash
./startup.sh
# Opens browser to http://localhost:8000
```

Requires Python 3.11+. The startup script handles venv creation and dependency installation.

---

## What's NOT in the Free Project (Paid Products)

| Excluded | Why | Where It Lives |
|----------|-----|---------------|
| Jurisdiction-specific compliance packs beyond Oregon | Requires lawyer review per state; this is a revenue stream | Gumroad/course platform, $49-$79/state |
| Video tutorials and walkthroughs | The "how to use this" education layer | Flagship course, $297-$497 |
| Community access | Peer support, Q&A, live sessions | Skool/Circle, $29-$39/mo |
| Pre-built AI prompt libraries | Workflow-specific prompt chains | Prompt pack, $27-$47 |
| Phil's real property data | Private, obviously | Reference implementation only |

**The line:** The framework gives you everything you need to run the system. The paid products teach you how to set it up well and keep you current on compliance.

---

## Installation & First-Run Experience

### Step 1: Clone
```bash
git clone https://github.com/[user]/property-management-ai-agents.git my-properties
cd my-properties
```

### Step 2: Setup
```bash
./setup.sh
```

The setup script:
1. Checks Python 3.11+ is installed
2. Creates a virtual environment
3. Installs web app dependencies
4. Runs an interactive first-time configuration:
   - How many properties? (creates folders)
   - Property addresses (populates READMEs)
   - Owner name(s)
   - State/jurisdiction (adjusts compliance docs)
   - Preferred AI tool (generates CLAUDE.md / notes on ChatGPT setup / etc.)
5. Initializes a git repo (if not already one)
6. Prints "You're ready. Open your AI assistant and say: 'Read AGENT_CONTEXT.md and help me set up my first property.'"

### Step 3: First AI Session
The user opens their AI assistant and the AI:
1. Reads AGENT_CONTEXT.md and AGENT_SETUP.md
2. Understands the system structure
3. Walks the user through filling in property details
4. Helps process any existing documents (leases, insurance policies, etc.)
5. Sets up compliance calendar based on their jurisdiction
6. Identifies first action items

**This is the "aha moment"** -- the AI immediately knows the system, knows the user's properties, and starts being useful. No training, no onboarding videos required for basic operation.

---

## Key Differences: Reference Implementation → Public Project

| Aspect | Phil's Version | Public Version |
|--------|---------------|----------------|
| Property data | Real addresses, real tenant, real financials | Blank templates with clear field labels |
| Agent context | CLAUDE.md (Claude-specific) | AGENT_CONTEXT.md (tool-agnostic) + auto-generated tool-specific files |
| Compliance | Oregon-specific, partially filled | Oregon as default template, clear structure for any state |
| Vendors | 75+ real contractors | Empty template with example format |
| Financial history | 6+ years of real statements | Empty CSVs with schema headers + example row |
| Web app | Tested against real data | Same code, works against template data |
| Agent infrastructure | .agents submodule (Phil's cross-project system) | Self-contained AGENT_SETUP.md (no submodule dependency) |
| Decisions log | 8 real decisions | Format guide + 1 example entry |
| Setup | Manual | Interactive setup.sh script |

---

## README.md (The GitHub Landing Page)

The README is the single most important marketing asset. It needs to:

1. **Hook in 5 seconds:** "Replace your $5,250/yr property manager with an AI-assisted system you own and control."
2. **Show, don't tell:** Screenshot of the web dashboard, example AI conversation, folder structure tree
3. **Prove substance:** Link to the compliance templates, the workflow docs, the checklist library
4. **Get them started in 2 minutes:** Clone → setup → first AI session
5. **Be authentic:** "Built by a landlord who fired his PM company and saved $X/year"

### README Structure

```
# Property Management for AI Agents
> The operating system a landlord and their AI run together.

[screenshot of dashboard]

## What This Is
[2-3 sentences]

## What You Get
[Bullet list of the 5 layers]

## Quick Start
[clone, setup, first AI session -- 3 commands]

## How It Works
[Brief explanation + link to docs/how-it-works.md]

## Screenshots
[Dashboard, file browser, editor, example AI conversation]

## What's Inside
[Folder tree]

## FAQ
[Top 5 questions]

## Contributing
[How to contribute templates, compliance docs, improvements]

## License
[MIT or Apache 2.0]
```

---

## Success Metrics (Validation)

Per the opportunity doc's validation checklist:

| Signal | Target | Timeline |
|--------|--------|----------|
| GitHub stars | 50+ | 30 days post-launch |
| BiggerPockets article comments | 100+ | 30 days post-article |
| Gumroad compliance pack sales | Any organic sales | 30 days |
| Email list signups | 200+ | 60 days |
| Clone/fork count | 100+ | 60 days |

**Kill criteria:** <20 stars in 30 days AND <50 BP comments AND zero Gumroad sales → re-evaluate before investing in course creation.

---

## Open Questions for Phil

| # | Question | Options | Recommendation |
|---|----------|---------|---------------|
| 1 | **License type?** | MIT (maximum adoption) vs. Apache 2.0 (patent protection) vs. AGPL (copyleft) | MIT — lowest barrier, most stars, standard for open-source frameworks |
| 2 | **Oregon-only compliance or blank?** | Ship Oregon compliance as the default vs. ship blank templates only | Oregon default — it's Phil's expertise, demonstrates real value, other states can follow the pattern |
| 3 | **Setup script: interactive or config file?** | Interactive CLI wizard vs. edit a config.yaml | Interactive wizard for the "magic moment," with config.yaml generated as output for repeatability |
| 4 | **Branding in the repo?** | Phil's name attached vs. anonymous/org | Phil's name — authenticity is the differentiator per the opportunity doc |
| 5 | **Git init during setup?** | Auto-init git repo vs. let user handle | Auto-init — git history is core to the system's value (version-controlled property records) |
| 6 | **Example data?** | Ship with fictional example property filled in vs. blank only | Include one fictional "123 Main St" example property that demonstrates what a filled-in system looks like, plus blank templates |
| 7 | **Web app: same codebase or cleaned up?** | Port Phil's existing webapp code vs. rewrite for public | Port + clean up — the existing code is well-tested (5,328 lines of tests), just needs config generalization |

---

## Implementation Sequence

Assuming Phil approves this product definition, the build sequence is:

| Step | Task | Effort |
|------|------|--------|
| 1 | Create folder structure in PM_FRAMEWORK | 1 session |
| 2 | Write AGENT_CONTEXT.md and AGENT_SETUP.md (tool-agnostic agent interface) | 1 session |
| 3 | Create all templates (port from reference, strip personal data, generalize) | 1-2 sessions |
| 4 | Write operational backbone files (DASHBOARD.md, TASKS.md, DECISIONS.md, IMPROVEMENTS.md templates) | 1 session |
| 5 | Port and clean up web app | 1-2 sessions |
| 6 | Write setup.sh (interactive first-time config) | 1 session |
| 7 | Create docs/ (getting-started, how-it-works, FAQ, etc.) | 1 session |
| 8 | Write README.md (GitHub landing page) | 1 session |
| 9 | Create example property ("123 Main St") showing a filled-in system | 1 session |
| 10 | End-to-end test: clone fresh, run setup, use with AI, verify web app | 1 session |

**Estimated total:** 8-12 working sessions.

---

## What Makes This Different From Everything Else

| Differentiator | Why It Matters |
|---------------|---------------|
| **The AI is a first-class user** | The project is literally designed to be read and operated by AI agents. Not "AI-compatible" as an afterthought. |
| **Complete system, not prompts** | Shipping 60+ files, templates, checklists, compliance docs, a web app. Not a PDF of ChatGPT prompts. |
| **You own your data** | Markdown + CSV on your computer. No vendor lock-in, no SaaS subscription, no data in someone else's cloud. |
| **Built by someone who actually uses it** | Not a consultant's theory. Phil manages real properties with this system. |
| **Tool-agnostic** | Works with Claude, ChatGPT, Copilot, Gemini, or whatever comes next. Plain text is forever. |
| **Continuity planning** | The only PM system that includes succession planning. If something happens to you, someone else can pick up where you left off. |
| **Open source** | In a market of $995 bootcamps and gated content, giving away the system builds trust and proves substance. |
