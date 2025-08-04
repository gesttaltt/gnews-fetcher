# QA Reports Directory

This directory contains test execution reports and artifacts generated during QA pipeline runs.

## Generated Files
- `coverage.xml` - Coverage report in XML format
- `test-results.xml` - JUnit-style test results
- `browser-screenshots/` - Screenshots from browser test failures
- `performance-metrics.json` - API response time measurements

## Retention Policy
- CI artifacts are retained for 30 days
- Local reports can be cleaned with `make clean`

## Viewing Reports
```bash
# View coverage report locally
coverage report
coverage html  # Generates htmlcov/index.html

# View test results
python -m pytest qa/tests/ -v --tb=short
```

*This directory is auto-created during CI runs and may be empty in fresh checkouts.*
