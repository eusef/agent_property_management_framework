# Adding a New Property

**Purpose:** Step-by-step guide for adding a new property to the framework.

---

## Step 1: Create the Directory Structure

Create a new property folder. Use a slug (short, lowercase, hyphenated name) for the directory:

```bash
mkdir -p properties/{property-slug}/financials
mkdir -p properties/{property-slug}/maintenance
mkdir -p properties/{property-slug}/tenants
mkdir -p properties/{property-slug}/inspections
```

Example: `properties/123-main-st/`

Or run the setup script if available:
```bash
./setup.sh add-property "123 Main St"
```

---

## Step 2: Create the Property README

Create `properties/{property-slug}/README.md` with key property details:

```markdown
# [Property Address]

## Quick Reference

| Field | Value |
|-------|-------|
| Address | [Full address] |
| Type | [Single family / Duplex / Condo / etc.] |
| Year built | [Year] |
| Sq ft | [Square footage] |
| Bedrooms | [Number] |
| Bathrooms | [Number] |
| Purchase date | [Date] |
| Purchase price | $[Amount] |
| Current rent | $[Amount]/mo |
| Mortgage lender | [Lender name] |
| Insurance carrier | [Carrier name] |
| Insurance policy # | [Policy number] |

## Current Tenant

| Field | Value |
|-------|-------|
| Name | [Tenant name] |
| Lease start | [Date] |
| Lease end | [Date] |
| Monthly rent | $[Amount] |
| Security deposit | $[Amount] |
| Payment method | [Zelle/Check/etc.] |

## Key Systems

| System | Details | Age | Condition |
|--------|---------|-----|-----------|
| Roof | [Type] | [Years] | [Good/Fair/Poor] |
| HVAC | [Type] | [Years] | [Good/Fair/Poor] |
| Water heater | [Type, gallons] | [Years] | [Good/Fair/Poor] |
| Electrical panel | [Amps] | [Years] | [Good/Fair/Poor] |
| Plumbing | [Material] | [Years] | [Good/Fair/Poor] |

## Emergency Shutoffs

| Utility | Location |
|---------|----------|
| Water main | [Location] |
| Gas shutoff | [Location] |
| Electrical panel | [Location] |
| Sewer cleanout | [Location] |
```

---

## Step 3: Set Up Financial Tracking

Create `properties/{property-slug}/financials/income.csv`:
```csv
date,tenant,amount,method,notes
```

Create `properties/{property-slug}/financials/expenses.csv`:
```csv
date,vendor,category,description,amount,receipt,notes
```

---

## Step 4: Update Portfolio-Level Files

1. **DASHBOARD.md** -- Add the property to the portfolio overview
2. **compliance/calendar.md** -- Add:
   - Insurance renewal date
   - Lease expiration date
   - Property-specific maintenance items (seasonal schedule)
   - Any local tax or registration deadlines
3. **compliance/insurance-tracker.md** -- Add the property's insurance details
4. **financials/summary.csv** -- Add a row for the property

---

## Step 5: Document Existing Conditions

If you have an existing property (not a new purchase):

1. Gather any existing inspection reports and save to `properties/{property-slug}/inspections/`
2. Document current condition of key systems in the README
3. Take photos of the property and note their storage location
4. If there's an existing tenant, document their lease details

If this is a new purchase:

1. Save the purchase inspection report to `inspections/`
2. Complete the move-in inspection checklist (`templates/checklists/move-in-inspection.md`)
3. Document the property's condition as your baseline

---

## Step 6: Vendor Setup

Review `vendors/README.md` and confirm you have:
- At least 2 vendors per critical trade (plumbing, electrical, HVAC) that serve this property's area
- Emergency contact numbers for this property's location
- W-9 forms collected from all contractors

---

## Step 7: Compliance Review

- [ ] Property registered with city/county (if required)
- [ ] Business license obtained (if required)
- [ ] Insurance coverage adequate (see compliance/insurance-tracker.md checklist)
- [ ] Lease reviewed by attorney
- [ ] Security deposit in trust account
- [ ] All required disclosures provided to tenant
- [ ] Property meets habitability standards (see compliance/landlord-tenant-law.md)
- [ ] Smoke/CO detectors installed and working

---

## Checklist Summary

- [ ] Directory structure created
- [ ] Property README completed
- [ ] Financial CSVs initialized
- [ ] DASHBOARD.md updated
- [ ] Compliance calendar updated
- [ ] Insurance tracker updated
- [ ] Financials summary updated
- [ ] Existing conditions documented
- [ ] Vendors confirmed for this area
- [ ] Compliance review completed
