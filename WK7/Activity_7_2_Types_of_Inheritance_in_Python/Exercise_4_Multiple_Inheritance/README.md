# Exercise 4: Multiple Inheritance - University Student Academic + Contact Information

## Problem Statement

A university wants to record both academic information (programme, GPA)
and contact information (email, phone) for each student, but neither
piece of information fits neatly under the other.

The task is to demonstrate **multiple inheritance** by creating one
child class, `Student`, that inherits from two unrelated parent classes
at the same time: `AcademicInfo` and `ContactInfo`.

## Requirements

Create the following classes:

1. `AcademicInfo` - holds `programme`, `gpa`, and
   `display_academic_info()`.
2. `ContactInfo` - holds `email`, `phone`, and `display_contact_info()`.
3. `Student` (inherits from both `AcademicInfo` and `ContactInfo`) -
   adds `name` and `display_details()`.

## How It Works

- `AcademicInfo` and `ContactInfo` are two independent parent classes
  with no relationship to each other. Each stores its own data and
  defines its own display method.
- `Student` inherits from BOTH at once:
  `class Student(AcademicInfo, ContactInfo):`. Listing more than one
  class in the parentheses, separated by commas, is what creates
  **multiple inheritance** - one child class combining behaviour from
  several unrelated parents.
- Because both parents define `__init__`, and Python's Method
  Resolution Order (MRO) can make calling `super().__init__()` for both
  ambiguous, `Student.__init__` calls each parent's constructor
  explicitly by name instead:
  `AcademicInfo.__init__(self, programme, gpa)` and
  `ContactInfo.__init__(self, email, phone)`.
- `Student.display_details()` prints the student's name, then calls
  `display_academic_info()` (inherited from `AcademicInfo`) and
  `display_contact_info()` (inherited from `ContactInfo`).
- `isinstance()` checks confirm `Student` is recognised as both an
  `AcademicInfo` and a `ContactInfo`.
- The program also prints `Student.__mro__`, which shows the exact
  order Python uses to look up attributes/methods across the multiple
  parent classes.

## Running the Program

```bash
python main.py
```

### Expected Output

```
---- Student Details (Academic + Contact) ----
Name      : Priya Sharma
Programme : BSc Computer Science
GPA       : 3.8
Email     : priya.sharma@example.edu
Phone     : 98-1234-5678

Is student1 an AcademicInfo? True
Is student1 a ContactInfo?   True

Method Resolution Order (MRO):
 -> Student
 -> AcademicInfo
 -> ContactInfo
 -> object
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
