# Manual Test Plan - GNews Fetcher API

## 📋 Test Overview

| **Field** | **Details** |
|-----------|-------------|
| **Product** | GNews Fetcher API v1.0.0 |
| **Test Environment** | Development (localhost:8000) |
| **Test Period** | Ongoing |
| **Tester** | Manual QA Team |
| **Documentation** | [API Docs](http://localhost:8000/docs) |

## 🎯 Test Objectives

1. **Functional Validation**: Verify core news search functionality
2. **Error Handling**: Test invalid inputs and edge cases
3. **API Documentation**: Validate Swagger UI accuracy
4. **Integration**: Test external API connectivity
5. **Usability**: Assess API ease of use and error messages

## 🔧 Test Environment Setup

### Prerequisites
```bash
# 1. Start the application
cd app && uvicorn news_app.api:app --reload --port 8000

# 2. Verify health endpoint
curl http://localhost:8000/

# 3. Open API documentation
open http://localhost:8000/docs
```

### Test Data
- **Valid API Key**: Configured via GNEWS_API_KEY environment variable
- **Test Queries**: "technology", "AI", "python", "news"
- **Invalid Inputs**: Empty strings, special characters, oversized parameters

## 📝 Manual Test Cases

### **TC-001: Health Check Endpoint**
- **Priority**: P0 (Critical)
- **Type**: Smoke Test
- **Objective**: Verify application is running and configured

**Steps:**
1. Navigate to `GET http://localhost:8000/`
2. Verify HTTP status code is 200
3. Verify response JSON contains:
   - `service`: "GNews Fetcher API"
   - `status`: "healthy"
   - `api_key_configured`: boolean

**Expected Result:**
```json
{
  "service": "GNews Fetcher API",
  "status": "healthy",
  "api_key_configured": true,
  "version": "1.0.0"
}
```

---

### **TC-002: Basic News Search**
- **Priority**: P0 (Critical)
- **Type**: Functional Test
- **Objective**: Verify core news search functionality

**Steps:**
1. Send `GET http://localhost:8000/news?query=technology`
2. Verify HTTP status code is 200
3. Verify response contains `articles` array
4. Verify each article has: `title`, `description`, `url`, `publishedAt`
5. Verify `total` count matches articles array length

**Expected Result:**
```json
{
  "articles": [
    {
      "title": "Sample Article",
      "description": "Article description",
      "url": "https://example.com/article",
      "publishedAt": "2025-01-XX"
    }
  ],
  "total": 1,
  "query": "technology"
}
```

---

### **TC-003: Missing Query Parameter**
- **Priority**: P1 (High)
- **Type**: Negative Test
- **Objective**: Test parameter validation

**Steps:**
1. Send `GET http://localhost:8000/news` (no query parameter)
2. Verify HTTP status code is 422
3. Verify error message indicates missing required field
4. Verify response format follows FastAPI validation pattern

**Expected Result:**
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["query", "query"],
      "msg": "Field required"
    }
  ]
}
```

---

### **TC-004: Invalid Language Parameter**
- **Priority**: P1 (High)
- **Type**: Boundary Test
- **Objective**: Test language validation

**Steps:**
1. Send `GET http://localhost:8000/news?query=test&language=invalid`
2. Verify HTTP status code is 422
3. Verify error message indicates invalid language code
4. Test with valid languages: `en`, `es`, `fr`, `de`

**Expected Result:** 422 error for invalid language, 200 for valid languages

---

### **TC-005: Limit Parameter Boundary Testing**
- **Priority**: P2 (Medium)
- **Type**: Boundary Test
- **Objective**: Test limit parameter edge cases

**Test Data:**
- Valid: `1`, `10`, `100`
- Boundary: `0`, `101`, `-1`
- Invalid: `abc`, `1.5`

**Steps:**
1. Test each limit value with `GET /news?query=test&limit={value}`
2. Verify appropriate responses for each case
3. Document maximum allowed limit

---

### **TC-006: Sort Parameter Validation**
- **Priority**: P2 (Medium)
- **Type**: Functional Test
- **Objective**: Test sorting functionality

**Steps:**
1. Test `sort_by=publishedAt` - verify chronological order
2. Test `sort_by=relevance` - verify relevance-based order
3. Test invalid sort value - verify error handling

---

### **TC-007: API Documentation Accuracy**
- **Priority**: P1 (High)
- **Type**: Documentation Test
- **Objective**: Validate Swagger UI and documentation

**Steps:**
1. Navigate to `http://localhost:8000/docs`
2. Verify all endpoints are documented
3. Test "Try it out" functionality for each endpoint
4. Verify example responses match actual responses
5. Check parameter descriptions and types

---

### **TC-008: Special Characters in Query**
- **Priority**: P2 (Medium)
- **Type**: Edge Case Test
- **Objective**: Test query handling with special characters

**Test Data:**
- Unicode: `"héllo wørld"`
- Symbols: `"@#$%^&*()"`
- SQL-like: `"'; DROP TABLE--"`
- Encoding: `"query with spaces"`

**Steps:**
1. Test each special character scenario
2. Verify proper encoding/decoding
3. Verify no security vulnerabilities
4. Document any character limitations

## 🐛 Defect Reporting

When issues are found, use the [Bug Report Template](../../.github/ISSUE_TEMPLATE/bug_report.md) with these severity guidelines:

- **Critical**: Application crashes, security issues
- **High**: Core functionality broken, incorrect results
- **Medium**: Error messages unclear, minor functionality issues
- **Low**: Documentation errors, cosmetic issues

## 📊 Test Execution Tracking

| Test Case | Priority | Status | Executed By | Date | Notes |
|-----------|----------|---------|-------------|------|-------|
| TC-001 | P0 | ⏳ PENDING | - | - | - |
| TC-002 | P0 | ⏳ PENDING | - | - | - |
| TC-003 | P1 | ⏳ PENDING | - | - | - |
| TC-004 | P1 | ⏳ PENDING | - | - | - |
| TC-005 | P2 | ⏳ PENDING | - | - | - |
| TC-006 | P2 | ⏳ PENDING | - | - | - |
| TC-007 | P1 | ⏳ PENDING | - | - | - |
| TC-008 | P2 | ⏳ PENDING | - | - | - |

**Status Legend:**
- ✅ PASS
- ❌ FAIL  
- ⚠️ BLOCKED
- ⏳ PENDING
- 🔄 IN PROGRESS

## 📈 Test Summary Template

### Execution Summary
- **Total Test Cases**: 8
- **Executed**: 0
- **Passed**: 0
- **Failed**: 0
- **Blocked**: 0
- **Pass Rate**: N/A

### Key Findings
_To be updated during test execution_

### Recommendations
_To be updated based on test results_
