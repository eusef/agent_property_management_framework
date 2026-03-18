# Tax Planning Guide for Rental Property Owners

**Purpose:** Reference guide for the key tax concepts, deductions, and deadlines that apply to residential rental property owners. This is educational guidance, not tax advice. Work with a CPA experienced in rental real estate.

---

## How Rental Income Is Taxed

Rental income is reported on **Schedule E (Form 1040)**. It is classified as **passive income**, which is taxed differently from wages or business income.

**What counts as rental income:**
- Rent payments
- Late fees collected
- Pet fees and deposits (non-refundable portions)
- Application fees
- Lease termination fees
- Any other money received from tenants in connection with the rental

**What counts as rental expenses (deductible):**
- Mortgage interest (not principal)
- Property taxes
- Insurance premiums
- Repairs and maintenance
- Property management fees
- Advertising for vacancies
- Legal and professional fees
- Utilities (if landlord-paid)
- Travel to and from properties (mileage or actual expenses)
- Home office (if you manage from home and meet IRS requirements)
- Depreciation (see below)

---

## Repairs vs. Improvements: The Critical Distinction

This is the single most important tax classification for landlords. Getting it wrong means either overpaying taxes or triggering an audit.

### Repairs (Deduct in Full This Year)

A repair **restores** the property to its prior working condition. It does not add value or extend the useful life.

| Example | Typical Cost | Tax Treatment |
|---------|-------------|---------------|
| Fix a leaky faucet | $150 | Deduct in full |
| Patch drywall | $200 | Deduct in full |
| Replace a broken window pane | $300 | Deduct in full |
| Fix a running toilet | $100 | Deduct in full |
| Repaint a room (same color) | $400 | Deduct in full |
| Replace a garbage disposal | $250 | Deduct in full |

### Improvements (Must Depreciate Over Time)

An improvement **adds value**, extends useful life, or adapts the property to a new use. These must be capitalized and depreciated.

| Example | Typical Cost | Tax Treatment |
|---------|-------------|---------------|
| New roof | $8,000-15,000 | Depreciate |
| New HVAC system | $5,000-10,000 | Depreciate |
| Kitchen remodel | $10,000+ | Depreciate |
| New flooring (entire unit) | $3,000-8,000 | Depreciate |
| Adding a room or deck | Varies | Depreciate |
| New appliance package | $3,000-5,000 | Depreciate |

### De Minimis Safe Harbor ($2,500 Rule)

Items that would normally be improvements but cost **$2,500 or less per item** can be expensed in the current year under the de minimis safe harbor election. You must make this election annually on your tax return.

| Example | Cost | Tax Treatment |
|---------|------|---------------|
| New toilet | $400 | Expense (de minimis) |
| New dishwasher | $600 | Expense (de minimis) |
| New water heater (basic) | $1,200 | Expense (de minimis) |
| Smart thermostat | $250 | Expense (de minimis) |

**In the PM_FRAMEWORK:** Every expense in `expenses.csv` should have the `tax_treatment` column set to: `repair`, `improvement`, `de_minimis`, or `expense`.

---

## Depreciation

Depreciation is a "phantom expense" that reduces your taxable income without costing you any cash. It accounts for the wear and tear on the building over time.

**Residential rental property depreciation period:** 27.5 years

**What you depreciate:** The building value only (not the land). If you bought a property for $300,000 and the land is worth $75,000, you depreciate $225,000 over 27.5 years = approximately $8,182/year in deductions.

**Improvements** to the property are also depreciated, typically over 27.5 years (same as the building) unless a shorter life applies.

**Depreciation recapture:** When you sell the property, the IRS "recaptures" the depreciation you claimed by taxing it at up to 25%. This is unavoidable, but strategies exist to defer it (see 1031 exchange below).

---

## Active Participation Loss Deduction

If you **actively participate** in managing your rental property (which you do if you're using this framework), you can deduct up to **$25,000 in rental losses** against your ordinary income (wages, salary).

**Requirements:**
- You own at least 10% of the property
- You make management decisions (approve tenants, set rent, approve repairs)
- Your Modified Adjusted Gross Income (MAGI) is under $100,000 (full deduction) to $150,000 (phase-out)

This is a significant tax benefit for owner-managers with moderate incomes.

---

## Key Tax Deadlines

| Deadline | Item | Notes |
|----------|------|-------|
| January 31 | File 1099-NEC | For all unincorporated contractors paid $600+ in the prior year |
| April 15 | Federal tax return (1040 + Schedule E) | Or file extension (Form 4868) |
| April 15 | Q1 estimated tax payment (1040-ES) | If you expect to owe $1,000+ |
| April 15 | State tax return | Check your state's deadline |
| June 15 | Q2 estimated tax payment | |
| September 15 | Q3 estimated tax payment | |
| January 15 (following year) | Q4 estimated tax payment | |

**These deadlines are tracked in `compliance/calendar.md`.**

---

## 1099-NEC Filing Requirements

You must file a 1099-NEC for any **unincorporated** contractor (sole proprietor or partnership) you paid **$600 or more** during the calendar year.

**Process:**
1. Collect a W-9 from every contractor before making the first payment
2. Track total payments per contractor throughout the year (the `vendors/performance.csv` and property `expenses.csv` files are your source data)
3. By January 31: file 1099-NEC with the IRS and provide a copy to the contractor
4. Track filing status in `financials/tax/[YEAR]/1099-tracking.csv`

**You do NOT need to file 1099-NEC for:**
- Corporations (S-corp or C-corp)
- Payments under $600/year to a single contractor
- Credit card payments (the card company handles reporting)

---

## Exit Strategies

### 1031 Exchange (Like-Kind Exchange)
Sell a rental property and reinvest the proceeds in another rental property. Defer ALL capital gains and depreciation recapture taxes indefinitely.

**Key rules:**
- Must identify replacement property within 45 days of sale
- Must close on replacement within 180 days of sale
- Must use a qualified intermediary (cannot touch the funds yourself)
- Properties must be "like-kind" (any real property for any real property)

### Installment Sale
Spread the sale proceeds over multiple years to reduce the tax hit in any single year. Useful when selling directly to a buyer willing to finance.

### Step-Up in Basis at Death
If you hold rental property until death, your heirs receive a "stepped-up" basis equal to the fair market value at the date of death. All accumulated depreciation recapture is eliminated.

---

## Record Keeping for Taxes

Per `compliance/records-retention.md`:
- Keep tax returns, 1099s, income records, expense records, and bank statements for **7 years**
- Keep property purchase documents, capital improvement records, and depreciation schedules for the **life of ownership + 7 years**
- Keep all receipts for expenses over $75 (IRS requirement)

---

## Working With a CPA

Every landlord should have a CPA experienced specifically in residential rental real estate. Key questions to ask a potential CPA:

1. How many landlord clients do you currently serve?
2. Are you familiar with Schedule E and passive activity rules?
3. Do you handle 1099 filing?
4. Can you advise on depreciation strategy and cost segregation?
5. What is your fee structure?

Add your CPA to the Professional Services section in `vendors/README.md`.

---

*This guide covers the fundamentals. Tax law changes frequently. Review annually with your CPA and update this document as needed.*
