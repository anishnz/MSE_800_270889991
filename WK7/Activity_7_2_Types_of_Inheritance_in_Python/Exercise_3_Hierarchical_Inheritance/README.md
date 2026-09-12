# Exercise 3: Hierarchical Inheritance - University Employee Types

## Problem Statement

A university employs several different kinds of staff - lecturers,
administrators, and technicians - who all share basic employee
information (name and employee ID), but each has its own additional
specific attribute.

The task is to demonstrate **hierarchical inheritance** by having more
than one child class (`Lecturer`, `Administrator`, `Technician`) inherit
from the same single parent class (`Employee`).

## Requirements

Create the following classes:

1. `Employee` - base class with `name`, `employee_id`, and
   `display_details()`.
2. `Lecturer` (inherits from `Employee`) - adds `teaching_subject`.
3. `Administrator` (inherits from `Employee`) - adds `department`.
4. `Technician` (inherits from `Employee`) - adds
   `technical_specialisation`.

## How It Works

- `Employee` is the single shared parent class. It stores `name` and
  `employee_id` and defines `display_details()`.
- `Lecturer`, `Administrator`, and `Technician` each inherit from
  `Employee` independently - three separate branches all coming from
  the same parent. This is **hierarchical inheritance**: the opposite
  arrangement of multilevel inheritance, where MANY children share ONE
  parent (rather than a chain of single parent-child links).
- Each subclass calls `super().__init__(name, employee_id)` to reuse
  `Employee`'s constructor, then stores its own unique attribute
  (`teaching_subject`, `department`, or `technical_specialisation`).
- Each subclass overrides `display_details()`, calling
  `super().display_details()` first to print the shared fields, then
  adding its own extra line.
- The demonstration code creates one instance of each subclass and
  shows that, despite having different extra attributes, all three are
  recognised as `Employee` instances via `isinstance()`.

## Running the Program

```bash
python main.py
```

### Expected Output

```
---- Lecturer ----
Name        : Dr. Sita Rai
Employee ID : EMP2001
Teaching Subject : Data Structures

---- Administrator ----
Name        : Ramesh Gurung
Employee ID : EMP2002
Department       : Admissions Office

---- Technician ----
Name        : Hari Thapa
Employee ID : EMP2003
Specialisation   : Network Systems

All are Employees? True True True
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
