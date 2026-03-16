"""
Shared test fixtures for the Property Management Web App test suite.

Provides:
- tmp_repo: A temporary directory mimicking the repo structure with sample .md files
- app_client: A FastAPI TestClient configured to use the tmp_repo
- sample_markdown: Various markdown content strings for testing
- sample_checkbox_file: A temp file with checkboxes for toggle testing
"""

import os
import textwrap
from datetime import datetime
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# Marker registration
# ---------------------------------------------------------------------------

def pytest_configure(config):
    config.addinivalue_line("markers", "unit: Unit tests for individual modules")
    config.addinivalue_line("markers", "integration: Integration tests for API routes")
    config.addinivalue_line("markers", "acceptance: Acceptance tests mapped to PRD AC codes")
    config.addinivalue_line("markers", "slow: Tests that may take more than 1 second")


# ---------------------------------------------------------------------------
# Temporary repo fixture
# ---------------------------------------------------------------------------

@pytest.fixture
def tmp_repo(tmp_path):
    """
    Creates a temporary directory mimicking the repo structure with sample .md files.

    Structure:
        CLAUDE.md
        TASKS.md
        DASHBOARD.md
        DECISIONS.md
        IMPROVEMENTS.md
        compliance/
            fair-housing.md
            or-landlord-tenant.md
        continuity/
            succession-plan.md
        docs/
            planning/
                roadmap.md
            meeting-notes.md
        properties/
            property-1 example-property/
                README.md
                maintenance/
                    work-log.md
                DOCS/
                    (empty - only .gitkeep)
            property-2 second-property/
                README.md
                inspections/
                    purchase-inspection.md
                projects/
                    fence-retaining-wall-2026.md
        vendors/
            README.md
        financials/
            tax/
                2026/
                    README.md
            HISTORICAL/
                summary.csv  (non-md, should be excluded from tree)
        scripts/
            README.md
        templates/
            checklists/
                (empty directory - no .md files)
        webapp/
            docs/
                PRD.md  (should be excluded from tree)
        .git/
            config  (hidden dir, should be excluded)
        .agents/
            notes.md  (hidden dir, should be excluded)
        empty_dir/
            (empty directory - should be excluded from tree)
    """
    repo = tmp_path / "repo"
    repo.mkdir()

    # Top-level markdown files
    (repo / "CLAUDE.md").write_text("# Claude Working Memory\n\nPersistent context.\n")
    (repo / "TASKS.md").write_text(textwrap.dedent("""\
        # Tasks

        ## In Progress
        - [ ] **Send termination notice** - 60-day notice to Example PM Co
        - [ ] Request lease copy from Example PM Co
          - [x] Called Example PM Co office
          - [ ] Follow up on email

        ## Completed
        - [x] Set up repo structure
        - [x] Process purchase inspection
    """))
    (repo / "DASHBOARD.md").write_text(textwrap.dedent("""\
        # Dashboard

        | Property | Status | Next Action |
        |----------|--------|-------------|
        | Property 1 | Active | Water heater replacement |
        | Property 2 | Personal | Fence project summer 2026 |
    """))
    (repo / "DECISIONS.md").write_text("# Decisions\n\n- 2026-03-01: Use markdown + CSV, no database\n")
    (repo / "IMPROVEMENTS.md").write_text("# Improvements Backlog\n\n- [ ] IMP-001: Add vendor rating system\n")

    # compliance/
    compliance = repo / "compliance"
    compliance.mkdir()
    (compliance / "fair-housing.md").write_text("# Fair Housing Summary\n\nFederal and state requirements.\n")
    (compliance / "or-landlord-tenant.md").write_text("# Oregon Landlord-Tenant Act\n\nSummary of key statutes.\n")

    # continuity/
    continuity = repo / "continuity"
    continuity.mkdir()
    (continuity / "succession-plan.md").write_text("# Succession Plan\n\nDesignated successor: Jane Smith\n")

    # docs/
    docs = repo / "docs"
    docs.mkdir()
    (docs / "meeting-notes.md").write_text("# Meeting Notes\n\n## 2026-03-01\nDiscussed fence project.\n")
    planning = docs / "planning"
    planning.mkdir()
    (planning / "roadmap.md").write_text("# Roadmap\n\n## Phase 1\n- [x] Scaffolding complete\n")

    # properties/property-1 example-property/
    prop1 = repo / "properties" / "property-1 example-property"
    prop1.mkdir(parents=True)
    (prop1 / "README.md").write_text(textwrap.dedent("""\
        # Property 1: 123 Main St

        ## Property Details

        | Field | Value |
        |-------|-------|
        | Address | 123 Main St |
        | City/State/ZIP | Anytown, ST 00000 |
        | Year built | 2008 |
        | Type | Single family home |
        | Rent | ~$3,500/mo |

        ## Open Items
        - [ ] Replace water heater (ASAP)
        - [ ] Get earthquake insurance quotes
        - [x] Document appliance inventory
    """))
    maint1 = prop1 / "maintenance"
    maint1.mkdir()
    (maint1 / "work-log.md").write_text("# Work Log\n\n- 2024-09: Oven replacement\n- 2023-11: Fridge replacement\n")
    docs1 = prop1 / "DOCS"
    docs1.mkdir()
    (docs1 / ".gitkeep").write_text("")  # No .md files here

    # properties/property-2 second-property/
    prop2 = repo / "properties" / "property-2 second-property"
    prop2.mkdir(parents=True)
    (prop2 / "README.md").write_text(textwrap.dedent("""\
        # Property 2: 456 Oak Ave

        ## Property Details

        | Field | Value |
        |-------|-------|
        | Address | 456 Oak Ave |
        | City/State/ZIP | Anytown, ST 00001 |
        | Year built | 2014 |
        | Type | Personal residence |

        ## Open Items
        - [ ] Fence + retaining wall project
        - [ ] Monitor water heater (13yr old)
        - [x] Roof inspection completed
    """))
    insp2 = prop2 / "inspections"
    insp2.mkdir()
    (insp2 / "purchase-inspection.md").write_text("# Purchase Inspection\n\nDate: 2021-01-12\nInspector: Jay Hensleigh\n")
    proj2 = prop2 / "projects"
    proj2.mkdir()
    (proj2 / "fence-retaining-wall-2026.md").write_text(textwrap.dedent("""\
        # Fence & Retaining Wall Project

        ## Tasks
        - [ ] Get structural engineer assessment
        - [ ] Get fence quotes (3 vendors)
          - [x] Example Fencing
          - [ ] Cascade Fence & Deck
          - [ ] Certified Fencing
        - [ ] Schedule work for summer 2026
    """))

    # vendors/
    vendors = repo / "vendors"
    vendors.mkdir()
    (vendors / "README.md").write_text("# Vendor Database\n\n| Vendor | Trade | Phone |\n|--------|-------|-------|\n| Example Fencing | Fencing | 503-555-0001 |\n")

    # financials/
    fin = repo / "financials"
    fin.mkdir()
    tax = fin / "tax" / "2026"
    tax.mkdir(parents=True)
    (tax / "README.md").write_text("# 2026 Tax Records\n\nPending.\n")
    hist = fin / "HISTORICAL"
    hist.mkdir()
    (hist / "summary.csv").write_text("date,amount,description\n2024-01-15,500,Plumbing repair\n")

    # scripts/
    scripts = repo / "scripts"
    scripts.mkdir()
    (scripts / "README.md").write_text("# Scripts\n\nAutomation scripts for property management.\n")

    # templates/ (with empty subdirectory)
    templates = repo / "templates"
    templates.mkdir()
    checklists = templates / "checklists"
    checklists.mkdir()
    # No .md files - this dir should be excluded from tree

    # webapp/ (should be excluded from tree)
    webapp = repo / "webapp"
    webapp.mkdir()
    webapp_docs = webapp / "docs"
    webapp_docs.mkdir()
    (webapp_docs / "PRD.md").write_text("# PRD\n\nThis should not appear in the file tree.\n")

    # .git/ (hidden, should be excluded)
    git_dir = repo / ".git"
    git_dir.mkdir()
    (git_dir / "config").write_text("[core]\n\tbare = false\n")

    # .agents/ (hidden, should be excluded)
    agents_dir = repo / ".agents"
    agents_dir.mkdir()
    (agents_dir / "notes.md").write_text("# Agent Notes\n\nShould be excluded.\n")

    # empty_dir/ (no .md files, should be excluded)
    (repo / "empty_dir").mkdir()

    return repo


