# Sonar Demo 2 – Student Grade Manager (Python)

## Run locally
```
pip install -r requirements.txt
python -m pytest --cov=src --cov-report=xml --cov-report=term
```
(You will see one harmless warning about `is 100`. That is the planted bug.)

Properties for later:
```
sonar.sources=src
sonar.tests=tests
sonar.python.coverage.reportPaths=coverage.xml
```

## Planted issues (all in src/grades.py)
| # | Line | Issue | Category |
|---|------|-------|----------|
| 1 | 3 | Hard-coded password `ADMIN_PASSWORD` (S2068/S6418) | Security |
| 2 | 31 | `eval()` on input (S1523) | Security (hotspot) |
| 3 | 13 | `score is 100` identity check with a literal (S5795) | Reliability |
| 4 | 26 | `raise "Invalid score"` raises a string, not an exception (S5632) | Reliability |
| 5 | 34 | Function has 8 parameters, limit is 7 (S107) | Maintainability |
| 6 | 44 | Unused local variable `total` (S1481) | Maintainability |
| 7 | 45 | Commented-out code (S125) | Maintainability |

Coverage starts at ~81%; the untested functions are `evaluate_formula`, `create_student`, `class_summary` and the error path.
Note: categories can vary slightly by SonarCloud version. Check your dashboard.

## Fixes (copy-paste)

### Fix 1 – hard-coded password
Add `import os` as the first line under the docstring, then replace line 3:
```
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
```

### Fix 2 – eval
Add `import ast` under the docstring, then:
```
def evaluate_formula(expression):
    return ast.literal_eval(expression)
```

### Fix 3 – `is` with literal
```
    if score == 100:
```

### Fix 4 – raising a string
```
        raise ValueError("Invalid score")
```

### Fix 5 – too many parameters
Replace the whole function with:
```
def create_student(first, last, age, grade, contact):
    return {
        "name": first + " " + last,
        "age": age,
        "grade": grade,
        "contact": contact,
    }
```

### Fix 6 and 7 – class_summary
Replace the whole function with:
```
def class_summary(scores):
    return average(scores)
```

## Optional: raise coverage
Change the import line in `tests/test_grades.py` to:
```
import pytest
from src.grades import average, letter_grade, validate_score, evaluate_formula, create_student, class_summary
```
and append:
```
def test_validate_score_bad():
    with pytest.raises(ValueError):
        validate_score(150)


def test_evaluate_formula():
    assert evaluate_formula("[1, 2]") == [1, 2]


def test_create_student():
    s = create_student("A", "B", 15, 9, "a@b.com")
    assert s["name"] == "A B"


def test_class_summary():
    assert class_summary([50, 100]) == 75
```
Then re-run: `python -m pytest --cov=src --cov-report=xml` and push `coverage.xml`. Coverage goes to 100%.
