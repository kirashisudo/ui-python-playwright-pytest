# Playwright UI Tests for DemoBlaze

This repository contains an automated UI test suite for the **DemoBlaze** web application built with **Python**, **Pytest**, and **Playwright**.

The project demonstrates the Page Object Model (POM), reusable fixtures, and end-to-end testing of the application's core user scenarios.

## Tech Stack

* Python 3.11+
* Playwright
* Pytest
* Page Object Model (POM)

## Project Structure

```text
src/
└── ui/
    ├── pages/
    │   ├── base_page.py
    │   ├── cart_page.py
    │   ├── login_page.py
    │   └── ...
    ├── tests/
    │   ├── test_catalog.py
    │   ├── test_cart.py
    │   ├── test_login.py
    │   └── test_registration.py
    └── conftest.py
```

## Test Coverage

The project includes automated UI tests for the main (P0) user scenarios:

* Product catalog
* Product details page
* Shopping cart
* Add products to cart
* Remove products from cart
* Total price validation
* Successful login
* Invalid login
* User registration
* User logout

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create and activate a virtual environment.

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Running Tests

Run all tests:

```bash
python -m pytest src/ui/tests -q
```

Run a specific test:

```bash
python -m pytest src/ui/tests/test_login.py -q
```

Run with headed browser:

```bash
python -m pytest --headed
```

## Design

The framework follows the **Page Object Model (POM)** design pattern.

Key features:

* reusable Page Objects
* shared Pytest fixtures
* explicit waits
* stable dialog handling using `page.expect_event("dialog")`
* unique usernames for registration tests to avoid data collisions

## Future Improvements

* API testing
* Cross-browser execution
* GitHub Actions CI
* Allure reports
* Parallel execution with pytest-xdist

