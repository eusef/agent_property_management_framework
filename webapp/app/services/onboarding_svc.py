"""Onboarding service: create property directories, populate templates, update context files."""
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

from app.config import settings
from app.services import config_svc

# US States + DC
US_STATES = [
    ("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"),
    ("CA", "California"), ("CO", "Colorado"), ("CT", "Connecticut"), ("DE", "Delaware"),
    ("DC", "District of Columbia"), ("FL", "Florida"), ("GA", "Georgia"), ("HI", "Hawaii"),
    ("ID", "Idaho"), ("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"),
    ("KS", "Kansas"), ("KY", "Kentucky"), ("LA", "Louisiana"), ("ME", "Maine"),
    ("MD", "Maryland"), ("MA", "Massachusetts"), ("MI", "Michigan"), ("MN", "Minnesota"),
    ("MS", "Mississippi"), ("MO", "Missouri"), ("MT", "Montana"), ("NE", "Nebraska"),
    ("NV", "Nevada"), ("NH", "New Hampshire"), ("NJ", "New Jersey"), ("NM", "New Mexico"),
    ("NY", "New York"), ("NC", "North Carolina"), ("ND", "North Dakota"), ("OH", "Ohio"),
    ("OK", "Oklahoma"), ("OR", "Oregon"), ("PA", "Pennsylvania"), ("RI", "Rhode Island"),
    ("SC", "South Carolina"), ("SD", "South Dakota"), ("TN", "Tennessee"), ("TX", "Texas"),
    ("UT", "Utah"), ("VT", "Vermont"), ("VA", "Virginia"), ("WA", "Washington"),
    ("WV", "West Virginia"), ("WI", "Wisconsin"), ("WY", "Wyoming"),
]

PROPERTY_TYPES = [
    ("single_family", "Single family home"),
    ("duplex", "Duplex"),
    ("condo", "Condo"),
    ("townhouse", "Townhouse"),
    ("multi_family", "Multi-family"),
    ("apartment", "Apartment"),
    ("other", "Other"),
]

AI_TOOLS = [
    ("claude-code", "Claude Code", "Anthropic's AI assistant for code and property management"),
    ("chatgpt", "ChatGPT / GPT-4", "OpenAI's conversational AI"),
    ("cursor", "Cursor", "AI-powered code editor"),
    ("other", "Other / Not sure", "Any AI assistant that can read markdown files"),
]


def get_us_states() -> list[tuple[str, str]]:
    """Return list of (code, name) tuples for all US states + DC."""
    return US_STATES


def get_property_types() -> list[tuple[str, str]]:
    """Return list of (value, label) tuples for property types."""
    return PROPERTY_TYPES


def get_ai_tools() -> list[tuple[str, str, str]]:
    """Return list of (value, name, description) tuples for AI tools."""
    return AI_TOOLS


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    text = text.strip('-')
    return text


def generate_slug(address: str, existing_slugs: list[str] | None = None) -> str:
    """Generate a unique slug from address."""
    if existing_slugs is None:
        existing_slugs = [p.get("slug", "") for p in config_svc.get_properties()]

    # Extract street portion (before city/state)
    parts = address.split(",")
    street = parts[0].strip() if parts else address

    # Remove house number for shorter slug, keep street name
    words = street.split()
    if len(words) > 1 and words[0].isdigit():
        slug_base = slugify(" ".join(words[1:]))
    else:
        slug_base = slugify(street)

    if not slug_base:
        slug_base = "property"

    slug = slug_base
    counter = 2
    while slug in existing_slugs:
        slug = f"{slug_base}-{counter}"
        counter += 1

    return slug


