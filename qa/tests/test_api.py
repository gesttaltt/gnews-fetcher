import os
from unittest.mock import patch, MagicMock
import requests


class TestAPI:
    """P0 Critical API tests with mocked GNews responses."""

    def test_root_endpoint(self, client):
        """Test the root health check endpoint."""
        response = client.get("/")
        assert response.status_code == 200

        data = response.json()
        assert "status" in data
        assert data["status"] == "healthy"
        assert "message" in data
        assert "api_key_configured" in data

    def test_root_endpoint_api_key_status(self, client):
        """Test API key configuration status in root endpoint."""
        with patch.dict(os.environ, {"GNEWS_API_KEY": "test_key"}):
            response = client.get("/")
            data = response.json()
            assert data["api_key_configured"] is True

        with patch.dict(os.environ, {}, clear=True):
            response = client.get("/")
            data = response.json()
            assert data["api_key_configured"] is False

    @patch('news_app.providers.gnews.requests.get')
    @patch.dict(os.environ, {"GNEWS_API_KEY": "test_api_key"})
    def test_news_endpoint_success(
            self,
            mock_requests,
            client,
            mock_gnews_response):
        """Test successful news fetching with default parameters."""
        # Mock the requests.get call
        mock_response = MagicMock()
        mock_response.json.return_value = mock_gnews_response
        mock_response.raise_for_status.return_value = None
        mock_requests.return_value = mock_response

        response = client.get("/news")
        assert response.status_code == 200

        data = response.json()
        assert "articles" in data
        assert "total" in data
        assert "query" in data
        assert data["query"] == "latest"

        # Check that articles are returned from GNews response
        assert isinstance(data["articles"], list)
        assert data["total"] == len(data["articles"])

    @patch('news_app.providers.gnews.requests.get')
    @patch.dict(os.environ, {"GNEWS_API_KEY": "test_api_key"})
    def test_news_endpoint_with_custom_query(
            self, mock_requests, client, mock_gnews_response):
        """Test news endpoint with custom query parameter."""
        mock_response = MagicMock()
        mock_response.json.return_value = mock_gnews_response
        mock_response.raise_for_status.return_value = None
        mock_requests.return_value = mock_response

        response = client.get("/news?query=machine+learning")
        assert response.status_code == 200

        data = response.json()
        assert data["query"] == "machine learning"

        # Verify GNews API was called with correct parameters
        mock_requests.assert_called_once()
        call_args = mock_requests.call_args
        assert call_args[1]["params"]["q"] == "machine learning"

    @patch('news_app.providers.gnews.requests.get')
    @patch.dict(os.environ, {"GNEWS_API_KEY": "test_api_key"})
    def test_news_endpoint_limit_parameter(
            self, mock_requests, client, mock_gnews_response):
        """Test news endpoint limit parameter enforcement."""
        mock_response = MagicMock()
        mock_response.json.return_value = mock_gnews_response
        mock_response.raise_for_status.return_value = None
        mock_requests.return_value = mock_response

        response = client.get("/news?limit=5")
        assert response.status_code == 200

        # Verify GNews API was called with correct limit (max parameter)
        mock_requests.assert_called_once()
        call_args = mock_requests.call_args
        assert call_args[1]["params"]["max"] == 5

    @patch.dict(os.environ, {"GNEWS_API_KEY": "test_api_key"})
    def test_news_endpoint_limit_validation(self, client):
        """Test limit parameter validation."""
        # Test limit too small
        response = client.get("/news?limit=0")
        assert response.status_code == 422

        # Test limit too large
        response = client.get("/news?limit=25")
        assert response.status_code == 422

    @patch.dict(os.environ, {"GNEWS_API_KEY": "test_api_key"})
    def test_news_endpoint_sort_by_validation(self, client):
        """Test sort_by parameter validation."""
        # Test invalid sort_by value
        response = client.get("/news?sort_by=invalid")
        assert response.status_code == 422

    @patch('news_app.providers.gnews.requests.get')
    @patch.dict(os.environ, {"GNEWS_API_KEY": "test_api_key"})
    def test_news_endpoint_sort_by_title(
            self, mock_requests, client, mock_gnews_response):
        """Test sorting by title."""
        mock_response = MagicMock()
        mock_response.json.return_value = mock_gnews_response
        mock_response.raise_for_status.return_value = None
        mock_requests.return_value = mock_response

        response = client.get("/news?sort_by=title")
        assert response.status_code == 200

        # Verify GNews API was called
        mock_requests.assert_called_once()
        call_args = mock_requests.call_args
        assert "gnews.io/api/v4/search" in call_args[0][0]

    @patch.dict(os.environ, {}, clear=True)
    def test_news_endpoint_no_api_key(self, client):
        """Test news endpoint when API key is not configured."""
        response = client.get("/news")
        assert response.status_code == 502  # Error due to None API key

    @patch('news_app.providers.gnews.requests.get')
    @patch.dict(os.environ, {"GNEWS_API_KEY": "test_api_key"})
    def test_news_endpoint_gnews_error(self, mock_requests, client):
        """Test handling of GNews API errors."""
        # Simulate an HTTP error from GNews
        mock_requests.side_effect = requests.exceptions.HTTPError(
            "HTTP Error")

        response = client.get("/news")
        assert response.status_code == 502

        data = response.json()
        assert "Error fetching news" in data["detail"]

    @patch('news_app.providers.gnews.requests.get')
    @patch.dict(os.environ, {"GNEWS_API_KEY": "test_api_key"})
    def test_news_endpoint_request_timeout(self, mock_requests, client):
        """Test handling of request timeouts."""
        mock_requests.side_effect = requests.exceptions.Timeout(
            "Request timeout")

        response = client.get("/news")
        assert response.status_code == 504

        data = response.json()
        assert "Request timeout" in data["detail"]

    @patch('news_app.providers.gnews.requests.get')
    @patch.dict(os.environ, {"GNEWS_API_KEY": "test_api_key"})
    def test_news_endpoint_language_parameter(
            self, mock_requests, client, mock_gnews_response):
        """Test language parameter mapping."""
        mock_response = MagicMock()
        mock_response.json.return_value = mock_gnews_response
        mock_response.raise_for_status.return_value = None
        mock_requests.return_value = mock_response

        response = client.get("/news?language=es")
        assert response.status_code == 200

        # Verify GNews API was called with correct language (lang parameter)
        mock_requests.assert_called_once()
        call_args = mock_requests.call_args
        assert call_args[1]["params"]["lang"] == "es"
