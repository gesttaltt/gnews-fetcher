# GNews Fetcher Makefile
# Development and QA automation

.PHONY: help install dev test ci clean coverage format lint

# Default target
help:
	@echo "GNews Fetcher - Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make dev        - Start development server"
	@echo "  make test       - Run tests only"
	@echo "  make ci         - Run full QA pipeline"
	@echo "  make coverage   - Run coverage analysis"
	@echo "  make format     - Format code with autopep8"
	@echo "  make lint       - Run linting checks"
	@echo "  make clean      - Clean cache files"

# Install dependencies
install:
	pip install -r requirements.txt

# Start development server
dev:
	cd app && uvicorn news_app.api:app --reload --host 0.0.0.0 --port 8000

# Run tests only (quick)
test:
	PYTHONPATH=app python -m pytest qa/tests/ -v

# Run full QA pipeline (comprehensive)
ci:
	./ci.sh

# Run coverage analysis
coverage:
	PYTHONPATH=app coverage run -m pytest qa/tests/
	coverage report --include="app/*" --omit="*/__pycache__/*,*/tests/*"
	coverage html --include="app/*" --omit="*/__pycache__/*,*/tests/*"

# Format code
format:
	autopep8 --in-place --recursive --aggressive --aggressive . --exclude=.git,__pycache__,.pytest_cache,.vscode

# Run linting
lint:
	flake8 . --exclude=.git,__pycache__,.pytest_cache,.vscode --statistics

# Clean cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	rm -rf htmlcov/ .coverage 2>/dev/null || true