def create_property_from_template(slug: str, data: dict) -> Path:
    """
    Copy property-template/ to properties/{slug}/, replace placeholders in README.md.
    Returns the path to the new property directory.
    """
    repo_root = settings.repo_root
    template_dir = repo_root / "properties" / "property-template"
    dest_dir = repo_root / "properties" / slug

    if dest_dir.exists():
        return dest_dir

    if template_dir.exists():
        shutil.copytree(str(template_dir), str(dest_dir))
    else:
        dest_dir.mkdir(parents=True, exist_ok=True)
        # Create minimal README if no template
        readme = dest_dir / "README.md"
        readme.write_text(_generate_readme(data), encoding="utf-8")
        return dest_dir

    # Replace placeholders in README.md
    readme = dest_dir / "README.md"
    if readme.exists():
        content = readme.read_text(encoding="utf-8")
        content = _replace_placeholders(content, data)
        readme.write_text(content, encoding="utf-8")

    return dest_dir


def _replace_placeholders(content: str, data: dict) -> str:
    """Replace [PLACEHOLDER] values in property README."""
    address = data.get("address", "")
    slug = data.get("slug", "")

    replacements = {
        "[PROPERTY_ADDRESS]": address,
        "[PROPERTY_SLUG]": slug,
        "[STREET_ADDRESS]": address.split(",")[0].strip() if "," in address else address,
        "[ACTIVE / VACANT / TRANSITIONING / OTHER]": data.get("status", "Active").capitalize(),
    }

    # Parse city/state/zip from address
    parts = [p.strip() for p in address.split(",")]
    if len(parts) >= 2:
        city_state_zip = parts[1] if len(parts) == 2 else ", ".join(parts[1:])
        replacements["[CITY], [STATE] [ZIP]"] = city_state_zip

    if data.get("year_built"):
        replacements["[YEAR_BUILT]"] = str(data["year_built"])
    if data.get("type"):
        type_label = dict(PROPERTY_TYPES).get(data["type"], data["type"])
        replacements["[Single family home / Duplex / Condo / Townhouse / Multi-family]"] = type_label
    if data.get("bedrooms"):
        replacements["[NUMBER_OF_BEDROOMS]"] = str(data["bedrooms"])
    if data.get("bathrooms"):
        replacements["[NUMBER_AND_TYPE, e.g., \"2 full, 1 half\"]"] = str(data["bathrooms"])
    if data.get("rent_amount"):
        replacements["[RENT_AMOUNT]"] = str(data["rent_amount"])
    if data.get("tenant_name"):
        replacements["[TENANT_NAME]"] = data["tenant_name"]

    # Get owner name from config
    owner = config_svc.get_owner()
    if owner.get("name"):
        replacements["[OWNER_NAMES]"] = owner["name"]
        replacements["[OWNER_NAME]"] = owner["name"]

    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)

    return content


def _generate_readme(data: dict) -> str:
    """Generate a minimal property README when no template exists."""
    address = data.get("address", "Unknown")
    slug = data.get("slug", "")
    status = data.get("status", "Active")

    return f"""# Property - {address} ({slug})

**Status:** {status}
**Slug:** {slug}

---

## Property Details

| Field | Value |
|-------|-------|
| Address | {address} |
| Type | {dict(PROPERTY_TYPES).get(data.get('type', ''), '')} |
| Bedrooms | {data.get('bedrooms', '')} |
| Bathrooms | {data.get('bathrooms', '')} |
| Year built | {data.get('year_built', '')} |

## Current Lease

| Field | Value |
|-------|-------|
| Tenant | {data.get('tenant_name', '')} |
| Monthly rent | ${data.get('rent_amount', '')} |
| Lease type | {data.get('lease_type', '')} |
| Lease end | {data.get('lease_end', '')} |
"""


