"""FastAPI application factory."""
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse

from app.config import settings
from app.services import config_svc
from app.routers import dashboard, files, tasks, search, server, onboarding, settings as settings_router

app = FastAPI(title="Property Management Web App")

# Static files
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

# Templates
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

# Include routers
app.include_router(onboarding.router)
app.include_router(settings_router.router)
app.include_router(dashboard.router)
app.include_router(files.router)
app.include_router(tasks.router)
app.include_router(search.router)
app.include_router(server.router)


# --- First-run redirect middleware ---

@app.middleware("http")
async def first_run_redirect(request: Request, call_next):
    path = request.url.path
    skip_prefixes = ("/static", "/onboarding", "/manifest.json", "/sw.js", "/offline")
    if any(path.startswith(p) for p in skip_prefixes):
        return await call_next(request)
    if config_svc.is_first_run():
        return RedirectResponse("/onboarding", status_code=302)
    return await call_next(request)


# --- PWA routes (served from root path for service worker scope) ---

@app.get("/manifest.json", response_class=FileResponse)
async def manifest():
    return FileResponse(Path(__file__).parent / "static" / "manifest.json", media_type="application/manifest+json")


@app.get("/sw.js", response_class=FileResponse)
async def service_worker():
    return FileResponse(
        Path(__file__).parent / "static" / "sw.js",
        media_type="application/javascript",
        headers={"Service-Worker-Allowed": "/"},
    )


@app.get("/offline", response_class=HTMLResponse)
async def offline():
    return FileResponse(Path(__file__).parent / "static" / "offline.html")


@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return templates.TemplateResponse(
        "404.html",
        {"request": request, "tree": [], "current_path": ""},
        status_code=404,
    )


@app.on_event("shutdown")
async def shutdown_event():
    print("\nServer stopped.")
