"""File system operations: tree building, reading, writing, path validation."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
import os

from app.config import settings


@dataclass
class TreeNode:
    """A node in the file tree (either a directory or a file)."""
    name: str
    rel_path: str
    is_dir: bool
    children: list[TreeNode] = field(default_factory=list)


def validate_path(rel_path: str) -> Path:
    """
    Validate and resolve a relative path against the repo root.
    Raises ValueError if the path is outside the repo root or not an .md file.
    Returns the resolved absolute path.
    """
    # Resolve the full path
    full_path = (settings.repo_root / rel_path).resolve()

    # Check it's under the repo root
    try:
        full_path.relative_to(settings.repo_root.resolve())
    except ValueError:
        raise ValueError(f"Path traversal detected: {rel_path}")

    # Check it's not in an excluded directory
    parts = Path(rel_path).parts
    if parts and parts[0] in settings.excluded_dirs:
        raise ValueError(f"Access to excluded directory: {parts[0]}")

    # Also check if any part starts with "." (hidden dirs)
    for part in parts[:-1]:  # Check directory parts, not the filename
        if part.startswith("."):
            raise ValueError(f"Access to hidden directory: {part}")

    return full_path


def validate_writable_path(rel_path: str) -> Path:
    """Validate a path for writing. Must be .md and under repo root."""
    full_path = validate_path(rel_path)

    if full_path.suffix.lower() != ".md":
        raise ValueError(f"Can only write to .md files, got: {full_path.suffix}")

    return full_path


def build_tree(root: Optional[Path] = None) -> list[TreeNode]:
    """
    Build a file tree from the repo root.
    Returns a list of top-level TreeNodes (files first, then directories).
    Excludes hidden dirs, webapp/, and non-.md files.
    Empty directories (no .md at any depth) are excluded.
    """
    if root is None:
        root = settings.repo_root.resolve()

    top_level_files = []
    top_level_dirs = []

    try:
        entries = sorted(os.scandir(root), key=lambda e: e.name.lower())
    except PermissionError:
        return []

    for entry in entries:
        # Skip excluded directories and hidden entries
        if entry.name.startswith(".") or entry.name in settings.excluded_dirs or entry.name == "__pycache__":
            continue

        if entry.is_dir(follow_symlinks=False):
            children = _build_subtree(Path(entry.path), root)
            if children is not None:  # None means empty dir
                rel_path = str(Path(entry.path).relative_to(root))
                node = TreeNode(
                    name=entry.name,
                    rel_path=rel_path,
                    is_dir=True,
                    children=children,
                )
                top_level_dirs.append(node)
        elif entry.is_file() and entry.name.endswith(".md"):
            rel_path = str(Path(entry.path).relative_to(root))
            top_level_files.append(TreeNode(
                name=entry.name,
                rel_path=rel_path,
                is_dir=False,
            ))

    # Top-level: files first (alphabetical), then directories (alphabetical)
    return top_level_files + top_level_dirs


def _build_subtree(dir_path: Path, repo_root: Path) -> Optional[list[TreeNode]]:
    """
    Recursively build a subtree. Returns None if the directory
    contains no .md files at any depth (should be excluded).
    """
    files = []
    dirs = []

    try:
        entries = sorted(os.scandir(dir_path), key=lambda e: e.name.lower())
    except PermissionError:
        return None

    for entry in entries:
        if entry.name.startswith(".") or entry.name in settings.excluded_dirs or entry.name == "__pycache__":
            continue

        if entry.is_dir(follow_symlinks=False):
            children = _build_subtree(Path(entry.path), repo_root)
            if children is not None:
                rel_path = str(Path(entry.path).relative_to(repo_root))
                dirs.append(TreeNode(
                    name=entry.name,
                    rel_path=rel_path,
                    is_dir=True,
                    children=children,
                ))
        elif entry.is_file() and entry.name.endswith(".md"):
            rel_path = str(Path(entry.path).relative_to(repo_root))
            files.append(TreeNode(
                name=entry.name,
                rel_path=rel_path,
                is_dir=False,
            ))

    if not files and not dirs:
        return None  # Empty directory

    # Directories first (alphabetical), then files (alphabetical)
    return dirs + files


def read_file(rel_path: str) -> str:
    """Read a markdown file and return its content."""
    full_path = validate_path(rel_path)

    if not full_path.exists():
        raise FileNotFoundError(f"File not found: {rel_path}")

    try:
        return full_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return full_path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            return full_path.read_text(encoding="latin-1")


def write_file(rel_path: str, content: str) -> None:
    """Write content to a markdown file."""
    full_path = validate_writable_path(rel_path)

    if not full_path.exists():
        raise FileNotFoundError(f"File not found: {rel_path}")

    full_path.write_text(content, encoding="utf-8")


def get_recent_files(limit: int = 15) -> list[dict]:
    """Get the most recently modified .md files."""
    files = []
    repo_root = settings.repo_root.resolve()

    for md_file in repo_root.rglob("*.md"):
        try:
            rel = md_file.relative_to(repo_root)
        except ValueError:
            continue

        # Skip excluded dirs
        parts = rel.parts
        if parts and (parts[0] in settings.excluded_dirs or parts[0].startswith(".")):
            continue

        stat = md_file.stat()
        files.append({
            "name": md_file.name,
            "rel_path": str(rel),
            "mtime": stat.st_mtime,
            "size": stat.st_size,
        })

    files.sort(key=lambda f: f["mtime"], reverse=True)
    return files[:limit]
