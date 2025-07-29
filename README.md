# News Fetcher

[![CI](https://github.com/gesttaltt/news-fetcher/actions/workflows/ci.yml/badge.svg)](https://github.com/gesttaltt/news-fetcher/actions/workflows/ci.yml)  
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)  
[![License MIT](https://img.shields.io/github/license/gesttaltt/news-fetcher)](LICENSE)

A clean, well‑structured FastAPI application that fetches real AI news using **GNews.io** and serves them through an HTTP API. It ships with automated QA testing (pytest + Selenium), Docker support and a CI/CD pipeline on GitHub Actions.

<div align="center">

<!-- GIFs placeholder, still building-->
<img src="docs/demo-placeholder.gif" width="700" alt="Swagger UI demo" />

</div>

---

## Why I built this 🥅

I wanted a compact, production‑grade project to showcase:

1. **QA Automation skills** – solid unit + browser tests running on every push.  
2. **Modern Python stack** – FastAPI, type hints, Docker, GitHub Actions.  
3. **Real‑world troubleshooting** – originally used NewsAPI.org, but its free tier blocks remote calls (403). I pivoted to **GNews.io**, updated the adapter, and kept the tests/CI green without a full rewrite.

---

## Features

- **FastAPI** REST service with OpenAPI docs  
- **Live news** from GNews (free 100 req/day token)  
- **Pytest & Selenium** coverage (>90 %)  
- **Docker‑Compose** one‑liner run  
- **GitHub Actions** CI (lint + tests)  
- **Robust validation & error handling**  
- **Config via `.env`** – change provider in seconds

---

## Installation

### Prerequisites

- Python 3.11+  
- Docker & Docker Compose (optional)  
- Firefox browser (for Selenium tests)  
- GNews token from [gnews.io](https://gnews.io)

### Clone & Set Up

```bash
git clone https://github.com/gesttaltt/news-fetcher.git
cd news-fetcher
pip install -r requirements.txt
echo "GNEWS_API_KEY=your_token_here" > .env
cd app
uvicorn news_app.api:app --reload      # http://localhost:8000
````

### Docker

```bash
export GNEWS_API_KEY=your_token_here
docker-compose up --build              # http://localhost:8000
```

---

## Configuration

| Variable        | Required | Default | Description                  |
| --------------- | -------- | ------- | ---------------------------- |
| `GNEWS_API_KEY` | ✅        | —       | Personal token from gnews.io |
| `PORT`          | ❌        | `8000`  | Override container port      |

---

## API Endpoints

### Health Check

```http
GET /
```

### Get News

```http
GET /news?query=<term>&limit=<1‑20>&sort_by=<publishedAt|title>&language=<en>
```

| Param      | Type   | Default       | Notes       |
| ---------- | ------ | ------------- | ----------- |
| `query`    | string | `latest`      | Search term |
| `limit`    | int    | `20`          | 1‑20        |
| `sort_by`  | string | `publishedAt` | or `title`  |
| `language` | string | `en`          | ISO code    |

> **Note**: GNews uses `max` and `lang` under the hood—handled transparently by the adapter.

---

## Testing & QA

```bash
pytest qa/tests -v            # unit + browser tests
flake8 .                      # lint
```

* **P0** – critical API logic (`qa/tests/test_api.py`)
* **P1** – browser validation (`qa/tests/test_browser.py`)

---

## Project Structure

```text
news-fetcher/
├── README.md
├── requirements.txt
├── docker-compose.yml
├── .github/workflows/ci.yml
├── docs/                     # GIF / screenshots
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── news_app/
│       ├── __init__.py
│       └── api.py
└── qa/
    ├── browser_checks.py
    ├── conftest.py
    └── tests/
        ├── test_api.py
        └── test_browser.py
```

---

## License

Distributed under the **MIT License**.

```
::contentReference[oaicite:0]{index=0}
```
