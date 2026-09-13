# University and Department Using Composition

## Problem Statement

A university has several departments. Each department has a name and a
head of department. The university should be able to display its details
along with the details of its department.

The task is to use composition to design this system.

## Requirements

Create two classes:

1. `Department`
   - Attributes: `department_name`, `head`
   - Method: `show_department()`
2. `University`
   - Attributes: `university_name`
   - Create a `Department` object inside the `University` class.
   - Method: `show_university()` should display the university and
     department details.

## How It Works

- `Department` is a standalone class that knows only about its own name
  and head, and how to display them via `show_department()`.
- `University` **has-a** `Department` — it creates and stores a
  `Department` object as one of its own attributes in `__init__`, rather
  than inheriting from it. This is **composition**.
- `show_university()` prints the university's own details, then
  **delegates** to `self.department.show_department()` to print the
  department's details, instead of duplicating that display logic.

## Running the Program

```bash
python main.py
```

### Expected Output

```
---- University Details ----
University: Yoobee Colleges
Department: Computer Science
Head of Department: Dr. Jane Smith
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
