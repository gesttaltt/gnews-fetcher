# GNews Fetcher

[![CI](https://github.com/gesttaltt/gnews-fetcher/actions/workflows/ci.yml/badge.svg)](https://github.com/gesttaltt/gnews-fetcher/actions/workflows/ci.yml)  
[![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen.svg)](https://github.com/gesttaltt/gnews-fetcher)  
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)  
[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**🚀 Quick Start:** `pip install -r requirements.txt && make ci`

A **FastAPI news aggregation service** demonstrating **comprehensive QA methodologies** - combining **manual testing expertise** with automated validation for professional quality assurance.

<div align="center">

<!-- TODO: Replace with actual demo GIF showing 'make ci' execution -->
![Demo](docs/demo.gif)

</div>

---

## 🔍 Quality Assurance Focus

This project showcases **professional QA practices** suitable for **manual testing roles** with technical growth potential:

### **Manual Testing Excellence**
- 📋 **[Test Plan](qa/manual/test_plan.md)**: 8 comprehensive test cases with priority classification
- 🐛 **[Defect Tracking](qa/manual/defect_log.md)**: Professional bug lifecycle management
- 🔍 **[Exploratory Testing](qa/manual/exploratory_testing.md)**: Session-based investigation methodology
- 📊 **[QA Strategy](docs/QA_STRATEGY.md)**: Complete testing methodology documentation

### **Automated Testing Integration**
- **P0 Tests**: 12 API tests with mocked external dependencies
- **P1 Tests**: 4 browser tests for end-to-end validation  
- **CI/CD Pipeline**: Automated quality gates with manual QA validation
- **94% Code Coverage**: Comprehensive test coverage metrics

## Why I built this 🥅

A demonstration of **professional QA methodologies** combining:

1. **Manual Testing Expertise** – comprehensive test planning, defect management, and exploratory testing
2. **Technical Growth Potential** – automation understanding with Selenium and CI/CD integration  
3. **Real‑world Application** – functional news API with external service integration and proper error handling

Perfect for showcasing **manual QA skills** with **automation learning capabilities**.

---

## Features

- **📋 Manual Test Suite** – 8 priority-classified test cases with execution tracking
- **🐛 Professional Defect Management** – structured bug reporting and lifecycle tracking
- **🔍 Exploratory Testing** – documented session-based investigation methodology
- **🚀 FastAPI** REST service with auto-generated OpenAPI documentation
- **📰 Live news** from GNews.io (100 requests/day free tier)
- **🧪 Automated Integration** – pytest + Selenium browser testing
- **⚙️ CI/CD Pipeline** with manual QA validation and automated quality gates

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
cp .env.sample .env
# Edit .env with your GNews API key

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

### Manual Testing (Primary QA Focus)
```bash
# 1. Start application for manual testing
cd app && uvicorn news_app.api:app --reload

# 2. Execute manual test cases
# Follow: qa/manual/test_plan.md
# Update: Test execution tracking table
# Report: Use .github/ISSUE_TEMPLATE/bug_report.md

# 3. Conduct exploratory testing
# Document: qa/manual/exploratory_testing.md
```

### Code Quality
```bash
# Linting and formatting
flake8 . --exclude=.git,__pycache__,.pytest_cache,.vscode --statistics
autopep8 --diff --recursive --aggressive --aggressive . --exclude=.git,__pycache__,.pytest_cache,.vscode
```

### Automated Testing (CI/CD Integration)
```bash
# P0 Critical tests (mocked APIs)
PYTHONPATH=app python -m pytest qa/tests/test_api.py -v

# P1 Browser integration tests
SKIP_BROWSER_TESTS=false PYTHONPATH=app python -m pytest qa/tests/test_browser.py -v

# All automated tests
PYTHONPATH=app python -m pytest qa/tests/ -v
```

**QA Coverage:**
- **8 Manual Test Cases** – systematic test planning with priority classification
- **12 Automated API Tests** – parameter validation, error handling, provider integration
- **4 Browser Tests** – Swagger UI accessibility, health endpoint validation
- **Professional Defect Management** – structured bug reporting and tracking

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
