# LendQA UI — Playwright Test Suite

End-to-end UI automation suite built with Python Playwright and pytest, demonstrating
login validation, session management, and access control patterns common in FinTech platforms.

## Tech Stack
- **Testing:** Python, Playwright, pytest, pytest-playwright
- **Pattern:** Page Object Model (POM)
- **CI:** GitHub Actions

## What's Tested (13 test cases)

| Area | Scenarios |
|---|---|
| Page Load | Title and all form elements visible |
| Valid Login | Redirects to secure area, success message shown |
| Invalid Login | Wrong password error, wrong username error |
| Edge Cases | Empty username, empty password |
| Session Security | Logout redirects to login, logout message shown |
| Access Control | Direct URL access to secure area without login is blocked |

## Project Structure

```
project2-ui-testing/
├── pages/
│   ├── login_page.py     ← selectors + actions for login page
│   └── secure_page.py    ← selectors + actions for secure area
├── tests/
│   ├── conftest.py       ← shared fixtures (login_page, logged_in)
│   ├── test_login.py     ← all login scenarios
│   └── test_secure_area.py ← post-login behavior
```

## Run Locally

```bash
pip install -r requirements.txt
playwright install chromium
pytest -v
```

## CI
Tests run automatically on every push via GitHub Actions with report uploaded as artifact.
# lendqa-ui-tests
# lendqa-ui-tests
# lendqa-ui-tests
