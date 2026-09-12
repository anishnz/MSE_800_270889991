# Exercise 2: Multilevel Inheritance - University Student Information System

## Problem Statement

A university wants to model people, students, and postgraduate students
as a chain of increasingly specific roles: every postgraduate student is
a student, and every student is a person.

The task is to demonstrate **multilevel inheritance** by building a
3-level class chain: `Person` -> `Student` -> `PostgraduateStudent`.

## Requirements

Create the following classes:

1. `Person` - top-level base class with `name` and `display_details()`.
2. `Student` (inherits from `Person`) - adds `student_id`.
3. `PostgraduateStudent` (inherits from `Student`) - adds
   `research_topic`.

Each level should add its own extra attribute while keeping everything
defined above it in the chain.

## How It Works

- `Person` is the top-level base class. It stores `name` and defines
  `display_details()`.
- `Student` inherits from `Person` (level 1 of the chain). Its
  `__init__` calls `super().__init__(name)` to let `Person` set up the
  shared field, then adds `student_id`. Its `display_details()` calls
  `super().display_details()` before printing the extra line.
- `PostgraduateStudent` inherits from `Student` (level 2 of the chain).
  Because `Student` already inherits from `Person`,
  `PostgraduateStudent` automatically has access to both `Person`'s and
  `Student`'s attributes and methods. Its `__init__` calls
  `super().__init__(name, student_id)`, which in turn calls
  `Person.__init__` internally, initialising every level in one call.
- This forms a **multilevel inheritance** chain:
  `Person -> Student -> PostgraduateStudent`, where each class is
  derived from the class directly above it (not all from the same
  parent, which would instead be hierarchical inheritance).
- `isinstance()` checks confirm the resulting object is an instance of
  all three classes in the chain.

## Running the Program

```bash
python main.py
```

### Expected Output

```
---- Postgraduate Student Details ----
Name           : Bimal Shrestha
Student ID     : STU2025
Research Topic : Machine Learning in Healthcare

Is pg_student a Person?               True
Is pg_student a Student?              True
Is pg_student a PostgraduateStudent?  True
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
