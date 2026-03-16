# Onboarding a New Tenant

**Purpose:** Step-by-step guide for onboarding a new tenant, from application through move-in.

---

## Phase 1: Marketing and Applications

### Prepare the Unit
- [ ] Complete any needed repairs or upgrades
- [ ] Clean the unit thoroughly (professional cleaning recommended)
- [ ] Take marketing photos
- [ ] Determine rental price (check market comps)

### List the Property
- [ ] Write listing description (follow fair housing guidelines -- see `compliance/fair-housing.md`)
- [ ] Post to rental listing sites (Zillow, Apartments.com, Craigslist, etc.)
- [ ] Include: rent amount, deposit amount, screening criteria, pet policy, lease terms
- [ ] If your city requires it, post screening criteria publicly before accepting applications

### Accept Applications
- [ ] Use a consistent application form for all applicants
- [ ] Collect screening fee (cannot exceed actual costs in many states -- check yours)
- [ ] Provide screening fee receipt

---

## Phase 2: Screening

Follow `templates/checklists/tenant-screening.md` for every applicant. Apply identical criteria to all.

### Key Steps
- [ ] Verify income (pay stubs, employment verification, tax returns)
- [ ] Run credit check (with applicant authorization)
- [ ] Run background check (with applicant authorization)
- [ ] Check eviction history
- [ ] Contact previous landlords
- [ ] Verify identity (government-issued photo ID)

### Decision
- [ ] Document decision and rationale
- [ ] If approved: proceed to lease signing
- [ ] If denied: send adverse action notice (required -- include reason and screening company info)
- [ ] Keep all applications on file for at least 3 years

---

## Phase 3: Lease Signing

### Prepare Lease Documents
- [ ] Rental agreement (use attorney-reviewed form -- see `templates/forms/README.md`)
- [ ] Any required addenda (pet addendum, lead paint disclosure, etc.)
- [ ] Required disclosures per your state/city
- [ ] Move-in inspection checklist (`templates/checklists/move-in-inspection.md`)

### At Lease Signing
- [ ] Review all lease terms with tenant
- [ ] Both parties sign all documents
- [ ] Collect first month's rent
- [ ] Collect security deposit
- [ ] Deposit security deposit into trust account (must be separate from operating funds)
- [ ] Provide tenant with copies of all signed documents
- [ ] Provide tenant with required disclosures
- [ ] Provide copies of keys (document how many of each)

---

## Phase 4: Move-In

### Move-In Inspection
- [ ] Complete move-in inspection with tenant present (`templates/checklists/move-in-inspection.md`)
- [ ] Take timestamped photos of every room
- [ ] Both parties sign the inspection report
- [ ] Provide tenant with copy of inspection report and photos
- [ ] Tell tenant they have 7 days to report anything missed

### Welcome Package
- [ ] Send welcome letter (`templates/comms/move-in-welcome.md`) including:
  - Your contact information (regular and emergency)
  - Rent amount, due date, and payment method
  - Utility responsibilities and setup instructions
  - Property information (trash day, parking, mail, etc.)
  - Maintenance request process
  - Renter's insurance requirements/recommendation

### System Updates
- [ ] Create tenant record in `properties/{slug}/tenants/{tenant-name}/`
- [ ] Update property README with current tenant information
- [ ] Add lease expiration to `compliance/calendar.md`
- [ ] Update `DASHBOARD.md`
- [ ] Log security deposit in financial records
- [ ] Log first month's rent in `properties/{slug}/financials/income.csv`
- [ ] File all signed documents

---

## Phase 5: First 30 Days

### Follow-Up
- [ ] Check in with tenant after 1 week (quick text/email: "How's everything going?")
- [ ] Address any issues reported promptly
- [ ] Confirm utility transfers completed
- [ ] Verify renter's insurance proof received (if required)

### Documentation
- [ ] All lease documents filed
- [ ] Move-in inspection filed in `properties/{slug}/inspections/`
- [ ] Photos stored and backed up
- [ ] Tenant contact information recorded
- [ ] Emergency contact for tenant recorded

---

## Common Pitfalls to Avoid

1. **Inconsistent screening.** Apply the same criteria to every applicant. Document your criteria before you start.
2. **Missing disclosures.** Research what your state and city require. Missing a required disclosure can void lease terms.
3. **No move-in inspection.** This is your baseline for security deposit deductions. Without it, courts side with tenants.
4. **Commingling deposits.** Security deposits must go in a separate trust account. Not optional.
5. **Skipping the welcome letter.** Sets a professional tone and prevents 90% of "where do I..." questions.
