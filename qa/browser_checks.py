"""
Browser validation functions for Selenium testing.
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_firefox_driver():
    """Get a configured Firefox WebDriver instance."""
    options = Options()
    options.add_argument("--headless")  # Run in headless mode for CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Firefox(options=options)
        driver.set_page_load_timeout(30)
        return driver
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Firefox driver: {e}")


def wait_for_element(driver, by, value, timeout=10):
    """Wait for an element to be present and return it."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except Exception as e:
        raise RuntimeError(f"Element {value} not found within {timeout}s: {e}")


def check_api_documentation(base_url):
    """Validate that API documentation is accessible."""
    driver = get_firefox_driver()
    try:
        # Check /docs endpoint
        driver.get(f"{base_url}/docs")
        wait_for_element(driver, By.TAG_NAME, "body")

        # Should contain FastAPI swagger UI elements
        title_element = wait_for_element(driver, By.TAG_NAME, "title")
        assert "FastAPI" in title_element.get_attribute("textContent") or \
               "GNews Fetcher" in title_element.get_attribute("textContent")

        return True
    finally:
        driver.quit()


def check_health_endpoint(base_url):
    """Check that the health endpoint returns valid HTML."""
    driver = get_firefox_driver()
    try:
        driver.get(base_url)
        wait_for_element(driver, By.TAG_NAME, "body")

        # Check if we get a valid response (might be JSON or HTML)
        page_source = driver.page_source.lower()

        # Should contain some indication of the API
        assert any(keyword in page_source for keyword in [
            "healthy", "status", "gnews", "api"
        ])

        return True
    finally:
        driver.quit()


def validate_news_response_structure(base_url):
    """
    Navigate to docs and validate the response structure description.
    This is a browser-level validation of API documentation.
    """
    driver = get_firefox_driver()
    try:
        driver.get(f"{base_url}/docs")
        time.sleep(2)  # Allow docs to load

        # Look for news endpoint documentation
        page_source = driver.page_source.lower()

        # Should mention key API elements
        assert "news" in page_source
        assert any(param in page_source for param in [
            "query", "limit", "sort", "language"
        ])

        return True
    finally:
        driver.quit()
