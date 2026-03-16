"""
Integration tests for search API routes (search router).

Covers:
- GET /search?q=term — search results page

AC codes tested:
- AC-F6.1: Search input availability
- AC-F6.2: File name search
- AC-F6.3: Content search
- AC-F6.4: Search exclusions
- AC-F6.5: Special characters
- AC-F6.6: Search results page
- AC-F6.7: Empty query
- AC-F6.8: Search performance

Related issues: S3-08, S3-09, S3-10, S3-12
"""

import pytest


class TestSearchRoute:
    """Tests for GET /search endpoint."""

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_search_returns_200(self, app_client):
        """
        Tests AC-F6.6: Given a valid search query, when GET /search?q=term is called,
        then the response is 200.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_search_returns_file_name_matches(self, app_client, tmp_repo):
        """
        Tests AC-F6.2: Given the query matches a file name, the response
        contains file name matches with links.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_search_returns_content_matches(self, app_client, tmp_repo):
        """
        Tests AC-F6.3: Given the query matches content in files, the response
        contains content matches with snippets and context.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_search_preserves_query_in_input(self, app_client):
        """
        Tests AC-F6.6: Given the search results page is displayed, then the
        search query is preserved in the search input field.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_search_results_include_sidebar(self, app_client):
        """
        Tests AC-F6.6: Given the search results page is displayed, then the
        sidebar file tree remains visible.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_search_no_results_shows_message(self, app_client):
        """
        Tests AC-F6.3: Given no results are found for the query, then a clear
        'No results' message is displayed.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_search_empty_query_shows_message(self, app_client):
        """
        Tests AC-F6.7: Given an empty or whitespace-only query, then a message
        like 'Please enter a search term' is shown.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_search_excludes_webapp_files(self, app_client, tmp_repo):
        """
        Tests AC-F6.4: Given the search query matches content in webapp/ files,
        then those files do NOT appear in results.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    def test_search_special_characters_literal(self, app_client, tmp_repo):
        """
        Tests AC-F6.5: Given the query contains special characters like '$500',
        they are treated as literal strings in the search.
        """

    @pytest.mark.skip(reason="Not yet implemented")
    @pytest.mark.integration
    @pytest.mark.slow
    def test_search_performance_under_one_second(self, app_client, tmp_repo):
        """
        Tests AC-F6.8: Given a repo with ~60 markdown files, when a content search
        is performed, then results are returned within 1 second.
        """
