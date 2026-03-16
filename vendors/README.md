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
3. References from other landlords if possible
4. Get at least 2 quotes for any job over $500
5. Track performance in vendors/performance.csv after each job
6. Collect W-9 before first payment (needed for 1099 if total payments exceed $600/year)

---

## Notes

- Individual vendor detail files go in vendors/{vendor-slug}.md
- Performance history tracked in vendors/performance.csv
