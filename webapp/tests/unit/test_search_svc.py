"""
Unit tests for the search service (search_svc.py).

Covers:
- File name matching (case-insensitive)
- Content matching (case-insensitive)
- Special character handling (literal, not regex)
- Exclusion of webapp/ and hidden directories
- Empty query handling
- Context lines around matches
- Multiple matches in one file

AC codes tested:
- AC-F6.2: File name search
- AC-F6.3: Content search
- AC-F6.4: Search exclusions
- AC-F6.5: Special characters in search
- AC-F6.7: Empty query

Related issues: S3-08, S3-09
Related risks: (none critical)
"""

import pytest


# ---------------------------------------------------------------------------
# File name matching
# ---------------------------------------------------------------------------

class TestFileNameSearch:
    """Tests for file name matching."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_filename_case_insensitive_match(self, tmp_repo):
        """
        Tests AC-F6.2: Given the query is 'tasks', when the search runs,
        then TASKS.md appears in the file name matches (case-insensitive).
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_filename_readme_matches_all(self, tmp_repo):
        """
        Tests AC-F6.2: Given the query is 'README', when the search runs,
        then all README.md files appear in the file name matches.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_filename_no_match(self, tmp_repo):
        """
        Tests AC-F6.2: Given the query is 'xyz123' and no file name contains
        this string, then the file name matches list is empty.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_filename_partial_match(self, tmp_repo):
        """
        Tests AC-F6.2: Given the query is 'dash', when the search runs,
        then DASHBOARD.md appears (partial filename match).
        """


# ---------------------------------------------------------------------------
# Content matching
# ---------------------------------------------------------------------------

class TestContentSearch:
    """Tests for content matching within files."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_content_case_insensitive_match(self, tmp_repo):
        """
        Tests AC-F6.3: Given the query is 'water heater', when the search runs,
        then files containing 'water heater' (case-insensitive) appear in results.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_content_includes_context_lines(self, tmp_repo):
        """
        Tests AC-F6.3: Given a content match, the result includes the matching line
        and 1 line of context above and below.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_content_multiple_matches_in_one_file(self, tmp_repo):
        """
        Tests AC-F6.3: Given the query appears multiple times in one file,
        then the file appears once in results with all matching lines shown.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_content_no_match(self, tmp_repo):
        """
        Tests AC-F6.3: Given the query is 'xyz123' and no file contains this string,
        then the content matches list is empty.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_content_match_at_first_line(self, tmp_repo):
        """
        Verify that a match on the first line of a file still works
        (context_before would be empty).
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_content_match_at_last_line(self, tmp_repo):
        """
        Verify that a match on the last line of a file still works
        (context_after would be empty).
        """


# ---------------------------------------------------------------------------
# Search exclusions
# ---------------------------------------------------------------------------

class TestSearchExclusions:
    """Tests for search exclusions (webapp/, hidden dirs)."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_excludes_webapp_files(self, tmp_repo):
        """
        Tests AC-F6.4: Given a file inside webapp/ contains the search query,
        then that file does NOT appear in search results.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_excludes_git_directory(self, tmp_repo):
        """
        Tests AC-F6.4: Given a file inside .git/ contains the search query,
        then that file does NOT appear in search results.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_excludes_agents_directory(self, tmp_repo):
        """
        Tests AC-F6.4: Given a file inside .agents/ contains the search query,
        then that file does NOT appear in search results.
        """


# ---------------------------------------------------------------------------
# Special characters
# ---------------------------------------------------------------------------

class TestSpecialCharacters:
    """Tests for special character handling in search queries."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_special_chars_dollar_sign(self, tmp_repo):
        """
        Tests AC-F6.5: Given the query contains '$500', then the dollar sign
        is treated literally, not as regex.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_special_chars_checkbox_syntax(self, tmp_repo):
        """
        Tests AC-F6.5: Given the query is '- [ ]', when the search runs,
        then it finds files containing the literal string '- [ ]'.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_special_chars_hash(self, tmp_repo):
        """
        Tests AC-F6.5: Given the query contains '#', then it is treated
        literally (finds heading lines).
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_special_chars_bold_syntax(self, tmp_repo):
        """
        Tests AC-F6.5: Given the query is '**bold**', then the asterisks
        are treated literally, not as regex.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_special_chars_parentheses(self, tmp_repo):
        """
        Tests AC-F6.5: Given the query contains parentheses (e.g., '(ASAP)'),
        then they are treated literally.
        """


# ---------------------------------------------------------------------------
# Empty query
# ---------------------------------------------------------------------------

class TestEmptyQuery:
    """Tests for empty or blank queries."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_empty_query_returns_no_results(self):
        """
        Tests AC-F6.7: Given an empty search query (''), when search is called,
        then no results are returned.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.unit
    def test_search_whitespace_only_query_returns_no_results(self):
        """
        Tests AC-F6.7: Given a whitespace-only query ('   '), when search is called,
        then no results are returned.
        """
