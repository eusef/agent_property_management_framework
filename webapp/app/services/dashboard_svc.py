"""Dashboard service: open tasks, recent files, pinned files, property cards."""
import re
from pathlib import Path
from datetime import datetime

from app.config import settings
from app.services import filesystem, markdown_svc


def get_open_tasks() -> list[dict]:
    """
    Scan all .md files for unchecked checkboxes (- [ ]).
    Returns list of dicts: {file_path, file_name, tasks: [{line_num, text, heading}]}
    Excludes files in webapp/ and hidden dirs.
    """
    repo_root = settings.repo_root.resolve()
    checkbox_pattern = re.compile(r'^(\s*)-\s+\[ \]\s+(.*)')
    heading_pattern = re.compile(r'^(#{1,6})\s+(.*)')
    fence_pattern = re.compile(r'^(`{3,}|~{3,})')

    task_groups = []

    for md_file in sorted(repo_root.rglob("*.md")):
        try:
            rel = md_file.relative_to(repo_root)
        except ValueError:
            continue

        parts = rel.parts
        if parts and (parts[0] in settings.excluded_dirs or parts[0].startswith(".")):
            continue

        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        lines = content.split('\n')
        # Find code block ranges
        code_lines = set()
        in_code = False
        for i, line in enumerate(lines):
            if fence_pattern.match(line.strip()):
                code_lines.add(i)
                in_code = not in_code
            elif in_code:
                code_lines.add(i)

        # Track current heading
        current_heading = ""
        tasks = []

        for i, line in enumerate(lines):
            if i in code_lines:
                continue

            heading_match = heading_pattern.match(line)
            if heading_match:
                current_heading = heading_match.group(2).strip()

            cb_match = checkbox_pattern.match(line)
            if cb_match:
                text = cb_match.group(2).strip()
                tasks.append({
                    "line_num": i,
                    "text": text,
                    "text_html": markdown_svc.render_inline(text),
                    "heading": current_heading,
                })

        if tasks:
            rel_str = str(rel)
            task_groups.append({
                "file_path": rel_str,
                "file_name": md_file.name,
                "tasks": tasks,
            })

    return task_groups


def get_recent_files(limit: int = 15) -> list[dict]:
    """Get recently modified .md files sorted by mtime. Delegates to filesystem."""
    files = filesystem.get_recent_files(limit=limit)
    # Format the timestamps for display
    for f in files:
        dt = datetime.fromtimestamp(f["mtime"])
        f["mtime_str"] = dt.strftime("%Y-%m-%d %H:%M")
        # Human-friendly file size
        size = f["size"]
        if size < 1024:
            f["size_str"] = f"{size} B"
        elif size < 1024 * 1024:
            f["size_str"] = f"{size / 1024:.1f} KB"
        else:
            f["size_str"] = f"{size / (1024 * 1024):.1f} MB"
    return files


def get_pinned_file_content(filename: str) -> dict:
    """
    Read and render a pinned file (TASKS.md or DASHBOARD.md).
    Returns {exists, content_html, file_path}.
    """
    repo_root = settings.repo_root.resolve()
    file_path = repo_root / filename

    if not file_path.exists():
        return {"exists": False, "content_html": "", "file_path": filename}

    try:
        content = file_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return {"exists": False, "content_html": "", "file_path": filename}

    # Render with interactive checkboxes
    html = markdown_svc.render_with_checkboxes(content, filename)

    return {"exists": True, "content_html": html, "file_path": filename}


def get_property_cards() -> list[dict]:
    """
    Scan properties/*/README.md files.
    Parse Field/Value tables to extract key data.
    Returns list of dicts with property details.
    """
    repo_root = settings.repo_root.resolve()
    properties_dir = repo_root / "properties"

    if not properties_dir.exists():
        return []

    cards = []

    for prop_dir in sorted(properties_dir.iterdir()):
        if not prop_dir.is_dir():
            continue
        readme = prop_dir / "README.md"
        if not readme.exists():
            continue

        try:
            content = readme.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        rel_path = str(readme.relative_to(repo_root))
        card = _parse_property_readme(content, prop_dir.name, rel_path)
        cards.append(card)

    return cards


def _parse_property_readme(content: str, dir_name: str, rel_path: str) -> dict:
    """Parse a property README.md and extract key fields from Field/Value tables."""
    card = {
        "dir_name": dir_name,
        "rel_path": rel_path,
        "title": "",
        "status": "",
        "fields": {},
        "alerts": [],
    }

    lines = content.split('\n')

    # Extract title from first heading
    for line in lines:
        if line.startswith("# "):
            card["title"] = line[2:].strip()
            break

    # Extract status from **Status:** line
    for line in lines:
        if line.startswith("**Status:**"):
            card["status"] = line.split("**Status:**")[1].strip()
            break

    # Parse all Field/Value tables
    fields = {}
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Look for "| Field | Value |" header (case-insensitive)
        if re.match(r'^\|\s*Field\s*\|\s*Value\s*\|', line, re.IGNORECASE):
            # Skip separator line
            i += 1
            if i < len(lines) and re.match(r'^\|[-\s|]+\|', lines[i].strip()):
                i += 1
            # Read data rows
            while i < len(lines):
                row = lines[i].strip()
                if not row.startswith("|"):
                    break
                cells = [c.strip() for c in row.split("|")]
                # Remove empty strings from split
                cells = [c for c in cells if c != ""]
                if len(cells) >= 2:
                    field_name = cells[0].strip()
                    field_value = cells[1].strip()
                    fields[field_name] = field_value
                i += 1
        else:
            i += 1

    card["fields"] = fields

    # Extract alerts section
    in_alerts = False
    for line in lines:
        if re.match(r'^##\s+Alerts', line, re.IGNORECASE):
            in_alerts = True
            continue
        if in_alerts:
            if line.startswith("## ") or line.startswith("---"):
                in_alerts = False
                continue
            stripped = line.strip()
            if stripped.startswith("- "):
                card["alerts"].append(stripped[2:].strip())

    # Build convenient display fields
    card["address"] = fields.get("Address", "Unknown address")
    card["type"] = fields.get("Type", fields.get("Style", ""))
    card["year_built"] = fields.get("Year built", "")
    card["rent"] = fields.get("Monthly rent", "")
    card["insurance_carrier"] = fields.get("Carrier", "")
    card["insurance_renewal"] = fields.get("Renewal date", fields.get("Policy period", ""))
    card["county"] = fields.get("County", "")

    return card
