# Exercise 1: Single Inheritance - Employee Management System

## Problem Statement

A company wants to model its employees. Every employee has a name and an
employee ID. Managers are a special kind of employee who additionally
belong to a specific department.

The task is to demonstrate **single inheritance** by creating one base
class, `Employee`, and exactly one derived class, `Manager`, that
inherits from it.

## Requirements

Create the following classes:

1. `Employee` - base class with `name`, `employee_id`, and
   `display_details()`.
2. `Manager` (inherits from `Employee`) - adds a `department` attribute
   and overrides `display_details()` to also show the department.

## How It Works

- `Employee` is the parent (base) class. It stores `name` and
  `employee_id` and defines `display_details()` to print them.
- `Manager` inherits from `Employee` using `class Manager(Employee):`.
  This is **single inheritance**: exactly one child class (`Manager`)
  derived from exactly one parent class (`Employee`).
- `Manager.__init__` calls `super().__init__(name, employee_id)` to let
  `Employee` set up the shared attributes, then adds its own
  `department` attribute.
- `Manager` **overrides** `display_details()`: it calls
  `super().display_details()` to reuse the parent's printing logic, then
  prints the extra `department` line.
- `isinstance()` checks confirm that a `Manager` object is recognised as
  both a `Manager` and an `Employee` at runtime.

## Running the Program

```bash
python main.py
```

### Expected Output

```
---- Manager Details ----
Employee Name : Alice Johnson
Employee ID   : EMP1001
Department    : Human Resources

Is manager1 an Employee? True
Is manager1 a Manager? True
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
