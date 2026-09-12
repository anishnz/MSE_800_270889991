# Activity 7.2: Types of Inheritance in Python

## Overview

This activity demonstrates the different types of inheritance supported
by Python's object-oriented model. Each exercise is a small, self-contained
program (`main.py`, run directly with `python main.py`) that focuses on
one type of inheritance, using its own themed example system. Every
exercise folder contains its own `README.md` and `QUESTION_AND_ANSWER.txt`
with more detail, an explanation of the class design, and the exact
program output.

## Exercises

| # | Folder | Inheritance Type | Example System |
|---|---|---|---|
| 1 | [Exercise_1_Single_Inheritance](Exercise_1_Single_Inheritance) | **Single Inheritance** - one child class inherits from exactly one parent class | Employee Management System (`Employee` -> `Manager`) |
| 2 | [Exercise_2_Multilevel_Inheritance](Exercise_2_Multilevel_Inheritance) | **Multilevel Inheritance** - a chain of more than one level, each class derived from the one above it | University Student Information System (`Person` -> `Student` -> `PostgraduateStudent`) |
| 3 | [Exercise_3_Hierarchical_Inheritance](Exercise_3_Hierarchical_Inheritance) | **Hierarchical Inheritance** - more than one child class inherits from the same single parent class | University Employee Types (`Employee` -> `Lecturer` / `Administrator` / `Technician`) |
| 4 | [Exercise_4_Multiple_Inheritance](Exercise_4_Multiple_Inheritance) | **Multiple Inheritance** - one child class inherits from more than one parent class at once | Student Academic + Contact Information (`Student` <- `AcademicInfo`, `ContactInfo`) |
| 5 | [Exercise_5_Hybrid_Inheritance](Exercise_5_Hybrid_Inheritance) | **Hybrid Inheritance** - a combination of hierarchical and multilevel inheritance in one design | Hospital Staff (`Person` -> `Doctor`/`Nurse`; `Nurse` -> `SeniorNurse`) |
| 6 | [Exercise_6_Custom_System_Hybrid_Inheritance](Exercise_6_Custom_System_Hybrid_Inheritance) | **Custom System - Hybrid Inheritance** (hierarchical + multilevel), plus a collaborating non-inherited class | Online Shopping Platform (`Person` -> `Customer`/`Employee`; `Employee` -> `Manager`; plus a standalone `Order` class) |

## How the Exercises Relate

- Exercises 1-4 each isolate ONE type of inheritance so the pattern is
  easy to recognise on its own: single (1), multilevel (2), hierarchical
  (3), and multiple (4).
- Exercise 5 shows that real designs often need MORE THAN ONE type at
  once - it deliberately combines hierarchical and multilevel
  inheritance into a single class hierarchy, which is the definition of
  hybrid inheritance.
- Exercise 6 applies the same hybrid idea to a larger, custom-designed
  system (an online shopping platform) with at least 5 classes, and adds
  a non-inheriting `Order` class to show that inheritance is only one of
  the relationships classes can have with each other (the other being
  plain object collaboration/composition).

## Running Any Exercise

From inside the relevant exercise folder:

```bash
python main.py
```

Each script is self-contained (classes plus an
`if __name__ == "__main__":` demonstration block) and requires no input
or external dependencies.