def update_property_readme(slug: str, data: dict) -> None:
    """Update existing property README Field|Value tables with new data."""
    repo_root = settings.repo_root
    readme = repo_root / "properties" / slug / "README.md"
    if not readme.exists():
        return

    content = readme.read_text(encoding="utf-8")

    # Update specific fields in Field|Value tables
    field_updates = {}
    if data.get("address"):
        field_updates["Address"] = data["address"]
    if data.get("type"):
        field_updates["Type"] = dict(PROPERTY_TYPES).get(data["type"], data["type"])
    if data.get("bedrooms"):
        field_updates["Bedrooms"] = str(data["bedrooms"])
    if data.get("bathrooms"):
        field_updates["Bathrooms"] = str(data["bathrooms"])
    if data.get("year_built"):
        field_updates["Year built"] = str(data["year_built"])
    if data.get("rent_amount"):
        field_updates["Monthly rent"] = f"${data['rent_amount']}"
    if data.get("tenant_name"):
        field_updates["Tenant"] = data["tenant_name"]
    if data.get("lease_type"):
        field_updates["Lease type"] = data["lease_type"]
    if data.get("lease_end"):
        field_updates["Lease end"] = data["lease_end"]

    if not field_updates:
        return

    lines = content.split("\n")
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("|") and "|" in stripped[1:]:
            cells = [c.strip() for c in stripped.split("|") if c.strip()]
            if len(cells) >= 2:
                field_name = cells[0]
                if field_name in field_updates:
                    # Reconstruct the row preserving pipe alignment
                    lines[i] = f"| {field_name} | {field_updates[field_name]} |"

    # Update title
    if data.get("address"):
        for i, line in enumerate(lines):
            if line.startswith("# Property -"):
                slug_str = data.get("slug", slug)
                lines[i] = f"# Property - {data['address']} ({slug_str})"
                break

    # Update status
    if data.get("status"):
        for i, line in enumerate(lines):
            if line.startswith("**Status:**"):
                lines[i] = f"**Status:** {data['status'].capitalize()}"
                break

    readme.write_text("\n".join(lines), encoding="utf-8")


def remove_property_files(slug: str) -> None:
    """Delete properties/{slug}/ directory."""
    prop_dir = settings.repo_root / "properties" / slug
    if prop_dir.exists() and prop_dir.is_dir():
        shutil.rmtree(str(prop_dir))


def update_agent_context(config: dict) -> None:
    """Rewrite AGENT_CONTEXT.md with current property list, owner, state."""
    context_file = settings.repo_root / ".pm_agent" / "AGENT_CONTEXT.md"
    if not context_file.exists():
        # Fallback to root location for repos that haven't moved it yet
        context_file = settings.repo_root / "AGENT_CONTEXT.md"
    if not context_file.exists():
        return

    content = context_file.read_text(encoding="utf-8")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Replace date placeholders
    content = content.replace("YYYY-MM-DD", today)

    # Replace owner placeholder
    owner_name = config.get("owner", {}).get("name", "")
    if owner_name:
        content = content.replace("[OWNER_NAME]", owner_name)

    # Replace state placeholder
    state = config.get("jurisdiction", {}).get("state", "")
    if state:
        content = content.replace("[YOUR_STATE]", state)

    # Replace AI tool placeholder
    ai_tool = config.get("ai_tool", "")
    tool_label = dict((t[0], t[1]) for t in AI_TOOLS).get(ai_tool, ai_tool)
    if tool_label:
        content = content.replace("[AI_TOOL]", tool_label)

    # Replace last updated placeholder
    content = content.replace("[LAST_UPDATED]", today)

    context_file.write_text(content, encoding="utf-8")


def update_continuity_files(config: dict) -> None:
    """Replace [OWNER_NAME] in continuity/*.md files."""
    owner_name = config.get("owner", {}).get("name", "")
    if not owner_name:
        return

    continuity_dir = settings.repo_root / "continuity"
    if not continuity_dir.exists():
        return

    for md_file in continuity_dir.glob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            if "[OWNER_NAME]" in content:
                content = content.replace("[OWNER_NAME]", owner_name)
                md_file.write_text(content, encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue


def run_complete_setup(config: dict) -> None:
    """Run all file-creation steps when onboarding completes."""
    # Create property directories from templates
    for prop in config.get("properties", []):
        slug = prop.get("slug", "")
        if slug:
            create_property_from_template(slug, prop)

    # Update AGENT_CONTEXT.md
    update_agent_context(config)

    # Update continuity files
    update_continuity_files(config)
