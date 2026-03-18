# Compliance Calendar

**Purpose:** Single view of all compliance deadlines. Scanned weekly by compliance-check.py to generate alerts.
**Format:** Sorted by date. Recurring items show next occurrence.

---

## Recurring Deadlines

### Monthly

| Item | Next Due | Property | Notes |
|------|----------|----------|-------|
| Rent collection check | 1st of each month | [PROPERTY_NAME] | Check income.csv, begin reminder sequence if unpaid by 5th |

### Quarterly

| Item | Next Due | Property | Notes |
|------|----------|----------|-------|
| Federal estimated tax payment (1040-ES) | [NEXT_DUE_DATE] | [OWNER_NAME] | See compliance/tax-guide.md. Quarterly: Apr 15, Jun 15, Sep 15, Jan 15 |
| [YOUR_STATE] estimated tax payment | [NEXT_DUE_DATE] | [OWNER_NAME] | Same schedule as federal |
| Market rent analysis | [NEXT_DUE_DATE] | [PROPERTY_NAME] | Research comps, evaluate adjustments. Check [YOUR_STATE] rent control limits. |
| Records retention review | [NEXT_DUE_DATE] | All | Review records past retention period, shred PII -- see compliance/records-retention.md |

### Semi-Annual

| Item | Next Due | Property | Notes |
|------|----------|----------|-------|
| Property inspection (interior) | [NEXT_DUE_DATE] | [PROPERTY_NAME] | [YOUR_STATE_NOTICE_PERIOD] written notice to tenant required. Reasonable hours only. |
| Gutter cleaning | [MONTH] + [MONTH] each year | [PROPERTY_NAME] | Frequency depends on climate and tree coverage |

### Annual -- Tax & Business (Calendar Year)

| Item | Due Date | Property | Notes |
|------|----------|----------|-------|
| 1099-NEC filing | Jan 31 | [OWNER_NAME] | File for all contractors paid $600+ previous year |
| [YOUR_CITY] Business Tax Return | [DUE_DATE] | [PROPERTY_NAME] | [YOUR_CITY business tax details, if applicable] |
| Federal tax return (1040 + Schedule E) | Apr 15 | [OWNER_NAME] | Rental income on Schedule E |
| [YOUR_STATE] state tax return | Apr 15 | [OWNER_NAME] | [YOUR_STATE tax form] |

### Annual -- Property Maintenance (Seasonal)

See `compliance/seasonal-maintenance.md` for the full seasonal guide with detailed task descriptions by season.

| Item | Target Month | Property | Notes |
|------|-------------|----------|-------|
| HVAC A/C servicing | April | [PROPERTY_NAME] | Before cooling season. Replace filters. |
| Exterior inspection | April | [PROPERTY_NAME] | Walk entire property: siding, foundation, trim, windows. Note winter damage. |
| Gutter cleaning (spring) | March | [PROPERTY_NAME] | Clear debris from fall/winter. |
| Test sprinkler system | April | [PROPERTY_NAME] | Check all heads, adjust coverage, check for leaks. |
| Roof inspection | April | [PROPERTY_NAME] | Missing/damaged shingles, flashing, moss. |
| Smoke/CO detector test (spring) | April | [PROPERTY_NAME] | Replace batteries. Replace units older than 10 years. |
| Pressure wash | May | [PROPERTY_NAME] | Driveway, walkways, siding. Climate-dependent. |
| Dryer vent cleaning | June | [PROPERTY_NAME] | Fire prevention. Professional cleaning recommended. |
| Furnace inspection + filter change | October | [PROPERTY_NAME] | Before heating season. Check for CO leaks. |
| Gutter cleaning (fall) | November | [PROPERTY_NAME] | After leaf drop, before rain/snow. Critical. |
| Winterize outdoor faucets and pipes | November | [PROPERTY_NAME] | Before first freeze. Disconnect hoses, insulate spigots. |
| Smoke/CO detector test (fall) | October | [PROPERTY_NAME] | Semi-annual. Replace batteries. |
| Weather stripping inspection | October | [PROPERTY_NAME] | Doors and windows. Replace if deteriorated. |

### Annual -- Insurance

| Item | Due Date | Property | Notes |
|------|----------|----------|-------|
| Insurance review (start shopping/comparing) | [DATE] | [PROPERTY_NAME] | 60 days before renewal |

### Ongoing

| Item | Frequency | Property | Notes |
|------|-----------|----------|-------|
| Collect W-9 from new vendors | Before first payment | All | Required for 1099 filing |
| Storm monitoring | [SEASON] | All | Emergency response only |

---

## One-Time / Event-Triggered Deadlines

| Date | Item | Property | Status | Notes |
|------|------|----------|--------|-------|
| [DATE] | [DESCRIPTION] | [PROPERTY] | [STATUS] | [NOTES] |

---

## Lease Expirations

| Tenant | Property | Lease End | 90-Day Notice Deadline | Status |
|--------|----------|-----------|----------------------|--------|
| [TENANT_NAME] | [PROPERTY_NAME] | [DATE] | [DATE] | [STATUS] |

---

## Insurance Renewals

| Policy | Property | Carrier | Renewal Date | 60-Day Alert Date | Status |
|--------|----------|---------|-------------|-------------------|--------|
| [POLICY_#] | [PROPERTY_NAME] | [CARRIER] | [DATE] | [DATE] | [STATUS] |

---

## Security Deposit Deadlines

Active only when a tenant moves out. [YOUR_STATE_DEADLINE]-day clock starts at move-out.

| Tenant | Property | Move-Out Date | [YOUR_STATE_DEADLINE]-Day Deadline | Status |
|--------|----------|--------------|----------------|--------|
| (none active) | | | | |

---

*This file is scanned by compliance-check.py weekly. Items due within 30 days appear in DASHBOARD.md. Items due within 7 days are flagged URGENT.*
