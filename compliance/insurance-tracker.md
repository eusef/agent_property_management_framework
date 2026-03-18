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

---

## Coverage Targets and Best Practices

### Recommended Minimum Coverage

| Coverage | Target |
|----------|--------|
| Liability per property | $500,000-$1,000,000 per occurrence |
| Aggregate liability | $2,000,000 |
| Umbrella policy | $1,000,000+ (costs only a few hundred dollars/year) |
| Deductible strategy | $2,500-$5,000 per property (higher deductible = lower premiums) |
| Policy type | **Landlord policy** (NOT homeowner's policy) |

### Policy Structure

Use a **separate policy per property**, not a commercial blanket policy. A claim on one property won't expose the others, and tenants cannot discover your full portfolio through policy records.

### Claims Philosophy

Insurance is for **catastrophic events only**. Never file small claims. Each claim raises premiums and risks policy cancellation. If the repair cost is close to your deductible, pay out of pocket.

### Tenant Renter's Insurance

Require as a lease condition. Verify proof of active policy before handing over keys. Track expiration dates above. If coverage lapses, issue a notice to comply (see `templates/comms/notice-to-comply.md`).

### Negligence Voids Coverage

Failure to maintain the property can void coverage on related claims (ignored roof leaks, faulty wiring, unaddressed mold). Proactive maintenance protects your coverage. See `compliance/seasonal-maintenance.md`.

---

*Populate with actual policy data during property onboarding. Review coverage at each annual property review.*
