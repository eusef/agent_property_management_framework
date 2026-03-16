"""Onboarding wizard routes."""
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.services import config_svc, onboarding_svc

router = APIRouter(prefix="/onboarding", tags=["onboarding"])
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "templates")

TOTAL_STEPS = 8


def _ctx(request: Request, step: int, **kwargs) -> dict:
    """Build common template context."""
    return {"request": request, "step": step, "total_steps": TOTAL_STEPS, **kwargs}


# --- Step 1: Welcome ---

@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
async def welcome(request: Request):
    config = config_svc.get_config()
    step = config.get("onboarding_step", 0)
    can_resume = step > 1 and not config.get("onboarding_complete", False)
    return templates.TemplateResponse(
        "onboarding/welcome.html",
        _ctx(request, 1, can_resume=can_resume, resume_step=step),
    )


@router.post("/start", response_class=HTMLResponse)
async def start_onboarding(request: Request):
    """Start fresh onboarding (reset step to 1)."""
    config = config_svc.get_config()
    config["onboarding_step"] = 1
    config["onboarding_complete"] = False
    config_svc.save_config(config)
    return RedirectResponse("/onboarding/owner", status_code=302)


# --- Step 2: Owner Profile ---

@router.get("/owner", response_class=HTMLResponse)
async def owner_form(request: Request):
    owner = config_svc.get_owner()
    return templates.TemplateResponse(
        "onboarding/owner.html",
        _ctx(request, 2, owner=owner, errors={}),
    )


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
            "onboarding/owner.html",
            _ctx(request, 2, owner={"name": name, "email": email, "phone": phone}, errors=errors),
        )

    config_svc.update_owner(name.strip(), email.strip(), phone.strip())
    config_svc.update_onboarding_step(3)
    return RedirectResponse("/onboarding/jurisdiction", status_code=302)


# --- Step 3: Jurisdiction ---

@router.get("/jurisdiction", response_class=HTMLResponse)
async def jurisdiction_form(request: Request):
    jurisdiction = config_svc.get_jurisdiction()
    states = onboarding_svc.get_us_states()
    return templates.TemplateResponse(
        "onboarding/jurisdiction.html",
        _ctx(request, 3, jurisdiction=jurisdiction, states=states, errors={}),
    )


@router.post("/jurisdiction", response_class=HTMLResponse)
async def save_jurisdiction(
    request: Request,
    state_code: str = Form(""),
):
    states = onboarding_svc.get_us_states()
    state_map = dict(states)
    state_name = state_map.get(state_code, "")

    errors = {}
    if not state_code or state_code not in state_map:
        errors["state"] = "Please select your state"

    if errors:
        return templates.TemplateResponse(
            "onboarding/jurisdiction.html",
            _ctx(request, 3, jurisdiction={"state": "", "state_code": state_code}, states=states, errors=errors),
        )

    config_svc.update_jurisdiction(state_name, state_code)
    config_svc.update_onboarding_step(4)
    return RedirectResponse("/onboarding/property", status_code=302)


# --- Step 4: Add Property ---

@router.get("/property", response_class=HTMLResponse)
async def property_form(request: Request):
    return templates.TemplateResponse(
        "onboarding/property.html",
        _ctx(request, 4, prop={}, errors={}, is_edit=False),
    )


@router.post("/property", response_class=HTMLResponse)
async def save_property(
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
            "onboarding/property.html",
            _ctx(request, 4, prop=prop_data, errors=errors, is_edit=False),
        )

    slug = onboarding_svc.generate_slug(address)
    prop_data["slug"] = slug
    config_svc.add_property(prop_data)
    config_svc.update_onboarding_step(5)
    return RedirectResponse("/onboarding/properties", status_code=302)


# --- Step 5: Properties List ---

@router.get("/properties", response_class=HTMLResponse)
async def properties_list(request: Request):
    properties = config_svc.get_properties()
    return templates.TemplateResponse(
        "onboarding/properties_list.html",
        _ctx(request, 5, properties=properties),
    )


# --- Edit/Delete property during onboarding ---

@router.get("/property/{slug}/edit", response_class=HTMLResponse)
async def edit_property_form(request: Request, slug: str):
    prop = config_svc.get_property(slug)
    if not prop:
        return RedirectResponse("/onboarding/properties", status_code=302)
    return templates.TemplateResponse(
        "onboarding/property.html",
        _ctx(request, 5, prop=prop, errors={}, is_edit=True, edit_slug=slug),
    )


@router.post("/property/{slug}", response_class=HTMLResponse)
async def update_property(
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
            "onboarding/property.html",
            _ctx(request, 5, prop=prop_data, errors=errors, is_edit=True, edit_slug=slug),
        )

    config_svc.update_property(slug, prop_data)
    return RedirectResponse("/onboarding/properties", status_code=302)


@router.post("/property/{slug}/delete", response_class=HTMLResponse)
async def delete_property(request: Request, slug: str):
    config_svc.remove_property(slug)
    return RedirectResponse("/onboarding/properties", status_code=302)


# --- Step 6: AI Setup ---

@router.get("/ai-setup", response_class=HTMLResponse)
async def ai_setup(request: Request):
    config = config_svc.get_config()
    ai_tools = onboarding_svc.get_ai_tools()
    return templates.TemplateResponse(
        "onboarding/ai_setup.html",
        _ctx(request, 6, ai_tool=config.get("ai_tool", "claude-code"), ai_tools=ai_tools),
    )


@router.post("/ai-setup", response_class=HTMLResponse)
async def save_ai_setup(request: Request, ai_tool: str = Form("claude-code")):
    config_svc.update_ai_tool(ai_tool)
    config_svc.update_onboarding_step(7)
    return RedirectResponse("/onboarding/summary", status_code=302)


# --- Step 7: Summary ---

@router.get("/summary", response_class=HTMLResponse)
async def summary(request: Request):
    config = config_svc.get_config()
    ai_tools = onboarding_svc.get_ai_tools()
    ai_label = dict((t[0], t[1]) for t in ai_tools).get(config.get("ai_tool", ""), "")
    return templates.TemplateResponse(
        "onboarding/summary.html",
        _ctx(request, 7, config=config, ai_label=ai_label),
    )


# --- Step 8: Complete ---

@router.post("/complete", response_class=HTMLResponse)
async def complete(request: Request):
    config = config_svc.get_config()

    # Run all file-creation steps
    onboarding_svc.run_complete_setup(config)

    # Mark onboarding as complete
    config_svc.complete_onboarding()
    config_svc.update_onboarding_step(8)

    return RedirectResponse("/onboarding/success", status_code=302)


@router.get("/success", response_class=HTMLResponse)
async def success(request: Request):
    config = config_svc.get_config()
    return templates.TemplateResponse(
        "onboarding/success.html",
        _ctx(request, 8, config=config),
    )
