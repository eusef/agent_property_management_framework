"""
Integration tests for server management routes (server router).

Covers:
- POST /api/shutdown — server shutdown
- App startup behavior

AC codes tested:
- AC-F1.1: Basic startup
- AC-F1.3: Port handling
- AC-F1.5: Shutdown via browser

Related issues: S1-03, S1-10, S2-11
Related risks: R-14 (port in use), R-15 (browser opens before ready), R-19 (package structure)
"""

import pytest


class TestShutdownRoute:
    """Tests for POST /api/shutdown endpoint."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_shutdown_returns_response(self, app_client):
        """
        Tests AC-F1.5: Given a POST /api/shutdown request, then the server
        returns a response with a 'server stopped' message before shutting down.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_shutdown_returns_goodbye_html(self, app_client):
        """
        Tests AC-F1.5: Given the confirmation is accepted, then the response
        contains a message like 'Server has been stopped. You can close this tab.'
        """


class TestAppStartup:
    """Tests for application startup behavior."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_app_creates_without_error(self):
        """
        Tests AC-F1.1 / R-19: Given the webapp package structure is correct,
        when the FastAPI app is instantiated, then no import errors occur.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_app_mounts_static_files(self, app_client):
        """
        Tests S1-11: Given the app is started, then static file serving
        is mounted and accessible.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_app_registers_all_routers(self, app_client):
        """
        Verify that all expected routers (dashboard, files, tasks, search, server)
        are registered with the app.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_app_templates_configured(self, app_client):
        """
        Verify that Jinja2 templates are configured and accessible.
        """
