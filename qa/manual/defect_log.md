# Defect Tracking Log

## 🐛 Active Defects

### BUG-001: [SAMPLE] Language Parameter Validation
**Reported**: 2025-01-XX  
**Reporter**: QA Tester  
**Severity**: Medium  
**Priority**: P2  
**Status**: Open  
**Assigned**: Development Team

**Description**: 
Invalid language codes should return clear validation errors with supported language list.

**Environment**: 
- Local development server
- API version 1.0.0

**Steps to Reproduce**:
1. Send `GET /news?query=test&language=xyz`
2. Observe response

**Expected Result**: 
422 error with message listing supported languages (en, es, fr, de, etc.)

**Actual Result**: 
Generic validation error without helpful guidance

**Impact**: 
Users receive unclear error messages when using invalid language codes

**Workaround**: 
Reference API documentation for valid language codes

**Screenshots/Logs**:
```json
{
  "detail": "Invalid language code"
}
```

**Additional Notes**:
Consider adding a `/languages` endpoint to list supported languages

---

## 📊 Defect Metrics

### By Severity
- **Critical**: 0
- **High**: 0  
- **Medium**: 1
- **Low**: 0

### By Status
- **Open**: 1
- **In Progress**: 0
- **Resolved**: 0
- **Closed**: 0

### By Component
- **API Validation**: 1
- **Core Functionality**: 0
- **Documentation**: 0
- **UI/UX**: 0

## ✅ Resolved Defects

### BUG-000: [TEMPLATE] Sample Resolved Issue
**Reported**: 2025-01-XX  
**Resolved**: 2025-01-XX  
**Severity**: High  
**Status**: Closed  

**Description**: Template for resolved defects
**Resolution**: Fixed in commit abc123
**Verification**: Confirmed by QA on 2025-01-XX

---

## 📝 Defect Report Guidelines

### Severity Definitions
- **Critical**: System crash, data loss, security vulnerability
- **High**: Core functionality broken, blocks testing
- **Medium**: Feature works but with issues, unclear errors
- **Low**: Cosmetic issues, documentation errors

### Priority Guidelines
- **P0**: Fix immediately, blocks release
- **P1**: Fix in current sprint
- **P2**: Fix in next sprint
- **P3**: Fix when resources available

### Required Information
1. Clear, descriptive title
2. Steps to reproduce
3. Expected vs actual results
4. Environment details
5. Screenshots/logs when applicable
6. Business impact assessment

### Status Workflow
1. **Open**: Newly reported, awaiting triage
2. **In Progress**: Assigned and being worked on
3. **Resolved**: Fix implemented, awaiting verification
4. **Closed**: Verified as fixed by QA
5. **Rejected**: Not a valid defect

---

*This log should be updated regularly during manual testing activities.*
