from news_app.api import app
import pytest
import sys
import os
from fastapi.testclient import TestClient

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))


@pytest.fixture
def client():
    """FastAPI test client fixture."""
    return TestClient(app)


@pytest.fixture
def mock_gnews_response():
    """Mock response from GNews.io API."""
    return {
        "articles": [
            {
                "title": "AI Technology Breakthrough in 2025",
                "url": "https://example.com/ai-breakthrough",
                "description": "Revolutionary AI development",
                "source": {"name": "Tech News"},
                "publishedAt": "2025-01-15T10:00:00Z",
                "image": "https://example.com/image1.jpg"
            },
            {
                "title": "Machine Learning Advances",
                "url": "https://example.com/ml-advances",
                "description": "New machine learning techniques",
                "source": {"name": "AI Weekly"},
                "publishedAt": "2025-01-14T08:30:00Z",
                "image": "https://example.com/image2.jpg"
            }
        ]
    }
