"""Config service: read/write config.json for onboarding and settings."""
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from app.config import settings

CONFIG_FILENAME = "config.json"
SCHEMA_VERSION = 1

DEFAULT_CONFIG = {
    "schema_version": SCHEMA_VERSION,
    "onboarding_complete": False,
    "onboarding_step": 0,
    "created_at": "",
    "updated_at": "",
    "owner": {"name": "", "email": "", "phone": ""},
    "jurisdiction": {"state": "", "state_code": ""},
    "ai_tool": "claude-code",
    "properties": [],
    "preferences": {"port": 8000, "auto_open_browser": True},
}


def _config_path() -> Path:
    return settings.repo_root / CONFIG_FILENAME


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def get_config() -> dict:
    """Read config.json. Returns default config if file doesn't exist."""
    path = _config_path()
    if not path.exists():
        return dict(DEFAULT_CONFIG)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return dict(DEFAULT_CONFIG)


def save_config(config: dict) -> None:
    """Atomic write: write to .tmp then rename."""
    config["updated_at"] = _now_iso()
    if not config.get("created_at"):
        config["created_at"] = config["updated_at"]
    path = _config_path()
    tmp_path = path.with_suffix(".json.tmp")
    tmp_path.write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(str(tmp_path), str(path))


def is_first_run() -> bool:
    """True if no config.json or onboarding not complete."""
    path = _config_path()
    if not path.exists():
        return True
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
        return not config.get("onboarding_complete", False)
    except (json.JSONDecodeError, OSError):
        return True


def get_onboarding_step() -> int:
    """Return the current onboarding step (0-based)."""
    config = get_config()
    return config.get("onboarding_step", 0)


def update_onboarding_step(step: int) -> dict:
    """Update the onboarding step and save."""
    config = get_config()
    config["onboarding_step"] = step
    save_config(config)
    return config


def complete_onboarding() -> dict:
    """Mark onboarding as complete."""
    config = get_config()
    config["onboarding_complete"] = True
    save_config(config)
    return config


# --- Owner CRUD ---

def get_owner() -> dict:
    return get_config().get("owner", {"name": "", "email": "", "phone": ""})


def update_owner(name: str = "", email: str = "", phone: str = "") -> dict:
    config = get_config()
    config["owner"] = {"name": name, "email": email, "phone": phone}
    save_config(config)
    return config


# --- Jurisdiction ---

def get_jurisdiction() -> dict:
    return get_config().get("jurisdiction", {"state": "", "state_code": ""})


def update_jurisdiction(state: str, state_code: str) -> dict:
    config = get_config()
    config["jurisdiction"] = {"state": state, "state_code": state_code}
    save_config(config)
    return config


# --- AI Tool ---

def update_ai_tool(tool: str) -> dict:
    config = get_config()
    config["ai_tool"] = tool
    save_config(config)
    return config


# --- Properties CRUD ---

def get_properties() -> list[dict]:
    return get_config().get("properties", [])


def get_property(slug: str) -> dict | None:
    for p in get_properties():
        if p.get("slug") == slug:
            return p
    return None


def add_property(prop: dict) -> dict:
    config = get_config()
    prop["created_at"] = _now_iso()
    config.setdefault("properties", []).append(prop)
    save_config(config)
    return config


def update_property(slug: str, data: dict) -> dict:
    config = get_config()
    for i, p in enumerate(config.get("properties", [])):
        if p.get("slug") == slug:
            data["created_at"] = p.get("created_at", _now_iso())
            config["properties"][i] = data
            break
    save_config(config)
    return config


def remove_property(slug: str) -> dict:
    config = get_config()
    config["properties"] = [p for p in config.get("properties", []) if p.get("slug") != slug]
    save_config(config)
    return config


# --- Migration from existing repos ---

def migrate_from_existing() -> dict | None:
    """
    Detect existing properties/ dirs with README.md files.
    Parse them and generate a config.json for repos that used the old setup.sh.
    Returns config if migration happened, None otherwise.
    """
    import re
    properties_dir = settings.repo_root / "properties"
    if not properties_dir.exists():
        return None

    existing_props = []
    for prop_dir in sorted(properties_dir.iterdir()):
        if not prop_dir.is_dir():
            continue
        if prop_dir.name == "property-template":
            continue
        readme = prop_dir / "README.md"
        if not readme.exists():
            continue

        try:
            content = readme.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        prop = _parse_readme_to_config(content, prop_dir.name)
        if prop:
            existing_props.append(prop)

    if not existing_props:
        return None

    # Try to detect owner from AGENT_CONTEXT.md or property READMEs
    owner_name = ""
    context_file = settings.repo_root / ".pm_agent" / "AGENT_CONTEXT.md"
    if not context_file.exists():
        context_file = settings.repo_root / "AGENT_CONTEXT.md"
    if context_file.exists():
        try:
            ctx = context_file.read_text(encoding="utf-8")
            # Look for owner name pattern
            for line in ctx.split("\n"):
                if "Owner" in line and "|" in line:
                    parts = [c.strip() for c in line.split("|") if c.strip()]
                    if len(parts) >= 2 and parts[0].lower().startswith("owner"):
                        val = parts[1]
                        if val and not val.startswith("["):
                            owner_name = val
                            break
        except OSError:
            pass

    config = dict(DEFAULT_CONFIG)
    config["properties"] = existing_props
    config["owner"]["name"] = owner_name
    config["onboarding_complete"] = True
    config["onboarding_step"] = 8
    save_config(config)
    return config


def _parse_readme_to_config(content: str, dir_name: str) -> dict | None:
    """Parse a property README.md into a config property dict."""
    import re

    # Parse Field/Value tables
    fields = {}
    lines = content.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if re.match(r"^\|\s*Field\s*\|\s*Value\s*\|", line, re.IGNORECASE):
            i += 1
            if i < len(lines) and re.match(r"^\|[-\s|]+\|", lines[i].strip()):
                i += 1
            while i < len(lines):
                row = lines[i].strip()
                if not row.startswith("|"):
                    break
                cells = [c.strip() for c in row.split("|") if c.strip()]
                if len(cells) >= 2:
                    fields[cells[0]] = cells[1]
                i += 1
        else:
            i += 1

    address = fields.get("Address", "")
    if not address or address.startswith("["):
        return None

    # Extract status
    status = "active"
    for line in lines:
        if line.startswith("**Status:**"):
            s = line.split("**Status:**")[1].strip().lower()
            if s and not s.startswith("["):
                status = s
            break

    return {
        "slug": dir_name,
        "address": address,
        "type": fields.get("Type", ""),
        "bedrooms": fields.get("Bedrooms", ""),
        "bathrooms": fields.get("Bathrooms", ""),
        "year_built": fields.get("Year built", ""),
        "rent_amount": fields.get("Monthly rent", "").replace("$", "").replace(",", ""),
        "tenant_name": fields.get("Tenant", ""),
        "lease_type": fields.get("Lease type", ""),
        "lease_end": fields.get("Lease end", ""),
        "status": status,
        "created_at": "",
    }
