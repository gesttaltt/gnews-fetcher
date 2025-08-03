# SPDX-License-Identifier: MIT
"""
GNews.io API provider for fetching news articles.
"""
import os
import requests
from typing import Dict, Any


def fetch(query: str, limit: int, sort_by: str,
          language: str) -> Dict[str, Any]:
    """
    Fetch news articles from GNews.io API.

    Args:
        query: Search query term
        limit: Number of articles to return (1-20)
        sort_by: Sort order - "publishedAt" or "title"
        language: Language code (e.g., "en")

    Returns:
        Dict containing articles, total count, and query

    Raises:
        ValueError: If GNEWS_API_KEY is not configured
        requests.exceptions.RequestException: If API request fails
    """
    api_key = os.getenv("GNEWS_API_KEY")
    if not api_key:
        raise ValueError(
            "GNEWS_API_KEY environment variable is required but not set. "
            "Please configure it in your environment or .env file."
        )

    # GNews API parameters mapping
    params = {
        "q": query,
        "max": limit,
        "lang": language,
        "token": api_key.strip()
    }

    # GNews doesn't support sort_by parameter in the same way,
    # but we'll store it for response consistency

    try:
        response = requests.get(
            "https://gnews.io/api/v4/search",
            params=params,
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        # Transform GNews response to match NewsAPI format
        articles = []
        if "articles" in data:
            for article in data["articles"]:
                # GNews structure is slightly different
                transformed_article = {
                    "title": article.get("title", ""),
                    "url": article.get("url", ""),
                    "description": article.get("description", ""),
                    "source": article.get("source", {}).get("name", "Unknown"),
                    "publishedAt": article.get("publishedAt", ""),
                    "urlToImage": article.get("image", "")
                }
                articles.append(transformed_article)

        # Sort articles if needed (client-side since GNews doesn't support it)
        if sort_by == "title":
            articles.sort(key=lambda x: x.get("title", "").lower())
        # Default is publishedAt (already sorted by GNews)

        return {
            "articles": articles,
            "total": len(articles),
            "query": query
        }

    except requests.exceptions.Timeout:
        raise requests.exceptions.Timeout("Request timeout")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Error fetching news: {e}")
