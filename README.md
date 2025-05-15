# ControlUp - Automation Home Test

This repository contains automation tests for both **UI** and **API** tasks as part of the ControlUp home assignment.

---

## 📁 Project Structure

```
ControlUp_Test/
├── ui/
│   ├── pages/          # Page Object Model classes
│   ├── tests/          # UI test files
│   ├── utils/          # Configuration and constants for UI
│   └── conftest.py     # Pytest driver fixture for Selenium
├── api/
│   ├── tests/          # API test files
│   ├── utils/          # Config and constants for API
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🚀 How to Run the Tests

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run all UI tests:
```bash
pytest ui/tests
```

3. Run all API tests:
```bash
pytest api/tests
```

4. Run both UI and API tests together:
```bash
pytest ui/tests api/tests
```

> ℹ️ If you encounter import errors (e.g., "ModuleNotFoundError"), run the following command from the **project root**, directly in your **terminal or command prompt**:
```bash
PYTHONPATH=. pytest ui/tests api/tests
```
---

## 🧪 UI Test Cases

### ✅ `test_01_inventory.py`
- Logs in and verifies that the inventory page shows exactly 6 items.

### ✅ `test_02_cart.py`
- Logs in, adds the first item to the cart, and checks that the cart badge shows `1`.

---

## 🧪 API Test Cases

### ✅ `test_airport_count.py`
- Sends a GET request to `/airports` and verifies that the response includes exactly 30 airports.

### ✅ `test_specific_airports.py`
- Verifies that the airports `"Akureyri Airport"`, `"St. Anthony Airport"` and `"CFB Bagotville"` are present in the `/airports` response.

### ✅ `test_airport_distance.py`
- Sends a POST request to `/airports/distance` with `from=KIX` and `to=NRT`, and verifies that the returned distance is greater than 400 kilometers.

---

## 🛠 Notable Decisions

- **Test files are numbered** (`test_01_...`, `test_02_...`) to enforce logical execution order in the UI tests.
- **JavaScript click** (`execute_script("arguments[0].click();", element)`) is used in UI tests when native Selenium click fails due to overlays or layout shifts. 
- **API payloads and expected data** (like airport names and distance limits) are kept in `constants.py` for clarity and maintainability.
- **Login logic** is abstracted into the `LoginPage` class and includes automatic navigation to the base URL.

---

## 📦 Tech Stack

- Python
- Selenium
- Pytest
- Requests
