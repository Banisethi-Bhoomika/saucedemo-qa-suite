# Test Plan: SauceDemo web app + JSONPlaceholder API

## Scope
UI: login, product listing (sort), cart, checkout. API: posts and comments endpoints.
Out of scope: performance, security, mobile devices.

## Approach
- UI automation: Pytest + Playwright (Python), Page Object Model.
- API automation: Pytest + requests.
- Test types: smoke (critical path), regression (broader), negative (failure paths and edge cases).
- Run in CI on every push via GitHub Actions; HTML report saved as an artifact.

## Test conditions covered
| Area | Happy path | Edge / failure |
|---|---|---|
| Login | valid user | locked-out, wrong password, empty fields, direct URL access without login |
| Cart | add, remove, badge count | sorting order checks |
| Checkout | full purchase, item total | missing first name / last name / postal code |
| API | GET, POST, filter | 404 on missing resource, schema check |

## Entry / exit criteria
Entry: site and API reachable. Exit: all smoke tests pass; every failure logged in docs/bug_log.md.
