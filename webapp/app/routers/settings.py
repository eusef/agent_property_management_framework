"""Settings routes for post-onboarding configuration."""
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.services import config_svc, onboarding_svc
from app.services.filesystem import build_tree
from app.config import settings as app_settings

router = APIRouter(prefix="/settings", tags=["settings"])
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")


def _ctx(request: Request, **kwargs) -> dict:
    """Build common template context with sidebar tree."""
    tree = build_tree(app_settings.repo_root)
    return {"request": request, "tree": tree, "current_path": "", **kwargs}


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
async def settings_page(request: Request):
    config = config_svc.get_config()
    ai_tools = onboarding_svc.get_ai_tools()
    ai_label = dict((t[0], t[1]) for t in ai_tools).get(config.get("ai_tool", ""), "")
    return templates.TemplateResponse(
        "settings.html",
        _ctx(request, config=config, ai_label=ai_label),
    )


# --- Owner ---

@router.get("/owner/edit", response_class=HTMLResponse)
async def edit_owner_form(request: Request):
    owner = config_svc.get_owner()
    is_htmx = request.headers.get("HX-Request") == "true"
    if is_htmx:
        return templates.TemplateResponse(
            "settings/edit_owner.html",
            {"request": request, "owner": owner, "errors": {}},
        )
    return RedirectResponse("/settings", status_code=302)


@router.post("/owner", response_class=HTMLResponse)
async def save_owner(
    request: Request,
    name: str = Form(""),
    email: str = Form(""),
    phone: str = Form(""),
):
    errors = {}
    if not name.strip():
        errors["name"] = "Name is required"

    if errors:
        return templates.TemplateResponse(
            "settings/edit_owner.html",
            {"request": request, "owner": {"name": name, "email": email, "phone": phone}, "errors": errors},
        )

    config = config_svc.update_owner(name.strip(), email.strip(), phone.strip())

    # Update files
    onboarding_svc.update_agent_context(config)
    onboarding_svc.update_continuity_files(config)

    is_htmx = request.headers.get("HX-Request") == "true"
    if is_htmx:
        owner = config_svc.get_owner()
        return templates.TemplateResponse(
            "fragments/settings_content.html",
            _settings_fragment_ctx(request),
        )
    return RedirectResponse("/settings", status_code=302)


# --- Jurisdiction ---

@router.get("/jurisdiction/edit", response_class=HTMLResponse)
async def edit_jurisdiction_form(request: Request):
    jurisdiction = config_svc.get_jurisdiction()
    states = onboarding_svc.get_us_states()
    is_htmx = request.headers.get("HX-Request") == "true"
    if is_htmx:
        return templates.TemplateResponse(
            "settings/edit_jurisdiction.html",
            {"request": request, "jurisdiction": jurisdiction, "states": states, "errors": {}},
        )
    return RedirectResponse("/settings", status_code=302)


@router.post("/jurisdiction", response_class=HTMLResponse)
async def save_jurisdiction(request: Request, state_code: str = Form("")):
    states = onboarding_svc.get_us_states()
    state_map = dict(states)
    state_name = state_map.get(state_code, "")

    if not state_code or state_code not in state_map:
        return templates.TemplateResponse(
            "settings/edit_jurisdiction.html",
            {"request": request, "jurisdiction": {"state": "", "state_code": state_code},
             "states": states, "errors": {"state": "Please select a state"}},
        )

    config = config_svc.update_jurisdiction(state_name, state_code)
    onboarding_svc.update_agent_context(config)

    is_htmx = request.headers.get("HX-Request") == "true"
    if is_htmx:
        return templates.TemplateResponse(
            "fragments/settings_content.html",
            _settings_fragment_ctx(request),
        )
    return RedirectResponse("/settings", status_code=302)


# --- Properties ---

@router.get("/property/add", response_class=HTMLResponse)
async def add_property_form(request: Request):
    return templates.TemplateResponse(
        "settings/add_property.html",
        _ctx(request, prop={}, errors={}),
    )


