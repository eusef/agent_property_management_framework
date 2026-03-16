"""Server management routes."""
import os
import signal
import asyncio
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).resolve().parent.parent / "templates")


@router.post("/api/shutdown", response_class=HTMLResponse)
async def shutdown(request: Request):
    """Shut down the server. Returns goodbye page, then terminates."""
    response = templates.TemplateResponse("server_stopped.html", {"request": request})

    # Schedule shutdown after response is sent
    loop = asyncio.get_event_loop()
    loop.call_later(0.5, lambda: os.kill(os.getpid(), signal.SIGTERM))

    return response
