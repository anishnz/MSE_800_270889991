# Exercise 5: Hybrid Inheritance - Hospital Staff

## Problem Statement

A hospital wants to model its staff. Doctors and nurses are both people
who share basic information (a name), but each has its own ID. Senior
nurses are a special, more experienced kind of nurse who additionally
manage a specific ward.

The task is to demonstrate **hybrid inheritance** - a combination of
more than one type of inheritance in a single design - by combining
hierarchical inheritance (`Doctor` and `Nurse` both from `Person`) with
multilevel inheritance (`SeniorNurse` from `Nurse` from `Person`).

## Requirements

Create the following classes:

1. `Person` - top-level base class with `name` and `display_details()`.
2. `Doctor` (inherits from `Person`) - adds `doctor_id`.
3. `Nurse` (inherits from `Person`) - adds `nurse_id`.
4. `SeniorNurse` (inherits from `Nurse`) - adds `ward`.

## How It Works

```
                   Person
                (name)
               /        \
              /          \
         Doctor          Nurse
      (doctor_id)      (nurse_id)
                           |
                           |
                      SeniorNurse
                        (ward)
```

- `Person` is the top-level base class, storing `name`.
- `Doctor` and `Nurse` both inherit directly from `Person` - this part
  is **hierarchical inheritance** (more than one child sharing one
  parent).
- `SeniorNurse` inherits from `Nurse` (not directly from `Person`),
  forming a 3-level chain `Person -> Nurse -> SeniorNurse` - this part
  is **multilevel inheritance**.
- Combining both patterns in one class design is what makes this
  **hybrid inheritance**.
- Each class calls `super().__init__(...)` to reuse its immediate
  parent's constructor, and each `display_details()` calls
  `super().display_details()` before adding its own extra line, so
  `SeniorNurse.display_details()` ends up running the full
  `SeniorNurse -> Nurse -> Person` chain.
- `isinstance()` checks show that a `SeniorNurse` is a `Nurse` and a
  `Person`, but NOT a `Doctor` - it belongs to a different branch of
  the hierarchy even though both branches share the same root.

## Running the Program

```bash
python main.py
```

### Expected Output

```
---- Doctor ----
Name       : Dr. Anish Karki
Doctor ID  : DOC501

---- Nurse ----
Name       : Nurse Maya Lama
Nurse ID   : NUR301

---- Senior Nurse (Hybrid Inheritance) ----
Name       : Nurse Sunita Basnet
Nurse ID   : NUR105
Ward       : Cardiology Ward

Is senior_nurse a Nurse?  True
Is senior_nurse a Person? True
Is senior_nurse a Doctor? False
```

## Files

| File | Description |
|---|---|
| `main.py` | Class definitions and demonstration code |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
