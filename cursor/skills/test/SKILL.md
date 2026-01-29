---
name: test
description: Write and run tests to verify code functionality. Use for testing and verification tasks.
---

# Test Skill
Skill for writing and running tests to ensure code quality and functionality.

## When to Use
- After code implementation to verify functionality.
- Before merging code changes (regression tests).
- When acceptance criteria need validation.
- When debugging to create reproduction tests.

## Instructions
- **Test Types:**
    1. **Unit Tests:** Test individual functions/methods in isolation.
    2. **Integration Tests:** Test component interactions.
    3. **E2E Tests:** Test complete user flows (if applicable).
- **Writing Tests:**
    1. Follow AAA pattern: Arrange, Act, Assert.
    2. Test happy path and edge cases.
    3. Test error conditions and boundary values.
    4. Keep tests independent and repeatable.
    5. Use descriptive test names that explain the scenario.
- **Running Tests:**
    1. Run the test suite using project's test framework.
    2. Verify all tests pass before reporting.
    3. Report test coverage if required.
- **Output:**
    - Test files
    - Test results (passed/failed count)
    - Coverage report (if available)
- **Constraints:**
    - Tests must be deterministic (no flaky tests).
    - Do not skip failing tests without documenting the reason.
    - Tests should not depend on external services unless mocked.
