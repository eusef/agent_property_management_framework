# Insurance Tracker

**Purpose:** Track all insurance policies, renewal dates, and coverage details. Scanned by compliance-check.py for renewal alerts (60 days before expiration).

---

## Landlord Policies

| Property | Carrier | Policy # | Coverage Type | Annual Premium | Effective | Expires | 60-Day Alert |
|----------|---------|----------|--------------|----------------|-----------|---------|-------------|
| [PROPERTY_NAME] | [CARRIER] | [POLICY_#] | Rental Property | $[AMOUNT] | [DATE] | [DATE] | [DATE] |

---

## Umbrella / Liability Policy

| Carrier | Policy # | Coverage Amount | Annual Premium | Effective | Expires |
|---------|----------|----------------|----------------|-----------|---------|
| TBD | TBD | TBD | $ TBD | TBD | TBD |

---

## Tenant Renter's Insurance

| Tenant | Property | Required? | Proof on File? | Carrier | Expires | Notes |
|--------|----------|-----------|---------------|---------|---------|-------|
| [TENANT_NAME] | [PROPERTY_NAME] | [Yes/No] | [ ] | TBD | TBD | |

---

## Coverage Checklist (Per Property)

Review annually at insurance renewal:

- [ ] Dwelling coverage adequate for replacement cost
- [ ] Other structures coverage adequate
- [ ] Liability coverage minimum $500K per occurrence
- [ ] Medical payments to others included
- [ ] Water backup/sump pump overflow endorsement
- [ ] Loss of rental income coverage included
- [ ] Natural disaster coverage appropriate for area (flood, earthquake, wildfire, hurricane)
- [ ] Vandalism and malicious mischief covered
- [ ] Named landlord (not homeowner) policy -- confirmed rental property policy
- [ ] Deductible amount acceptable: $[AMOUNT]

---

## Claims History

| Date | Property | Description | Claim # | Amount | Status | Notes |
|------|----------|-------------|---------|--------|--------|-------|
| (none) | | | | | | |

---

## Annual Premium History

Track for cost trend analysis:

| Year | Property | Carrier | Premium | Change vs Prior |
|------|----------|---------|---------|----------------|
| [YEAR] | [PROPERTY_NAME] | [CARRIER] | $[AMOUNT] | - |

---

*Populate with actual policy data during property onboarding.*
