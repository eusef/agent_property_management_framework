"""
Integration tests for dashboard and widget API routes (dashboard router).

Covers:
- GET / — dashboard home page
- GET /api/widget/open-tasks — open tasks widget
- GET /api/widget/recent-files — recently modified files widget
- GET /api/widget/pinned-files — TASKS.md & DASHBOARD.md widget
- GET /api/widget/property-cards — property quick-reference cards

AC codes tested:
- AC-F5.1: Dashboard is the home page
- AC-F5.2: Open Tasks widget
- AC-F5.3: Recently Modified Files widget
- AC-F5.4: TASKS.md & DASHBOARD.md widget
- AC-F5.5: Property Quick-Reference Cards widget
- AC-F5.6: Widget toggle behavior

Related issues: S3-01, S3-02, S3-03, S3-04, S3-05, S3-06, S3-07
"""

import pytest


# ---------------------------------------------------------------------------
# GET / — Dashboard
# ---------------------------------------------------------------------------

class TestDashboardRoute:
    """Tests for the dashboard home page route."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_dashboard_returns_200(self, app_client):
        """
        Tests AC-F5.1: Given the user navigates to /, then the response is 200.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_dashboard_contains_all_widgets(self, app_client):
        """
        Tests AC-F5.6: Given the dashboard loads for the first time,
        then all four widgets are rendered in the response.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_dashboard_includes_sidebar(self, app_client):
        """
        Tests AC-F2.9: Given the dashboard page, then the sidebar file tree
        is included in the response.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_dashboard_includes_search_input(self, app_client):
        """
        Tests AC-F6.1: Given the dashboard page, then a search input
        is visible in the response HTML.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_dashboard_home_link_points_to_root(self, app_client):
        """
        Tests AC-F5.1: Given the user clicks a 'Home' or logo link,
        then it navigates to /.
        """


# ---------------------------------------------------------------------------
# Widget endpoints
# ---------------------------------------------------------------------------

class TestOpenTasksWidget:
    """Tests for GET /api/widget/open-tasks."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_open_tasks_widget_returns_html_fragment(self, app_client):
        """
        Tests AC-F5.2: Given the widget endpoint is called, then it returns
        an HTML fragment suitable for HTMX swap.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_open_tasks_widget_lists_unchecked_tasks(self, app_client, tmp_repo):
        """
        Tests AC-F5.2: Given unchecked tasks exist, the widget HTML contains
        checkbox elements for each open task.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_open_tasks_widget_shows_count_in_header(self, app_client, tmp_repo):
        """
        Tests AC-F5.2: Given there are N open tasks, the widget header
        shows 'Open Tasks (N)'.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_open_tasks_widget_groups_by_file(self, app_client, tmp_repo):
        """
        Tests AC-F5.2: Given tasks exist in multiple files, the widget groups
        them by source file with clickable file path links.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_open_tasks_widget_checkboxes_are_interactive(self, app_client, tmp_repo):
        """
        Tests AC-F5.2: Given task checkboxes in the dashboard, they have
        HTMX attributes for toggling.
        """


class TestRecentFilesWidget:
    """Tests for GET /api/widget/recent-files."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_recent_files_widget_returns_html_fragment(self, app_client):
        """
        Tests AC-F5.3: Given the widget endpoint is called, then it returns
        an HTML fragment.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_recent_files_widget_lists_files_with_links(self, app_client, tmp_repo):
        """
        Tests AC-F5.3: Given recent files exist, each entry includes
        a clickable link to the file viewer.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_recent_files_widget_shows_mtime_and_size(self, app_client, tmp_repo):
        """
        Tests AC-F5.3: Given each file entry, it displays the last modified
        date/time and the file size.
        """


class TestPinnedFilesWidget:
    """Tests for GET /api/widget/pinned-files."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_pinned_files_widget_returns_html_fragment(self, app_client):
        """
        Tests AC-F5.4: Given the widget endpoint is called, then it returns
        an HTML fragment with rendered TASKS.md and DASHBOARD.md.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_pinned_files_widget_handles_missing_tasks_md(self, app_client, tmp_repo):
        """
        Tests AC-F5.4: Given TASKS.md does not exist, the widget shows
        'TASKS.md not found' without errors.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_pinned_files_widget_handles_missing_dashboard_md(self, app_client, tmp_repo):
        """
        Tests AC-F5.4: Given DASHBOARD.md does not exist, the widget shows
        'DASHBOARD.md not found' without errors.
        """


class TestPropertyCardsWidget:
    """Tests for GET /api/widget/property-cards."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_property_cards_widget_returns_html_fragment(self, app_client):
        """
        Tests AC-F5.5: Given the widget endpoint is called, then it returns
        an HTML fragment with property cards.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_property_cards_widget_shows_both_properties(self, app_client, tmp_repo):
        """
        Tests AC-F5.5: Given two property directories exist, the widget
        renders two cards.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_property_cards_widget_cards_link_to_readme(self, app_client, tmp_repo):
        """
        Tests AC-F5.5: Given a property card, clicking it or a 'View' link
        navigates to the full README for that property.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_property_cards_widget_no_properties(self, app_client, tmp_repo):
        """
        Tests AC-F5.5: Given no properties/*/README.md files exist,
        the widget shows 'No properties found.'
        """