@router.post("/property/add", response_class=HTMLResponse)
async def create_property(
    request: Request,
    address: str = Form(""),
    property_type: str = Form(""),
    bedrooms: str = Form(""),
    bathrooms: str = Form(""),
    year_built: str = Form(""),
    rent_amount: str = Form(""),
    tenant_name: str = Form(""),
    lease_type: str = Form(""),
    lease_end: str = Form(""),
    status: str = Form("active"),
):
    errors = {}
    if not address.strip():
        errors["address"] = "Address is required"

    prop_data = {
        "address": address.strip(),
        "type": property_type,
        "bedrooms": bedrooms.strip(),
        "bathrooms": bathrooms.strip(),
        "year_built": year_built.strip(),
        "rent_amount": rent_amount.strip(),
        "tenant_name": tenant_name.strip(),
        "lease_type": lease_type,
        "lease_end": lease_end.strip(),
        "status": status,
    }

    if errors:
        return templates.TemplateResponse(
            "settings/add_property.html",
            _ctx(request, prop=prop_data, errors=errors),
        )

    slug = onboarding_svc.generate_slug(address)
    prop_data["slug"] = slug
    config_svc.add_property(prop_data)

    # Create property directory
    onboarding_svc.create_property_from_template(slug, prop_data)

    # Update AGENT_CONTEXT
    config = config_svc.get_config()
    onboarding_svc.update_agent_context(config)

    return RedirectResponse("/settings", status_code=302)


@router.get("/property/{slug}/edit", response_class=HTMLResponse)
async def edit_property_form(request: Request, slug: str):
    prop = config_svc.get_property(slug)
    if not prop:
        return RedirectResponse("/settings", status_code=302)
    return templates.TemplateResponse(
        "settings/edit_property.html",
        _ctx(request, prop=prop, edit_slug=slug, errors={}),
    )


@router.post("/property/{slug}", response_class=HTMLResponse)
async def save_property(
    request: Request,
    slug: str,
    address: str = Form(""),
    property_type: str = Form(""),
    bedrooms: str = Form(""),
    bathrooms: str = Form(""),
    year_built: str = Form(""),
    rent_amount: str = Form(""),
    tenant_name: str = Form(""),
    lease_type: str = Form(""),
    lease_end: str = Form(""),
    status: str = Form("active"),
):
    errors = {}
    if not address.strip():
        errors["address"] = "Address is required"

    prop_data = {
        "slug": slug,
        "address": address.strip(),
        "type": property_type,
        "bedrooms": bedrooms.strip(),
        "bathrooms": bathrooms.strip(),
        "year_built": year_built.strip(),
        "rent_amount": rent_amount.strip(),
        "tenant_name": tenant_name.strip(),
        "lease_type": lease_type,
        "lease_end": lease_end.strip(),
        "status": status,
    }

    if errors:
        return templates.TemplateResponse(
            "settings/edit_property.html",
            _ctx(request, prop=prop_data, edit_slug=slug, errors=errors),
        )

    config_svc.update_property(slug, prop_data)

    # Update property README
    onboarding_svc.update_property_readme(slug, prop_data)

    # Update AGENT_CONTEXT
    config = config_svc.get_config()
    onboarding_svc.update_agent_context(config)

    return RedirectResponse("/settings", status_code=302)


@router.post("/property/{slug}/delete", response_class=HTMLResponse)
async def delete_property(request: Request, slug: str):
    config_svc.remove_property(slug)
    onboarding_svc.remove_property_files(slug)

    config = config_svc.get_config()
    onboarding_svc.update_agent_context(config)

    return RedirectResponse("/settings", status_code=302)


# --- AI Tool ---

@router.get("/ai-tool/edit", response_class=HTMLResponse)
async def edit_ai_tool_form(request: Request):
    config = config_svc.get_config()
    ai_tools = onboarding_svc.get_ai_tools()
    is_htmx = request.headers.get("HX-Request") == "true"
    if is_htmx:
        return templates.TemplateResponse(
            "settings/edit_ai_tool.html",
            {"request": request, "ai_tools": ai_tools, "current_tool": config.get("ai_tool", "")},
        )
    return RedirectResponse("/settings", status_code=302)


@router.post("/ai-tool", response_class=HTMLResponse)
async def save_ai_tool(request: Request, ai_tool: str = Form("claude-code")):
    config = config_svc.update_ai_tool(ai_tool)
    onboarding_svc.update_agent_context(config)

    is_htmx = request.headers.get("HX-Request") == "true"
    if is_htmx:
        return templates.TemplateResponse(
            "fragments/settings_content.html",
            _settings_fragment_ctx(request),
        )
    return RedirectResponse("/settings", status_code=302)


# --- Re-onboard ---

@router.post("/re-onboard", response_class=HTMLResponse)
async def re_onboard(request: Request):
    config = config_svc.get_config()
    config["onboarding_complete"] = False
    config["onboarding_step"] = 0
    config_svc.save_config(config)
    return RedirectResponse("/onboarding", status_code=302)


# --- Helper ---

def _settings_fragment_ctx(request: Request) -> dict:
    config = config_svc.get_config()
    ai_tools = onboarding_svc.get_ai_tools()
    ai_label = dict((t[0], t[1]) for t in ai_tools).get(config.get("ai_tool", ""), "")
    return {"request": request, "config": config, "ai_label": ai_label}
