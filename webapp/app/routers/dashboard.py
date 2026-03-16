"""Dashboard home page routes and widget endpoints."""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.services import filesystem, dashboard_svc

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).resolve().parent.parent / "templates")


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Dashboard home page. Widgets load lazily via HTMX."""
    tree = filesystem.build_tree()
    ctx = {
        "request": request,
        "tree": tree,
        "current_path": "",
    }
    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("fragments/dashboard_content.html", ctx)
    return templates.TemplateResponse("dashboard.html", ctx)


@router.get("/api/widget/open-tasks", response_class=HTMLResponse)
async def widget_open_tasks(request: Request):
    """Open Tasks widget - scans all .md files for unchecked checkboxes."""
    task_groups = dashboard_svc.get_open_tasks()
    total = sum(len(g["tasks"]) for g in task_groups)
    return templates.TemplateResponse("widgets/open_tasks.html", {
        "request": request,
        "task_groups": task_groups,
        "total": total,
    })


@router.get("/api/widget/recent-files", response_class=HTMLResponse)
async def widget_recent_files(request: Request):
    """Recently Modified Files widget."""
    files = dashboard_svc.get_recent_files(limit=15)
    return templates.TemplateResponse("widgets/recent_files.html", {
        "request": request,
        "files": files,
    })


@router.get("/api/widget/pinned-files", response_class=HTMLResponse)
async def widget_pinned_files(request: Request):
    """TASKS.md & DASHBOARD.md pinned widget."""
    tasks_data = dashboard_svc.get_pinned_file_content("TASKS.md")
    dashboard_data = dashboard_svc.get_pinned_file_content("DASHBOARD.md")
    return templates.TemplateResponse("widgets/pinned_files.html", {
        "request": request,
        "tasks_data": tasks_data,
        "dashboard_data": dashboard_data,
    })


@router.get("/api/widget/property-cards", response_class=HTMLResponse)
async def widget_property_cards(request: Request):
    """Property Quick-Reference Cards widget."""
    cards = dashboard_svc.get_property_cards()
    return templates.TemplateResponse("widgets/property_cards.html", {
        "request": request,
        "cards": cards,
    })
