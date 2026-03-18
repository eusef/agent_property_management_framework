# Vendor Database

**Purpose:** Master list of contractors and service providers. Organized by trade with ratings, rates, and backup contacts.
**Rule:** Always have at least 2 vendors per critical trade (plumbing, electrical, HVAC) so you're never stuck waiting.
**Last updated:** [DATE]

---

## Emergency Vendors (24-hour availability)

| Trade | Primary | Phone | Backup | Phone | Notes |
|-------|---------|-------|--------|-------|-------|
| Plumber | [VENDOR_NAME] | [PHONE] | [VENDOR_NAME] | [PHONE] | |
| Electrician | [VENDOR_NAME] | [PHONE] | [VENDOR_NAME] | [PHONE] | |
| HVAC | [VENDOR_NAME] | [PHONE] | [VENDOR_NAME] | [PHONE] | |
| Locksmith | [VENDOR_NAME] | [PHONE] | [VENDOR_NAME] | [PHONE] | |

---

## Regular Vendors

| Trade | Vendor | Phone | Email | Total Spent | License # | Notes |
|-------|--------|-------|-------|-------------|-----------|-------|
| [TRADE] | [VENDOR_NAME] | [PHONE] | [EMAIL] | $[AMOUNT] | [LICENSE] | [NOTES] |

---

## Professional Services

| Service | Provider | Phone | Email | Rate | Notes |
|---------|----------|-------|-------|------|-------|
| Lawyer (landlord-tenant) | TBD | | | | Need to find [YOUR_STATE] L-T specialist |
| Accountant/CPA | TBD | | | | Need for tax filing, depreciation |
| Insurance agent | [CARRIER] | [PHONE] | [WEBSITE] | | Policy [POLICY_#] |
| Property inspector | TBD | | | | |

---

## Gaps to Fill

These trades need at least one reliable contact before self-managing:

| Trade | Priority | Action |
|-------|----------|--------|
| Plumber (emergency) | HIGH | Need 24hr option |
| HVAC | HIGH | Need direct contact info |
| Electrician | MEDIUM | Verify they do residential |
| Tree Service | MEDIUM | Regular need - get 2 quotes |
| General Handyman | LOW | For small jobs under $250 |

---

## Vendor Selection Criteria

When choosing a new vendor:
1. Licensed and insured (verify - don't take their word for it)
2. State contractor license (required in most states for work over a certain amount)
3. Request Certificate of Insurance and ask to be listed as additional insured (for jobs over $1,000)
4. References from other landlords if possible
5. Get at least 2-3 quotes for any job over $500
6. Track performance in vendors/performance.csv after each job
7. Collect W-9 before first payment (needed for 1099 if total payments exceed $600/year)

---

## Working With Contractors - Payment and Contract Rules

### Payment Terms

- **NEVER pay 100% upfront.** This is a non-negotiable rule.
- Standard payment schedule for jobs over $500:
  - 1/3 at project start
  - 1/3 at midpoint
  - 1/3 upon satisfactory completion
- For small jobs under $500: 50% at start, 50% at completion is acceptable
- For emergency repairs: payment upon completion is standard

### Bidding Requirements

| Job Size | Requirement |
|----------|-------------|
| Under $300 | 1 trusted vendor is fine |
| $300-$1,000 | Get at least 2 quotes |
| Over $1,000 | Get at least 3 quotes |

### Contract Essentials

For any job over $500, get these in writing before work begins:
- Scope of work (specific, detailed description)
- Materials specified (brand, grade, color - not "contractor's choice")
- Fixed price (avoid cost-plus bids - they can balloon)
- Timeline (start date, estimated completion, penalties for delay if applicable)
- Payment schedule
- Warranty on work
- Cleanup expectations

### Vendor Onboarding Checklist

Before making the first payment to any new vendor:
- [ ] W-9 collected and filed
- [ ] License number verified with state licensing board
- [ ] Insurance certificate received (for trades that require it)
- [ ] Added to vendor database (Regular Vendors table above)
- [ ] Added to vendors/performance.csv

### 1099 Tracking

Any unincorporated vendor (sole proprietor, partnership) paid $600+ in a calendar year requires a 1099-NEC filing by January 31. Track cumulative payments per vendor throughout the year. See `docs/tax-planning.md` and `financials/tax/[YEAR]/1099-tracking.csv`.

---

## Notes

- Individual vendor detail files go in vendors/{vendor-slug}.md
- Performance history tracked in vendors/performance.csv
- Every maintenance visit is also a property inspection - vendor should note the general condition of the unit and report any visible lease violations
