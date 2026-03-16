"""
Unit tests for the config module (config.py).

Covers:
- Repo root auto-detection logic
- Settings dataclass defaults and overrides
- Port configuration
- Excluded directories set

AC codes tested:
- AC-F1.2: Repo root auto-detection
- AC-F1.3: Port handling

Related issues: S1-04
"""

import pytest


# ---------------------------------------------------------------------------
# Repo root detection
# ---------------------------------------------------------------------------

class TestRepoRootDetection:
    """Tests for the detect_repo_root() function."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_repo_root_resolves_from_config_file_location(self):
        """
        Tests AC-F1.2: Given the app lives in webapp/, when the app starts,
        then it resolves the repo root as the parent directory of webapp/
        without any CLI argument or environment variable.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_repo_root_contains_known_markers(self):
        """
        Tests AC-F1.2: Given the repo root is resolved, verify it contains
        expected markers (CLAUDE.md or .git directory).
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_repo_root_raises_on_missing_markers(self):
        """
        Tests AC-F1.2: Given the config file is not inside a valid repo,
        when detect_repo_root is called, then a RuntimeError is raised.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_repo_root_works_from_webapp_dir(self):
        """
        Tests AC-F1.1: Given the user runs the app from inside the webapp/
        directory, when the app starts, then it still correctly auto-detects
        the repo root as ../.
        """


# ---------------------------------------------------------------------------
# Settings dataclass
# ---------------------------------------------------------------------------

class TestSettings:
    """Tests for the Settings dataclass."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_settings_default_port(self):
        """
        Tests AC-F1.3: Given no port override, when Settings is created,
        then the default port is 8000.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_settings_default_host(self):
        """
        Verify the default host is 127.0.0.1 (localhost only).
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_settings_excluded_dirs_default(self):
        """
        Verify the default excluded_dirs set includes webapp, .git, .agents, .venv.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_settings_excluded_dirs_contains_webapp(self):
        """
        Verify 'webapp' is in the excluded directories set so webapp/ files
        are never shown in the file tree or search results.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_settings_auto_save_delay_default(self):
        """
        Verify the default auto-save delay is 2000ms.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_settings_preview_debounce_default(self):
        """
        Verify the default preview debounce is 400ms.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_settings_custom_port(self):
        """
        Given a custom port value, when Settings is created with that port,
        then the port attribute reflects the custom value.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_config_settings_webapp_dir_derived(self):
        """
        Verify webapp_dir is correctly derived as repo_root / 'webapp'.
        """
