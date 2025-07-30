# GNews Fetcher

[![CI](https://github.com/gesttaltt/gnews-fetcher/actions/workflows/ci.yml/badge.svg)](https://github.com/gesttaltt/gnews-fetcher/actions/workflows/ci.yml)  
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)  
[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A clean, well‑structured **FastAPI news aggregation service** that fetches real AI news using **GNews.io** and serves them through an HTTP API. Built with a **provider pattern architecture**, automated QA testing (pytest + Selenium), Docker support, and a complete CI/CD pipeline.

<div align="center">

<!-- Demo placeholder - production ready for Swagger UI -->
<img src="docs/demo-placeholder.gif" width="700" alt="FastAPI Swagger UI Demo" />

</div>

---

## Why I built this 🥅

A compact, production‑grade project showcasing:

1. **QA Automation expertise** – comprehensive unit + browser tests with 95%+ coverage
2. **Modern Python architecture** – FastAPI, provider pattern, type hints, Docker deployment  
3. **Real‑world adaptability** – originally NewsAPI, pivoted to GNews.io while maintaining test coverage and CI pipeline integrity

---

## Features

- **🚀 FastAPI** REST service with auto-generated OpenAPI documentation
- **📰 Live news** from GNews.io (100 requests/day free tier)
- **🔧 Provider pattern** – easily swap news sources without breaking changes
- **🧪 Comprehensive testing** – 12 API tests + 4 browser validation tests
- **🐳 Docker & Compose** ready for containerized deployment
- **⚙️ GitHub Actions CI** with automated code quality checks
- **🛡️ Robust error handling** with proper HTTP status codes
- **📋 Dual requirements** strategy for development vs production

---

## Quick Start

### Prerequisites

- Python 3.11+
- GNews API token from [gnews.io](https://gnews.io) (free tier available)
- Firefox browser (for Selenium tests, optional)

### Local Development

```bash
# Clone and setup
git clone https://github.com/gesttaltt/gnews-fetcher.git
cd gnews-fetcher

# Install all dependencies (dev + production)
pip install -r requirements.txt

# Configure API key
echo "GNEWS_API_KEY=your_token_here" > .env

# Start development server
cd app
uvicorn news_app.api:app --reload

# Visit http://localhost:8000/docs for interactive API documentation
```

### Docker Deployment

```bash
# Set environment variable
export GNEWS_API_KEY=your_token_here

# Build and run
docker-compose up --build

# API available at http://localhost:8000
```

---

## API Documentation

### Health Check
```http
GET /
```
Returns API status and configuration validation.

### News Endpoint
```http
GET /news?query=AI&limit=10&sort_by=publishedAt&language=en
```

| Parameter  | Type   | Default       | Description                    |
|------------|--------|---------------|--------------------------------|
| `query`    | string | `"latest"`    | Search term for news articles |
| `limit`    | int    | `20`          | Number of articles (1-20)     |
| `sort_by`  | string | `"publishedAt"` | Sort by `publishedAt` or `title` |
| `language` | string | `"en"`        | Language code (ISO 639-1)     |

**Response Format:**
```json
{
  "articles": [...],
  "total": 10,
  "query": "AI"
}
```

> **Provider Abstraction**: FastAPI uses standard REST parameters, but GNews.io requires `q`, `max`, `lang`, `token`. The provider layer handles this transformation transparently.

---

## Development & Testing

### Code Quality
```bash
# Linting and formatting
flake8 . --exclude=.git,__pycache__,.pytest_cache,.vscode --statistics
autopep8 --diff --recursive --aggressive --aggressive . --exclude=.git,__pycache__,.pytest_cache,.vscode
```

### Testing Strategy
```bash
# P0 Critical tests (mocked APIs)
PYTHONPATH=app python -m pytest qa/tests/test_api.py -v

# P1 Browser integration tests
SKIP_BROWSER_TESTS=false PYTHONPATH=app python -m pytest qa/tests/test_browser.py -v

# All tests
PYTHONPATH=app python -m pytest qa/tests/ -v
```

**Test Coverage:**
- **12 API tests** – parameter validation, error handling, provider integration
- **4 browser tests** – Swagger UI accessibility, health endpoint validation
- **Mocked external calls** – no real API requests during CI/CD

---

## Architecture

### Provider Pattern
```
FastAPI App → Provider Interface → GNews.io API
    ↓              ↓                    ↓
Standard REST → Transform params → External API
Parameters      (query → q)          Integration
```

### Dual Requirements Strategy
- **Root `requirements.txt`**: Development + testing + production (CI/CD)
- **`app/requirements.txt`**: Production-only (Docker builds)

### Directory Structure
```
gnews-fetcher/
├── app/                      # Production application
│   ├── Dockerfile           # Container configuration
│   ├── requirements.txt     # Production dependencies only
│   └── news_app/
│       ├── api.py          # FastAPI application
│       └── providers/
│           └── gnews.py    # GNews.io API adapter
├── qa/                      # Quality assurance
│   ├── conftest.py         # Pytest fixtures
│   ├── browser_checks.py   # Selenium utilities
│   └── tests/
│       ├── test_api.py     # P0 Critical API tests
│       └── test_browser.py # P1 Browser validation
├── .github/workflows/ci.yml # GitHub Actions pipeline
├── docker-compose.yml      # Local container setup
├── render.yaml            # Render deployment config
└── requirements.txt       # Complete dependency stack
```

---

## Deployment

### Environment Variables

| Variable       | Required | Description                    |
|----------------|----------|--------------------------------|
| `GNEWS_API_KEY` | ✅       | GNews.io API token            |
| `PORT`         | ❌       | Override default port (8000)  |

### Render Deployment
```bash
# Render configuration (Python runtime)
Root Directory: app
Build Command: pip install -r requirements.txt  
Start Command: uvicorn news_app.api:app --host 0.0.0.0 --port $PORT
```

See [`RENDER_DEPLOYMENT.md`](RENDER_DEPLOYMENT.md) for detailed deployment guide.

### Docker Alternative
```bash
# Using docker-compose
export GNEWS_API_KEY=your_token
docker-compose up --build
```

---

## Contributing

### CI Pipeline
- **Automated testing** on every push/PR
- **Code quality checks** (flake8, autopep8)
- **Browser test validation** (optional in CI)
- **Firefox + geckodriver** setup for Selenium

### Development Workflow
1. Fork and clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Make changes and add tests
4. Run quality checks: `flake8 . && pytest qa/tests/ -v`
5. Submit pull request

---

## License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

## Links

- **API Documentation**: Visit `/docs` endpoint for interactive Swagger UI
- **Health Check**: Monitor service status at `/` endpoint  
- **Repository**: [github.com/gesttaltt/gnews-fetcher](https://github.com/gesttaltt/gnews-fetcher)
- **GNews.io**: [gnews.io](https://gnews.io) - News API provider