@pytest.fixture
def app_client(tmp_repo):
    """
    FastAPI TestClient configured to use the tmp_repo as the repo root.

    This fixture patches the app's settings to point to the temporary repo
    and returns an httpx-based TestClient for making requests.

    Usage:
        def test_something(app_client):
            response = app_client.get("/")
            assert response.status_code == 200
    """
    # This will be implemented once the app code exists.
    # For now, return None so stubs can reference it.
    pytest.skip("App not yet implemented - TestClient fixture pending")


@pytest.fixture
def sample_markdown():
    """
    Dictionary of sample markdown content strings for testing various rendering scenarios.

    Keys:
        - headers: Markdown with h1-h6 headers
        - tables: Markdown with pipe-delimited tables
        - formatting: Markdown with bold, italic, inline code
        - lists: Markdown with bullet and numbered lists
        - code_blocks: Markdown with fenced code blocks
        - links: Markdown with various link formats
        - hr: Markdown with horizontal rules
        - checkboxes: Markdown with checked and unchecked checkboxes
        - nested_checkboxes: Markdown with indented/nested checkboxes
        - checkboxes_in_code: Markdown with checkbox syntax inside code blocks
        - mixed: Markdown combining multiple elements
        - empty: Empty string
        - whitespace_only: Only whitespace characters
        - bold_checkboxes: Checkboxes with bold text
        - property_table: Field/Value table like property READMEs
    """
    return {
        "headers": textwrap.dedent("""\
            # Heading 1
            ## Heading 2
            ### Heading 3
            #### Heading 4
            ##### Heading 5
            ###### Heading 6
        """),
        "tables": textwrap.dedent("""\
            | Column A | Column B | Column C |
            |----------|----------|----------|
            | Value 1  | Value 2  | Value 3  |
            | Value 4  | Value 5  | Value 6  |
        """),
        "formatting": textwrap.dedent("""\
            This has **bold text** and *italic text* and `inline code`.
            Also __bold__ and _italic_ variants.
        """),
        "lists": textwrap.dedent("""\
            - Bullet item 1
            - Bullet item 2
              - Nested bullet
            * Star bullet

            1. Numbered item 1
            2. Numbered item 2
        """),
        "code_blocks": textwrap.dedent("""\
            Some text before.

            ```python
            def hello():
                print("world")
            ```

            ```
            - [ ] This is inside a code block, NOT a checkbox
            - [x] This too
            ```

            Some text after.
        """),
        "links": textwrap.dedent("""\
            Visit [Google](https://google.com) or [Local file](TASKS.md).
            Also bare URL: https://example.com
        """),
        "hr": textwrap.dedent("""\
            Above the rule.

            ---

            Below the rule.
        """),
        "checkboxes": textwrap.dedent("""\
            # Tasks

            ## In Progress
            - [ ] First unchecked task
            - [ ] Second unchecked task
            - [x] Completed task
            - [X] Also completed (uppercase X)

            ## Done
            - [x] All done here
        """),
        "nested_checkboxes": textwrap.dedent("""\
            - [ ] Parent task
              - [x] Completed subtask
              - [ ] Pending subtask
                - [ ] Deeply nested task
            - [x] Another parent (done)
              - [x] Its subtask (done)
        """),
        "checkboxes_in_code": textwrap.dedent("""\
            Real checkbox:
            - [ ] This is a real checkbox

            Code block with checkbox syntax:
            ```
            - [ ] This should NOT be interactive
            - [x] Neither should this
            ```

            Inline code: `- [ ] not a checkbox`

            Another real checkbox:
            - [x] This is real too
        """),
        "mixed": textwrap.dedent("""\
            # Project Status

            ## Overview
            This project has **bold goals** and *italic emphasis*.

            | Phase | Status |
            |-------|--------|
            | 1     | Done   |
            | 2     | Active |

            ## Tasks
            - [ ] Implement feature A
            - [x] Design feature B

            ---

            See [details](docs/details.md) for more.
        """),
        "empty": "",
        "whitespace_only": "   \n\n\t\n  \n",
        "bold_checkboxes": textwrap.dedent("""\
            - [ ] **Send termination notice** - 60-day notice to Example PM Co
            - [ ] **Get earthquake quotes** - USAA + standalone providers
            - [x] **Document appliance inventory** - All Frigidaire stainless
        """),
        "property_table": textwrap.dedent("""\
            # Property Details

            | Field | Value |
            |-------|-------|
            | Address | 123 Main St |
            | City/State/ZIP | Anytown, ST 00000 |
            | Year built | 2008 |
            | Type | Single family home |
            | Rent | ~$3,500/mo |
        """),
    }


@pytest.fixture
def sample_checkbox_file(tmp_path):
    """
    Creates a temporary markdown file with various checkbox patterns for toggle testing.

    Returns a tuple of (file_path, original_content) so tests can verify
    modifications against the original.
    """
    content = textwrap.dedent("""\
        # Test Checkbox File

        ## Section A
        - [ ] Unchecked task A1
        - [x] Checked task A2
        - [ ] **Bold task A3** - with description

        ## Section B
        - [ ] Parent task B1
          - [x] Completed subtask B1a
          - [ ] Pending subtask B1b
            - [ ] Deeply nested B1b-i

        ## Section C (code block)
        ```
        - [ ] This is NOT a real checkbox
        - [x] Neither is this
        ```

        ## Section D
        - [ ] Duplicate text
        - [ ] Duplicate text
        - [x] Unique checked task D3

        Inline code: `- [ ] also not a checkbox`

        - [ ] Final task
    """)
    file_path = tmp_path / "checkboxes.md"
    file_path.write_text(content)
    return file_path, content
