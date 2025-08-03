# SPDX-License-Identifier: MIT
from fastapi.responses import RedirectResponse
import os
from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv
import requests
from .providers import gnews

# Load environment variables
load_dotenv()

app = FastAPI(
    title="GNews Fetcher API",
    description="Fetch AI news using GNews.io",
    version="1.0.0"
)


def get_api_key() -> str:
    """Get the API key from environment variables."""
    api_key = os.getenv("GNEWS_API_KEY")
    if not api_key:
        raise ValueError(
            "GNEWS_API_KEY environment variable is required but not set. "
            "Please configure it in your environment or .env file."
        )
    return api_key.strip()


@app.get("/")
async def root():
    """Health check endpoint that confirms API key configuration."""
    try:
        api_key_configured = bool(get_api_key())
    except ValueError:
        api_key_configured = False

    return {
        "status": "healthy",
        "message": "GNews Fetcher API is running",
        "api_key_configured": api_key_configured
    }


@app.get("/news")
async def get_news(
    query: str = Query(
        "latest",
        min_length=1,
        title="Search query",
        description="Search term for news"
    ),
    limit: int = Query(
        20,
        ge=1,
        le=20,
        title="Limit",
        description="Number of articles to return (1–20)"
    ),
    sort_by: str = Query(
        "publishedAt",
        pattern="^(publishedAt|title)$",
        title="Sort by",
        description='"publishedAt" or "title"'
    ),
    language: str = Query(
        "en",
        min_length=2,
        max_length=2,
        title="Language",
        description="Language code, e.g. en"
    ),
):
    """
    Fetch news articles from GNews.io.

    Args:
        query: Search query (default: "latest")
        limit: Number of articles to return (1-20)
        sort_by: Sort by "publishedAt" or "title"
        language: Language code (default: "en")

    Returns:
        JSON response with articles, total count, and query
    """
    # Ensure API key is present (return 502 if not)
    try:
        get_api_key()
    except ValueError as e:
        raise HTTPException(status_code=502, detail=str(e))

    try:
        # Use the GNews provider
        result = gnews.fetch(query, limit, sort_by, language)
        return result
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Request timeout")
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Error fetching news: {e}"
        )


@app.get("/ui", include_in_schema=False)
@app.get("/ui/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
