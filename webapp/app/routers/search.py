"""Search routes."""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.services import filesystem, search_svc

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).resolve().parent.parent / "templates")


@router.get("/search", response_class=HTMLResponse)
async def search_page(request: Request, q: str = ""):
    """Search files by name and content."""
    tree = filesystem.build_tree()

    if not q.strip():
        results = {"query": q, "file_matches": [], "content_matches": []}
        empty_query = True
    else:
        results = search_svc.search(q)
        empty_query = False

    ctx = {
        "request": request,
        "tree": tree,
        "current_path": "",
        "query": q,
        "results": results,
        "empty_query": empty_query,
    }
    if request.headers.get("HX-Request"):
        return templates.TemplateResponse("fragments/search_content.html", ctx)
    return templates.TemplateResponse("search_results.html", ctx)
