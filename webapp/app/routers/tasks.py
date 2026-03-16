"""Checkbox toggle routes."""
import asyncio
import re
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.services import filesystem, markdown_svc

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).resolve().parent.parent / "templates")

# Per-file locks to prevent concurrent toggle race conditions (Risk R-01)
_file_locks: dict[str, asyncio.Lock] = {}


def _get_lock(file_path: str) -> asyncio.Lock:
    if file_path not in _file_locks:
        _file_locks[file_path] = asyncio.Lock()
    return _file_locks[file_path]


@router.post("/api/toggle-checkbox", response_class=HTMLResponse)
async def toggle_checkbox(
    request: Request,
    file_path: str = Form(...),
    line_num: int = Form(...),
    original_text: str = Form(...),
):
    """Toggle a checkbox in a markdown file."""
    lock = _get_lock(file_path)

    async with lock:
        try:
            content = filesystem.read_file(file_path)
            new_content = markdown_svc.toggle_checkbox(content, line_num, original_text)
            filesystem.write_file(file_path, new_content)
        except (ValueError, FileNotFoundError) as e:
            return HTMLResponse(
                content=f'<span class="text-error">Error: {e}</span>',
                status_code=400,
            )

    # Re-read file and build the replacement checkbox element
    new_file_content = filesystem.read_file(file_path)
    lines = new_file_content.split('\n')
    checkbox_pattern = re.compile(r'^(\s*)-\s+\[([ xX])\]\s+(.*)')

    if 0 <= line_num < len(lines):
        match = checkbox_pattern.match(lines[line_num])
        if match:
            indent, state, text = match.groups()
            checked = state.lower() == 'x'
            checked_attr = 'checked' if checked else ''
            safe_text = (text.strip()
                         .replace('\\', '\\\\')
                         .replace('"', '&quot;')
                         .replace("'", "&#39;"))
            rendered_text = markdown_svc.render_inline(text.strip())

            return HTMLResponse(content=(
                f'<li class="checkbox-item" id="cb-{line_num}">'
                f'<label class="checkbox-task">'
                f'<input type="checkbox" {checked_attr} '
                f'hx-post="/api/toggle-checkbox" '
                f'hx-vals=\'{{"file_path": "{file_path}", "line_num": {line_num}, "original_text": "{safe_text}"}}\' '
                f'hx-target="#cb-{line_num}" '
                f'hx-swap="outerHTML" />'
                f'<span>{rendered_text}</span>'
                f'</label></li>'
            ))

    # Fallback: return success message
    return HTMLResponse(content='<span>Toggled. Refresh to see changes.</span>')
