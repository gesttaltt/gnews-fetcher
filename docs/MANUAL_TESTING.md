# Manual Testing Guide

## Test Scenarios for GNews Fetcher

### Smoke Tests (P0) - Critical Path
- [ ] Application starts without errors (`uvicorn news_app.api:app`)
- [ ] Health endpoint returns 200 (`GET /`)
- [ ] API documentation accessible (`GET /docs`)
- [ ] API key status visible in health check

### Functional Tests (P1) - Core Features
- [ ] News search with valid query returns articles (`GET /news?query=AI`)
- [ ] Invalid API key returns 502 error
- [ ] Missing query parameter returns 422 error
- [ ] Language filter works correctly (`GET /news?query=tech&language=en`)
- [ ] Sort by date/relevance functions properly (`GET /news?query=tech&sort_by=publishedAt`)
- [ ] Limit parameter controls article count (`GET /news?query=tech&limit=5`)

### Browser Compatibility (P2) - Cross-Platform
- [ ] Firefox: API responses render correctly
- [ ] Chrome: Error messages display properly
- [ ] Edge: Documentation pages load
- [ ] Mobile browsers: Responsive API documentation

### Exploratory Testing Areas
- **Edge Cases**: Special characters in search queries (@#$%^&*)
- **Performance**: Very long search terms (500+ characters)
- **Load**: Rapid consecutive requests (stress testing)
- **Network**: Timeout scenarios and connection issues
- **Security**: SQL injection attempts in query parameters
- **Usability**: API documentation clarity and examples

### Test Data Sets
```bash
# Valid test queries
"artificial intelligence"
"machine learning"
"technology news"
"python programming"

# Edge case queries
"query with @special #characters"
""  # empty query
"a"  # single character
"very long query with many words to test parameter length limits and system behavior"

# Invalid parameters
limit=-1
limit=1000
sort_by=invalid_value
language=xyz
```

### Manual Execution Commands
```bash
# Start application
cd app && uvicorn news_app.api:app --reload

# Test endpoints manually
curl http://localhost:8000/
curl "http://localhost:8000/news?query=AI&limit=3"
curl "http://localhost:8000/docs"

# Browser testing
firefox http://localhost:8000/docs
```

### Expected Results Documentation
- **200 responses**: Should return JSON with articles array
- **4xx errors**: Should return clear error messages
- **5xx errors**: Should indicate server/API issues
- **API docs**: Should display interactive Swagger interface

---
*This manual testing guide complements automated P0/P1 tests and ensures comprehensive coverage for junior QA validation.*
