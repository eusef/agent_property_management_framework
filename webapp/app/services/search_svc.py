"""Search service: file name and content search across all .md files."""
import re
from pathlib import Path

from app.config import settings


def search(query: str) -> dict:
    """
    Search file names and content across all .md files.
    Returns {query, file_matches: [...], content_matches: [...]}
    """
    if not query or not query.strip():
        return {"query": query, "file_matches": [], "content_matches": []}

    query = query.strip()
    query_lower = query.lower()
    escaped = re.escape(query)
    pattern = re.compile(escaped, re.IGNORECASE)

    repo_root = settings.repo_root.resolve()
    file_matches = []
    content_matches = []

    for md_file in sorted(repo_root.rglob("*.md")):
        try:
            rel = md_file.relative_to(repo_root)
        except ValueError:
            continue

        parts = rel.parts
        if parts and (parts[0] in settings.excluded_dirs or parts[0].startswith(".")):
            continue

        rel_str = str(rel)

        # File name match
        if query_lower in md_file.name.lower():
            file_matches.append({"name": md_file.name, "rel_path": rel_str})

        # Content match
        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        lines = content.split('\n')
        matches = []
        for i, line in enumerate(lines):
            if pattern.search(line):
                matches.append({
                    "line_num": i + 1,
                    "line": line,
                    "context_before": lines[i - 1] if i > 0 else "",
                    "context_after": lines[i + 1] if i < len(lines) - 1 else "",
                })

        if matches:
            content_matches.append({
                "rel_path": rel_str,
                "name": md_file.name,
                "matches": matches,
            })

    return {
        "query": query,
        "file_matches": file_matches,
        "content_matches": content_matches,
    }
