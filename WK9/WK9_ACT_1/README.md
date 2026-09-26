# Student Result Management - Writing and Debugging with Python Tutor

## Problem Statement

Develop a simple student result management program. The program should:

- Ask the user to enter the names and marks of five students.
- Store the information in a list or dictionary.
- Calculate the average mark for each student.
- Display whether each student has Passed or Failed, based on a pass
  mark of 50.
- Calculate and display the class average.
- Identify the student with the highest mark.

Then deliberately introduce one or two errors (a wrong variable, a wrong
calculation, or a statement placed in the wrong part of a loop), run the
buggy program in [Python Tutor](https://pythontutor.com/), step through
it with the Forward button, find where it first produces a wrong result,
fix it, and confirm the fix.

## Requirements

1. Each student has a name and a mark in three subjects: Maths, Science,
   English.
2. `average` for a student = the sum of their three marks / 3.
3. `Passed` if `average >= 50`, otherwise `Failed`.
4. `class_average` = the sum of every student's average / the number of
   students.
5. The student with the highest average is reported.
6. A buggy first attempt, and the corrected program that followed it.

## The Two Bugs That Were Introduced

| # | File / line | Bug type (from the exercise) | What it does |
|---|---|---|---|
| 1 | `buggy_version.py`, `total = 0` before the student loop, `total += mark` inside it | Statement in the wrong part of a loop | `total` is never reset between students, so each student's average includes every earlier student's marks too. |
| 2 | `buggy_version.py`, `class_average = class_total / len(SUBJECTS)` | Incorrect variable used in a calculation | Divides by 3 (the number of subjects) instead of 5 (the number of students). |

Full details of how each one was found by stepping through Python
Tutor, and the exact fix, are in `QUESTION_AND_ANSWER.txt`.

## How It Works (corrected version, `main.py`)

- `read_student(position)` asks for one student's name and three marks,
  and returns `{"name": ..., "marks": [...], "average": ...}`. `total`
  and `average` are calculated fresh inside this function every time it
  is called, so nothing from a previous student can leak in.
- `main()` builds the list of five student records, then:
  - prints each student's average and Passed/Failed status;
  - computes `class_average` by dividing the sum of the five averages by
    `len(students)`;
  - finds the highest-average student with
    `max(students, key=lambda s: s["average"])`.

## Running the Program

```bash
python main.py
```

You will be prompted for a name and three marks per student, five times
in total.

### Expected Output (using the sample data below)

Sample input, one value per prompt, in order:

```
Alice, 80, 70, 90
Bob,   40, 55, 50
Cara,  60, 65, 70
Dan,   30, 20, 25
Eva,   95, 100, 90
```

Output:

```
--- Results ---
Alice: average = 80.00 -> Passed
Bob: average = 48.33 -> Failed
Cara: average = 65.00 -> Passed
Dan: average = 25.00 -> Failed
Eva: average = 95.00 -> Passed

Class average: 62.67
Highest average: Eva (95.00)
```

### Same Sample Data Run Through `buggy_version.py` (for comparison)

```
--- Results ---
Alice: average = 80.00 -> Passed
Bob: average = 128.33 -> Passed
Cara: average = 193.33 -> Passed
Dan: average = 218.33 -> Passed
Eva: average = 313.33 -> Passed

Class average: 311.11
Highest average: Eva (313.33)
```

Alice (the first student) is correct by accident - there is nothing
before her for `total` to have picked up. From Bob onwards every average
is wrong, and an "average" over 100 (a percentage-style mark) is an
immediate sign something is broken - that is exactly the kind of clue
Python Tutor makes visible one step at a time.

## Files

| File | Description |
|---|---|
| `buggy_version.py` | The first attempt: runs without crashing, but contains the two introduced bugs |
| `main.py` | The corrected, working program |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation, including the Python Tutor debugging trace |
| `README.md` | This file |
