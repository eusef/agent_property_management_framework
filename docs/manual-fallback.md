# Manual Fallback Procedures

**Purpose:** Run the property management business when AI (Claude/other) is unavailable. This document covers every critical function using only the files in this repo, a phone, and email.
**When to use:** AI service outage, internet outage, or any situation where Claude is not accessible.
**Last updated:** [DATE]

---

## Quick Reference: What to Do Right Now

If AI just went down and you need to act:

1. Open `DASHBOARD.md` for current portfolio status
2. Open `compliance/calendar.md` for upcoming deadlines
3. Open the property README for property details and contacts
4. Open `vendors/README.md` for contractor phone numbers
5. Open `docs/emergency-procedures.md` if there's an emergency

---

## 1. Rent Collection (1st of each month)

**Normal flow:** AI checks income.csv and drafts reminders.

**Manual flow:**
- On the 1st: check bank account for rent deposit
- If received: add a row to the property's `financials/income.csv` with date, tenant, amount, method, and notes
- If NOT received by the 3rd: send a friendly reminder using the template in `templates/comms/rent-reminder.md` (Day 3 version)
- If NOT received by the 5th: send the Day 5 version
- If NOT received by the 10th: send the Day 10 version and consult `compliance/eviction.md`

---

## 2. Maintenance Requests

**Normal flow:** AI triages, suggests vendor, drafts response.

**Manual flow:**
1. Tenant contacts you with an issue
2. Determine urgency:
   - **Emergency** (no heat, flooding, gas leak, fire, sewage, security): Act immediately. Call the appropriate vendor from `vendors/README.md`. You can spend any amount. Document after.
   - **Urgent** (broken appliance, plumbing leak, no hot water): Respond within 24 hours. If under $250, authorize repair directly.
   - **Routine** (cosmetic, minor): Respond within 48 hours. Schedule at convenience.
3. Acknowledge the request using `templates/comms/maintenance-ack.md`
4. Call vendor, get estimate
5. If estimate < $250: approve and schedule
6. If estimate $250-$500: review estimate, then approve
7. If estimate > $500: get at least 2 quotes before deciding
8. Send update to tenant using `templates/comms/maintenance-update.md`
9. Log in the property's `financials/expenses.csv` after work is complete
10. Create a maintenance record in the property's `maintenance/` folder

---

## 3. Compliance Deadlines

**Normal flow:** AI scans calendar weekly and alerts you.

**Manual flow:**
- Open `compliance/calendar.md` at least weekly
- Check the "One-Time / Event-Triggered Deadlines" section for anything marked ACTION NEEDED
- Check "Recurring Deadlines" for items due this month
- Set phone reminders for anything due within 30 days

**Critical recurring deadlines:**
- 1st of month: rent collection
- Quarterly: estimated tax payments (Apr 15, Jun 15, Sep 15, Jan 15)
- Annual: insurance renewal alert (60 days before renewal date)
- Annual: 1099-NEC filing (Jan 31)
- Annual: tax returns (Apr 15)

---

## 4. Tenant Communication

**Normal flow:** AI drafts, owner reviews and sends.

**Manual flow:**
- All templates are in `templates/comms/`
- Each template has instructions at the top explaining when to use it
- Available templates: rent-reminder, maintenance-ack, maintenance-update, lease-renewal, move-in-welcome, move-out-notice, inspection-notice
- Fill in the bracketed fields and send via email
- Log all communications (save sent emails)

---

## 5. Monthly Financial Close

**Normal flow:** AI generates P&L from CSVs.

**Manual flow:**
1. Open the property's `financials/income.csv` and confirm all rent received is logged
2. Open the property's `financials/expenses.csv` and confirm all expenses are logged
3. Calculate: Net income = total income - total expenses for the month
4. File any new receipts (digital copies in expenses, physical in file)
5. If a vendor was paid $600+ YTD, check `financials/tax/[YEAR]/1099-tracking.csv` and update

---

## 6. Insurance Claim

**Manual flow:**
1. Document the damage (photos, written description, date/time)
2. Call insurance carrier: [CARRIER_PHONE]
3. Policy #: [POLICY_NUMBER]
4. Named insured: [OWNER_NAME]
5. Deductible: $[AMOUNT]
6. Note coverage exclusions (check your policy for flood, earthquake, etc.)
7. Log the claim in `compliance/insurance-tracker.md` under Claims History

---

## 7. Lease Renewal / Non-Renewal

**Manual flow:**
1. Check lease end date in `compliance/calendar.md` (Lease Expirations section)
2. Send notice per your state's required timeline before lease end
3. Use templates in `templates/comms/lease-renewal.md`
4. If raising rent: check your state's notice requirements and any rent control limits
5. Consult `compliance/landlord-tenant-law.md` for current rules

---

## 8. Vacancy / New Tenant

**Manual flow:**
1. Follow `templates/checklists/move-out-inspection.md` when current tenant leaves
2. Return security deposit within your state's deadline (see `compliance/security-deposits.md`)
3. Follow `docs/onboarding-a-tenant.md` for new tenant process
4. Follow `templates/checklists/tenant-screening.md` for applications
5. Follow `templates/checklists/move-in-inspection.md` for new move-in

---

## 9. Emergency Procedures

See `docs/emergency-procedures.md` for the full emergency playbook.

---

## 10. Quarterly Checklist (Do These Even Without AI)

- [ ] Review compliance/calendar.md for upcoming deadlines
- [ ] Confirm all rent payments received and logged
- [ ] Confirm all expenses logged with receipts
- [ ] Review vendor database for any needed updates
- [ ] Check 1099 tracking for vendors approaching $600 threshold
- [ ] Review insurance coverage (annually, or if property changes)
- [ ] Check estimated tax payments due
- [ ] Review records-retention.md and archive/purge as needed

---

## Key File Locations

| What You Need | Where to Find It |
|---------------|-----------------|
| Property details | properties/{property-slug}/README.md |
| Vendor phone numbers | vendors/README.md |
| Compliance deadlines | compliance/calendar.md |
| Landlord-tenant law | compliance/landlord-tenant-law.md |
| Eviction procedures | compliance/eviction.md |
| Communication templates | templates/comms/ |
| Checklists | templates/checklists/ |
| Tax info | financials/tax/[YEAR]/ |
| Insurance details | compliance/insurance-tracker.md |
| Records retention policy | compliance/records-retention.md |
| Emergency procedures | docs/emergency-procedures.md |

---

*This document should be updated any time a workflow or automation is added or changed.*
