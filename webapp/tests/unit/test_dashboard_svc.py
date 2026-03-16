"""
Unit tests for the dashboard service (dashboard_svc.py).

Covers:
- Open tasks scanning across all files
- Section heading context for tasks
- Property card extraction from Field/Value tables
- Pinned file (TASKS.md, DASHBOARD.md) rendering
- Edge cases: missing files, missing fields, no properties

AC codes tested:
- AC-F5.2: Open Tasks widget
- AC-F5.3: Recently Modified Files widget (delegates to filesystem)
- AC-F5.4: TASKS.md & DASHBOARD.md widget
- AC-F5.5: Property Quick-Reference Cards widget

Related issues: S3-02, S3-03, S3-04, S3-05, S3-06
Related risks: R-18 (inconsistent table format)
"""

import pytest


# ---------------------------------------------------------------------------
# Open tasks scanning
# ---------------------------------------------------------------------------

class TestOpenTasksScanning:
    """Tests for scanning all files for unchecked checkboxes."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_open_tasks_scans_all_md_files(self, tmp_repo):
        """
        Tests AC-F5.2: Given markdown files across the repo contain '- [ ]' checkboxes,
        when get_open_tasks is called, then all unchecked tasks are found.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_open_tasks_excludes_webapp_files(self, tmp_repo):
        """
        Tests AC-F5.2: Given a file inside webapp/ contains checkboxes,
        then those tasks are NOT included in the results.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_open_tasks_excludes_checked_tasks(self, tmp_repo):
        """
        Tests AC-F5.2: Given some checkboxes are checked '- [x]',
        they are not included in the open tasks list.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_open_tasks_grouped_by_file(self, tmp_repo):
        """
        Tests AC-F5.2: Given tasks exist in multiple files, then results
        are grouped by source file with the file path included.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_open_tasks_includes_heading_context(self, tmp_repo):
        """
        Tests AC-F5.2: Given a task exists under a markdown heading (e.g., ## In Progress),
        then the section heading is included alongside the task.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_open_tasks_count(self, tmp_repo):
        """
        Tests AC-F5.2: Given there are N open tasks across the repo,
        then the total count matches the actual number of unchecked checkboxes.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_open_tasks_empty_when_none_exist(self, tmp_repo):
        """
        Tests AC-F5.2: Given no open tasks exist anywhere in the repo,
        then the results list is empty.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_open_tasks_excludes_code_block_checkboxes(self, tmp_repo):
        """
        Tests R-06: Given checkbox syntax inside code blocks, those are NOT
        counted as open tasks.
        """


# ---------------------------------------------------------------------------
# Property cards
# ---------------------------------------------------------------------------

class TestPropertyCards:
    """Tests for property quick-reference card extraction."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_property_cards_extracts_from_field_value_table(self, tmp_repo):
        """
        Tests AC-F5.5: Given a property README contains a '| Field | Value |' table,
        when get_property_cards is called, then the card extracts and displays
        the corresponding values.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_property_cards_extracts_address(self, tmp_repo):
        """
        Tests AC-F5.5: Given the README contains a row where Field is 'Address',
        then the card includes the address value.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_property_cards_extracts_year_built(self, tmp_repo):
        """
        Tests AC-F5.5: Given the README contains a row where Field is 'Year built',
        then the card includes the year built value.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_property_cards_extracts_type(self, tmp_repo):
        """
        Tests AC-F5.5: Given the README contains a row where Field is 'Type',
        then the card includes the type value.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_property_cards_handles_missing_fields(self, tmp_repo):
        """
        Tests AC-F5.5 / R-18: Given a property README is missing expected fields
        (e.g., no 'Year built' row), then the card shows 'Unknown' or empty
        for those fields without errors.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_property_cards_handles_missing_readme(self, tmp_repo):
        """
        Tests AC-F5.5: Given a property directory exists but has no README.md,
        then no card is created for that directory.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_property_cards_no_properties_dir(self, tmp_repo):
        """
        Tests AC-F5.5: Given no properties/ directory exists,
        then get_property_cards returns an empty list.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_property_cards_no_properties_found(self, tmp_repo):
        """
        Tests AC-F5.5: Given no properties/*/README.md files exist,
        then get_property_cards returns an empty list.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_property_cards_includes_both_properties(self, tmp_repo):
        """
        Tests AC-F5.5: Given two property directories exist with README.md files,
        then two cards are returned.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_property_cards_includes_rel_path(self, tmp_repo):
        """
        Tests AC-F5.5: Given a property card, it includes the relative path
        to the README for linking purposes.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_property_cards_different_table_format_degrades_gracefully(self, tmp_repo):
        """
        Tests R-18: Given a property README uses a non-standard table format
        (not '| Field | Value |'), then the card shows defaults without errors.
        """


# ---------------------------------------------------------------------------
# Pinned files (TASKS.md, DASHBOARD.md)
# ---------------------------------------------------------------------------

class TestPinnedFiles:
    """Tests for TASKS.md and DASHBOARD.md pinned widget content."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_pinned_tasks_md_exists(self, tmp_repo):
        """
        Tests AC-F5.4: Given TASKS.md exists at the repo root, when get_pinned_file_content
        is called, then it returns exists=True and rendered HTML.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_pinned_dashboard_md_exists(self, tmp_repo):
        """
        Tests AC-F5.4: Given DASHBOARD.md exists at the repo root, when
        get_pinned_file_content is called, then it returns exists=True and rendered HTML.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_pinned_file_not_found(self, tmp_repo):
        """
        Tests AC-F5.4: Given TASKS.md does not exist, when get_pinned_file_content
        is called with 'TASKS.md', then it returns exists=False without error.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_pinned_tasks_md_checkboxes_are_interactive(self, tmp_repo):
        """
        Tests AC-F5.4: Given TASKS.md is rendered for the pinned widget,
        then checkboxes within it are interactive (rendered with HTMX attributes).
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_dashboard_pinned_dashboard_md_not_found(self, tmp_repo):
        """
        Tests AC-F5.4: Given DASHBOARD.md does not exist, when get_pinned_file_content
        is called with 'DASHBOARD.md', then it returns exists=False without error.
        """
