"""File viewing, editing, and saving routes."""
from datetime import datetime
from fastapi import APIRouter, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.services import filesystem, markdown_svc

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).resolve().parent.parent / "templates")


def _get_base_context(request: Request, current_path: str = "") -> dict:
    """Build the base template context with file tree."""
    tree = filesystem.build_tree()
    return {
        "request": request,
        "tree": tree,
        "current_path": current_path,
    }


def _now():
    return datetime.now().strftime("%H:%M:%S")


@router.get("/file/{path:path}", response_class=HTMLResponse)
async def view_file(request: Request, path: str):
    """View a rendered markdown file."""
    try:
        content = filesystem.read_file(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"File not found: {path}")
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))

    rendered = markdown_svc.render_with_checkboxes(content, path)

    ctx = _get_base_context(request, current_path=path)
    ctx["file_path"] = path
    ctx["file_name"] = Path(path).name
    ctx["rendered_content"] = rendered

    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("fragments/file_view_content.html", ctx)
    return templates.TemplateResponse("file_view.html", ctx)


@router.get("/edit/{path:path}", response_class=HTMLResponse)
async def edit_file(request: Request, path: str):
    """Edit a markdown file — side-by-side textarea and preview."""
    try:
        content = filesystem.read_file(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"File not found: {path}")
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))

    # Preview uses render_markdown (non-interactive checkboxes) per S2-10
    preview = markdown_svc.render_markdown(content)

    ctx = _get_base_context(request, current_path=path)
    ctx["file_path"] = path
    ctx["file_name"] = Path(path).name
    ctx["raw_content"] = content
    ctx["preview_content"] = preview

    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("fragments/file_edit_content.html", ctx)
    return templates.TemplateResponse("file_edit.html", ctx)


@router.post("/api/preview", response_class=HTMLResponse)
async def preview_markdown(content: str = Form("")):
    """Render markdown preview (non-interactive checkboxes)."""
    rendered = markdown_svc.render_markdown(content)
    return HTMLResponse(content=rendered)


@router.put("/api/file/{path:path}", response_class=HTMLResponse)
async def save_file(request: Request, path: str, content: str = Form(...)):
    """Save file content to disk."""
    try:
        filesystem.write_file(path, content)
    except ValueError as e:
        return templates.TemplateResponse("components/toast.html", {
            "request": request, "message": str(e), "type": "error", "time": _now()
        })
    except FileNotFoundError as e:
        return templates.TemplateResponse("components/toast.html", {
            "request": request, "message": str(e), "type": "error", "time": _now()
        })
    except (PermissionError, OSError) as e:
        return templates.TemplateResponse("components/toast.html", {
            "request": request, "message": f"Cannot save: {e}", "type": "error", "time": _now()
        })

    return templates.TemplateResponse("components/toast.html", {
        "request": request, "message": "Saved successfully", "type": "success", "time": _now()
    })
