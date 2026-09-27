# Adaptive Student Learning Path Recommendation Engine
### Subject: Python Programming — Core & Advanced | 2nd Year B.Tech / BSc CS

---

## How to Run

```bash
# Automated demo (no input needed — great for showing the project):
python demo.py

# Full interactive application:
python main.py
```

> Requires **Python 3.8+** — no third-party libraries needed.

---

## Project Structure

```
adaptive_learning_engine/
│
├── main.py              ← Entry point; interactive CLI menu
├── demo.py              ← Automated demo (no user input required)
│
├── student.py           ← Student class (OOP: encapsulation, methods)
├── quiz.py              ← Diagnostic quiz with 70+ questions
├── resources.py         ← 60+ learning resources for all 15 Python topics
├── recommendation.py    ← Adaptive path generation (core logic)
├── file_handler.py      ← JSON save/load for student profiles
│
└── data/
    └── students/        ← Saved student profiles (auto-created as .json files)
```

---

## Python Concepts Used

| File | Concept |
|---|---|
| `student.py` | Class, `__init__`, `self`, instance methods, `__str__`, `__repr__` |
| `quiz.py` | Dictionaries, tuples, `random.sample`, `if/elif/else`, `while` loop, `try/except` |
| `resources.py` | Nested dictionaries, lists, constants, helper functions |
| `recommendation.py` | Scoring formula, `sorted()` + lambda, list comprehensions, conditional logic, `for` loops |
| `file_handler.py` | `json.dump/load`, `with open()`, `os.path`, `os.makedirs`, exception handling |
| `main.py` | Modules & imports, `while` menu loop, `if/elif/else` routing, `if __name__ == "__main__"` |

---

## How the Adaptive Logic Works

### 1 — Diagnostic Quiz → Skill Level

```python
if score >= 70:
    return "advanced"       # ready for harder content
elif score >= 40:
    return "core"           # revise core first
else:
    return "core"           # needs fundamentals
```

### 2 — Resource Scoring Formula

```
score = style_alignment + (3 × weak_topic_match) − strong_topic_match + duration_bonus
```

Resources are sorted highest → lowest score, then selected until the daily time budget runs out.

### 3 — Learning Style → Resource Type Priority

| Style | Preferred Order |
|---|---|
| Visual | Video → Exercise → Quiz → Reading → Project |
| Reading | Reading → Quiz → Video → Exercise → Project |
| Hands-On | Exercise → Project → Video → Reading → Quiz |

### 4 — Topic Prioritisation

Weak topics always appear first in the daily plan, ensuring struggling students tackle their weakest areas when focus is highest.

---

## Features

- **Diagnostic Quiz** — 70+ questions across 15 Python topics (Core + Advanced)
- **Adaptive Level** — `if/elif/else` determines Core or Advanced per topic
- **Personalised Path** — Resources ranked by style match + weak topic boost
- **Time Budget** — Daily plan auto-fitted to your available study time
- **Progress Tracking** — Completion percentage per topic with a visual bar
- **Topic Prioritisation** — Weak topics appear first in the plan
- **Profile Persistence** — Student data saved as JSON, reloaded next session
- **Level Promotion** — When Core is complete, prompts to move to Advanced

---

## Available Topics (15 Python Topics)

| # | Topic | Levels |
|---|---|---|
| 1 | Variables & Data Types | Core + Advanced |
| 2 | Operators & Expressions | Core + Advanced |
| 3 | Control Flow | Core + Advanced |
| 4 | Loops | Core + Advanced |
| 5 | Functions | Core + Advanced |
| 6 | Strings | Core + Advanced |
| 7 | Lists & Tuples | Core + Advanced |
| 8 | Dictionaries & Sets | Core + Advanced |
| 9 | File Handling | Core + Advanced |
| 10 | Exception Handling | Core + Advanced |
| 11 | Object-Oriented Programming | Core + Advanced |
| 12 | Inheritance & Polymorphism | Core + Advanced |
| 13 | List Comprehensions & Lambdas | Core + Advanced |
| 14 | Modules & Packages | Core + Advanced |
| 15 | Decorators & Generators | Core + Advanced |
