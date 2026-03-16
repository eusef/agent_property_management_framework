# Frequently Asked Questions

---

## General

### What is this framework?
A file-based, AI-assisted property management system. All your property data, compliance documents, templates, and financial records live in plain markdown and CSV files, tracked with git. An AI assistant can help process the data, but the system works fully manually too.

### Do I need to be technical to use this?
You need basic comfort with text files and folders. If you can edit a document, you can use this system. Git knowledge is helpful but not required for daily use -- you can always just edit files directly.

### What AI assistant does this work with?
Any AI that can read and process text files. It was designed with Claude in mind but will work with ChatGPT, Gemini, or any LLM that can read your files.

### What if the AI is unavailable?
The system works 100% manually. See `docs/manual-fallback.md` for step-by-step procedures for every critical function without AI.

---

## Setup

### How do I add my first property?
Follow the guide in `docs/adding-a-property.md`. The short version: create a directory under `properties/`, fill in the README template, initialize your CSV files, and update the compliance calendar.

### How do I customize this for my state?
All compliance documents in `compliance/` use `[YOUR_STATE]` placeholders. Research your state's landlord-tenant laws and fill them in. See `examples/oregon/` for a worked example showing what completed files look like.

### Do I need a lawyer to set this up?
You don't need a lawyer to set up the system itself. However, you should have a lawyer review any compliance documents before relying on them for legal actions (evictions, security deposit deductions, lease terms, etc.).

---

## Daily Operations

### How do I track rent payments?
Add a row to `properties/{property-slug}/financials/income.csv` each time rent is received. The AI can check this and flag missing payments.

### How do I handle a maintenance request?
1. Acknowledge immediately using `templates/comms/maintenance-ack.md`
2. Triage (emergency/urgent/routine)
3. Contact vendor from `vendors/README.md`
4. Update tenant using `templates/comms/maintenance-update.md`
5. Log expense when complete

### How do I know what deadlines are coming up?
Check `compliance/calendar.md` weekly. The AI and/or `scripts/compliance-check.py` can scan this automatically and flag items due within 30 days.

### Where do I find communication templates?
All templates are in `templates/comms/`. Each one has instructions at the top explaining when to use it and what to fill in.

---

## Compliance

### Is this legal advice?
No. The compliance documents are operational references, not legal advice. Laws vary by state, county, and city, and change frequently. Always consult a qualified attorney for legal decisions.

### How often should I review compliance documents?
At least annually. Set a reminder in your compliance calendar. Laws change, and your documents should be current.

### What if my city has additional requirements?
Many cities layer extra regulations on top of state law (rent control, rental registration, relocation assistance, etc.). Create a city-specific document similar to `examples/oregon/portland-regs.md` and reference it from your compliance files.

---

## Financial

### How do I handle taxes?
Track all income in income.csv and all expenses in expenses.csv. At tax time, these provide the data for Schedule E (federal) and your state return. See `financials/tax/` for 1099 tracking and estimated payment tracking. Work with a CPA for actual filing.

### How do I track depreciation?
Depreciation schedules go in `financials/tax/`. You need: purchase price, land/building value split, and date placed in service. A CPA should set up your initial depreciation schedule.

### Do I need to send 1099s?
If you pay any contractor $600 or more in a calendar year, you must send them a 1099-NEC by January 31. Track payments in `financials/tax/[YEAR]/1099-tracking.csv`. Collect W-9 forms from contractors before their first payment.

---

## Vendors

### How many vendors do I need?
At minimum, have 2 vendors per critical trade (plumbing, electrical, HVAC). This ensures you're never stuck waiting in an emergency. See `vendors/README.md`.

### How do I track vendor performance?
Log every job in `vendors/performance.csv` with quality rating, timeliness, and cost accuracy. Over time this builds a reliable performance history.

---

## Continuity

### What happens if I'm unable to manage the properties?
The `continuity/` folder contains a succession plan: designated successor, credentials checklist, and a personal letter. A physical continuity kit should be stored in a secure location. See `continuity/README.md`.

### Who should be my designated successor?
Typically a co-owner, family member, or trusted person who is willing and able to step in. They need access to the repo, bank accounts, insurance policies, and physical keys.

---

## Troubleshooting

### I made a mistake in a file. Can I undo it?
If you're using git: `git log` to find the last good version, then `git checkout [commit] -- [file]` to restore it. Git preserves the full history of every file.

### My compliance documents are out of date. What do I do?
Research your state's current laws, update the documents, and note the review date at the top. Consider having a lawyer review the updates. Set a recurring calendar reminder to review annually.

### I have multiple properties in different states. How do I handle that?
Create state-specific compliance files for each state (like the Oregon examples in `examples/oregon/`). Each property's README should reference the applicable state and local compliance documents.
