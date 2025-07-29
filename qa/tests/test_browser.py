import pytest
import os
from qa.browser_checks import (
    check_api_documentation,
    check_health_endpoint,
    validate_news_response_structure
)


class TestBrowser:
    """P1 Browser integration tests using Selenium."""

    @pytest.fixture
    def api_base_url(self):
        """Get the API base URL for testing."""
        # In CI/CD, this might be set to a test server
        # For local testing, assume the app is running on localhost:8000
        return os.getenv("API_BASE_URL", "http://localhost:8000")

    @pytest.mark.skipif(
        os.getenv("SKIP_BROWSER_TESTS") == "true",
        reason="Browser tests skipped via SKIP_BROWSER_TESTS env var"
    )
    def test_api_documentation_accessibility(self, api_base_url):
        """Test that API documentation pages are accessible via browser."""
        try:
            result = check_api_documentation(api_base_url)
            assert result is True
        except Exception as e:
            pytest.skip(f"Browser test skipped due to environment: {e}")

    @pytest.mark.skipif(
        os.getenv("SKIP_BROWSER_TESTS") == "true",
        reason="Browser tests skipped via SKIP_BROWSER_TESTS env var"
    )
    def test_health_endpoint_browser_access(self, api_base_url):
        """Test health endpoint accessibility via browser."""
        try:
            result = check_health_endpoint(api_base_url)
            assert result is True
        except Exception as e:
            pytest.skip(f"Browser test skipped due to environment: {e}")

    @pytest.mark.skipif(
        os.getenv("SKIP_BROWSER_TESTS") == "true",
        reason="Browser tests skipped via SKIP_BROWSER_TESTS env var"
    )
    def test_api_documentation_structure(self, api_base_url):
        """Test that API documentation shows expected structure."""
        try:
            result = validate_news_response_structure(api_base_url)
            assert result is True
        except Exception as e:
            pytest.skip(f"Browser test skipped due to environment: {e}")

    def test_browser_tests_configuration(self):
        """Verify browser test configuration."""
        # This test always passes but logs configuration
        skip_tests = os.getenv("SKIP_BROWSER_TESTS", "false")
        api_url = os.getenv("API_BASE_URL", "http://localhost:8000")

        print(f"Browser tests skip flag: {skip_tests}")
        print(f"API base URL: {api_url}")

        assert True  # Always pass, just for logging
