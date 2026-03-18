# Getting Started

**Purpose:** Quick start guide for setting up the PM Framework for your rental properties.

---

## Prerequisites

### Technical
- Git installed on your machine
- A text editor (VS Code, Sublime, or any markdown editor)
- An AI assistant (Claude, ChatGPT, etc.) for AI-assisted workflows (optional but recommended)
- Basic comfort with markdown files and CSV spreadsheets

### Business Setup (Complete Before Your First Tenant)

1. **Set up separate bank accounts**
   - One **checking account** for all rental income and expenses (never use personal accounts)
   - One **savings account** for security deposits (required by law in most states - never commingle with operating funds)

2. **Set up a business identity**
   - Get a dedicated business phone number (Google Voice is free and provides up to 30 numbers with voicemail transcription)
   - Set up a dedicated business email address (not your personal email)
   - Get a PO Box or use a registered agent address (never give tenants your home address)
   - Present yourself as the "Property Manager" rather than the "Landlord" - this creates professional distance and simplifies enforcement

3. **Build your professional team** (at minimum)
   - Real estate attorney specializing in landlord-tenant law in your state
   - CPA with specific experience in residential rental property
   - Insurance agent knowledgeable about landlord policies
   - See `vendors/README.md` Professional Services section

4. **Get proper insurance**
   - Landlord policy (NOT homeowner's) on each rental property
   - Umbrella policy ($1M+ coverage for a few hundred dollars/year)
   - See `compliance/insurance-tracker.md` for coverage targets

5. **Gather all forms before you need them**
   - Lease agreement (reviewed by your attorney)
   - All templates in `templates/` are ready to customize
   - State-specific forms (see `templates/forms/`)

See `docs/policy-binder.md` for a consolidated reference of all your standing business policies.

---

## Step 1: Clone the Repository

```bash
git clone [YOUR_REPO_URL] pm-framework
cd pm-framework
```

## Step 2: Run the Setup Script

```bash
chmod +x setup.sh
./setup.sh
```

The setup script will:
- Create the directory structure for your first property
- Initialize configuration files
- Set up the properties/ folder with the correct layout

## Step 3: Configure Your Jurisdiction

1. Open `compliance/landlord-tenant-law.md` and fill in your state's laws
2. Open `compliance/security-deposits.md` and fill in your state's deposit rules
3. Open `compliance/eviction.md` and fill in your state's eviction procedures
4. Review `compliance/fair-housing.md` and add your state's additional protected classes
5. Check `examples/oregon/` for a worked example of how a completed set looks

## Step 4: Add Your First Property

Follow the guide in `docs/adding-a-property.md`. In summary:

1. Create a property directory: `properties/[property-slug]/`
2. Copy the property README template and fill in property details
3. Set up the financials subdirectory with income.csv and expenses.csv
4. Add the property to your compliance calendar
5. Add the property to your insurance tracker

## Step 5: Set Up Vendors

1. Open `vendors/README.md` and add your emergency vendors (plumber, electrician, HVAC)
2. Ensure you have at least 2 vendors per critical trade
3. Collect W-9 forms from every contractor before first payment

## Step 6: Set Up Compliance Calendar

1. Open `compliance/calendar.md` and fill in your deadlines
2. Add insurance renewal dates
3. Add tax payment deadlines
4. Add lease expiration dates
5. Set up recurring maintenance items based on your climate

## Step 7: Review Templates

Browse the `templates/` folder to familiarize yourself with available templates:
- `templates/comms/` -- Tenant communication templates (rent reminders, maintenance updates, etc.)
- `templates/checklists/` -- Inspection checklists, screening checklists, review checklists
- `templates/forms/` -- Official form inventory and sources

---

## Daily Operations

Once set up, your typical workflow looks like:

1. **Check the dashboard** for upcoming deadlines and action items
2. **Process any tenant communications** using templates in `templates/comms/`
3. **Log income and expenses** in the property's CSV files
4. **Track maintenance requests** and vendor work
5. **Review compliance calendar** weekly for upcoming deadlines

See `docs/how-it-works.md` for a full architecture overview.

---

## Need Help?

- `docs/faq.md` -- Frequently asked questions
- `docs/manual-fallback.md` -- How to operate without AI assistance
- `docs/emergency-procedures.md` -- What to do in an emergency
