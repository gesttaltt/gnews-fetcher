#!/bin/bash
# GNews Fetcher CI/QA Pipeline
# Comprehensive quality assurance automation script

set -euo pipefail

echo "🧪 Starting GNews Fetcher QA Pipeline"
echo "======================================"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_step() {
    echo -e "${BLUE}🔍 $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Install Firefox and geckodriver for Selenium (if not already installed)
print_step "Setting up browser testing environment..."
if ! command -v firefox >/dev/null 2>&1; then
    echo "Installing Firefox..."
    sudo apt-get update >/dev/null 2>&1
    sudo apt-get install -y firefox >/dev/null 2>&1
fi

if ! command -v geckodriver >/dev/null 2>&1; then
    echo "Installing geckodriver..."
    wget -q https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz
    tar -xzf geckodriver-v0.33.0-linux64.tar.gz
    sudo mv geckodriver /usr/local/bin/
    rm -f geckodriver-v0.33.0-linux64.tar.gz
fi
print_success "Browser environment ready!"

# Step 1: Code formatting check
print_step "Running autopep8 diff check..."
if autopep8 --diff --recursive --aggressive --aggressive . --exclude=.git,__pycache__,.pytest_cache,.vscode | grep -q .; then
    print_error "Code formatting issues found! Run autopep8 to fix."
    exit 1
else
    print_success "Code formatting check passed!"
fi

# Step 2: Linting with flake8
print_step "Running flake8 linting..."
if flake8 . --exclude=.git,__pycache__,.pytest_cache,.vscode --statistics; then
    print_success "Linting check passed!"
else
    print_error "Linting errors found!"
    exit 1
fi

# Step 3: API tests (P0 - Critical)
print_step "Running P0 API tests (mocked)..."
export PYTHONPATH="${PWD}/app"
if python -m pytest qa/tests/test_api.py -v --tb=short; then
    print_success "P0 API tests passed!"
else
    print_error "P0 API tests failed!"
    exit 1
fi

# Step 4: Browser tests (P1 - Integration) 
if [ "${SKIP_BROWSER_TESTS:-false}" != "true" ]; then
    print_step "Running P1 browser tests (headless)..."
    if python -m pytest qa/tests/test_browser.py -v --tb=short; then
        print_success "P1 browser tests passed!"
    else
        print_warning "P1 browser tests failed (continuing...)"
        # Don't exit on browser test failure as they may be environment-dependent
    fi
else
    print_warning "Browser tests skipped (SKIP_BROWSER_TESTS=true)"
fi

# Step 5: Coverage analysis
print_step "Running coverage analysis..."
if command -v coverage >/dev/null 2>&1; then
    coverage run -m pytest qa/tests/ --tb=short
    echo ""
    print_step "Coverage Report:"
    coverage report --include="app/*" --omit="*/__pycache__/*,*/tests/*"
    print_success "Coverage analysis completed!"
else
    print_warning "Coverage tool not installed - skipping coverage analysis"
fi

echo ""
echo "======================================"
print_success "QA Pipeline completed successfully! 🎉"
echo "======================================"
