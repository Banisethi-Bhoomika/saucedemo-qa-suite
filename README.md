# SauceDemo QA Automation Suite

UI and API test automation using Python, Pytest and Playwright, with a Page Object Model and GitHub Actions CI.

## What is tested
- **UI** (https://www.saucedemo.com): login (valid, locked-out, wrong password, empty fields, unauthenticated access), cart, sorting, checkout form validation, full purchase flow
- **API** (https://jsonplaceholder.typicode.com): GET, POST, filtering, schema check, 404 handling

## Setup
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Run
```bash
pytest                       # everything
pytest -m smoke              # critical-path checks only
pytest -m "not api"          # UI only
pytest -m api                # API only
pytest --headed              # watch the browser
pytest --browser firefox     # cross-browser
```
HTML report: `reports/report.html`

## Structure
```
pages/   Page Objects (locators + actions)
tests/   ui/ and api/ tests, shared fixtures in conftest.py
docs/    test plan and bug log
```
