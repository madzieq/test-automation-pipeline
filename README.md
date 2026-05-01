# test-automation-pipeline
Python test automation framework | REST API &amp; UI tests (Selenium) | Docker | GitHub Actions CI/CD | pytest

Test automation framework built with Python, covering both REST API and UI layers.
Tests run inside a Docker container and are triggered automatically via GitHub Actions CI/CD pipeline.

---
## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Main programming language |
| pytest | Test framework |
| requests | REST API testing |
| Selenium | UI browser automation |
| Page Object Model | UI test design pattern |
| Docker | Test containerisation |
| GitHub Actions | CI/CD pipeline |
| pytest-html | HTML test report generation |

## Project Structure

```
test-automation-pipeline/
├── tests/
│   ├── api/
│   │   └── test_posts.py       # REST API tests
│   └── ui/
│       └── test_login.py       # Selenium UI tests
├── pages/
│   └── login_page.py           # Page Object Model
├── conftest.py                 # pytest fixtures (WebDriver setup)
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker image definition
├── .github/
│   └── workflows/
│       └── tests.yml           # GitHub Actions CI/CD pipeline
└── README.md
```

## Test Coverage

### REST API Tests — JSONPlaceholder API
- GET /posts/{id} — returns HTTP 200 for multiple valid IDs
- GET /posts/{id} — response contains all required fields
- GET /posts — returns list of 100 posts
- POST /posts — creates a post and returns HTTP 201
- DELETE /posts/{id} — returns HTTP 200

### UI Tests — The Internet (Selenium)
- Successful login with valid credentials
- Failed login with invalid credentials (parametrized — 4 combinations)
- Login form visibility on page load

---

## How to Run

### Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html
```

### With Docker
```bash
# Build Docker image
docker build -t test-automation-pipeline .

# Run tests and generate HTML report
docker run -v ${PWD}/reports:/app/reports test-automation-pipeline
```

---

## CI/CD Pipeline

Tests run automatically on every push and pull request to `main` branch via GitHub Actions.

After each run:
- full test results are visible in the **Actions** tab
- HTML report is available as a downloadable **Artifact**

---

## Test Report

HTML report is generated automatically after each test run.
Available as artifact in GitHub Actions → select a run → **Artifacts** → `test-report`.