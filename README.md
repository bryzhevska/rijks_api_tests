# Rijksmuseum API Test Suite 🖼️ (with Pydantic)

A modular, reusable test automation framework for validating the Rijksmuseum's public API using Python, Pytest, Allure,
and Pydantic for JSON validation.

---

## 🔧 Features

- REST API Testing with `requests`
- JSON Validation using `Pydantic`
- Logging and debugging
- Secure API Key via `.env`
- Allure reports with features/stories
- GitHub Actions CI/CD integration

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repo-url>
cd rijks_api_tests
```

### 2. Set up environment

Create `.env`:

```
RIJKSMUSEUM_API_KEY=your_api_key
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run Tests locally

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

##  GitHub Actions

- CI runs tests and uploads Allure results.
- Make sure to add `RIJKSMUSEUM_API_KEY` to your GitHub secrets.

---

##  Identified issues (for which automated tests fail):
 - Request of an object with invalid ID does not result in 400(404) response code
 - ps parameter handled not as expected 

## Dashboard with test results
 - https://bryzhevska.github.io/rijks_api_tests/

