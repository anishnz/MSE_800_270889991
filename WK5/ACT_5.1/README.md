# Week 5 - Activity 5.1: Python Comprehensions and Data Structures

## Purpose

This folder contains a set of small, standalone Python exercises from
Week 5, Activity 5.1. Each script is a short, self-contained example
practicing one specific Python concept: list comprehensions, dictionary
comprehensions, the `enumerate()` function, building/merging dictionaries
from lists, filtering data with conditions, and basic matrix operations
using `numpy`.

## Files

| File | Description |
|---|---|
| `Dictionary_Comp.py` | Placeholder for a dictionary comprehension exercise; left empty in the original submission (documented with an explanatory docstring only). |
| `List_Comp_1.py` | Placeholder for a list comprehension exercise; left empty in the original submission (documented with an explanatory docstring only). |
| `List_com_2.py` | Attempts to flatten a 3x3 `numpy` matrix into a single list using a nested list comprehension over its rows. |
| `enumerate_for_looping.py` | Uses `enumerate()` in a for-loop to add a 5-point bonus to each grade in a list, except the 5th grade (index 4), which gets a 10-point bonus. |
| `even_index.py` | Placeholder noting the goal of filtering a list to keep only elements at an even index using `enumerate()` and a list comprehension; no implementation code was written in the original submission. |
| `extract_info.py` | Uses a list comprehension to filter a list of dictionaries, keeping only the people whose `age` is greater than 25. |
| `main.py` | Builds a dictionary from two separate lists (keys and values) using `zip()` and `dict()`. |
| `matrix.py` | Performs matrix multiplication (dot product) of a 3x5 matrix and a 5x2 matrix using `numpy.dot()`. |
| `mergining_Dicti.py` | Builds two dictionaries from parallel key/value lists, merges them with `{**dict1, **dict2}`, then filters the merged result to keep only entries with an odd value. |
| `QUESTION_AND_ANSWER.txt` | One reconstructed question/answer pair per script, describing the exercise goal, approach, and output. |
| `README.md` | This file. |

There is also a Jupyter notebook, `Tips for Python_exercises(2).ipynb`, in
this folder. It contains reference tips/notes related to these
exercises and has been left untouched.

## How to Run

Each script can be run independently from within the `WK5/ACT_5.1`
directory, for example:

```bash
python Dictionary_Comp.py
python List_Comp_1.py
python List_com_2.py
python enumerate_for_looping.py
python even_index.py
python extract_info.py
python main.py
python matrix.py
python mergining_Dicti.py
```

Scripts that use `numpy` (`List_com_2.py` and `matrix.py`) require the
`numpy` package to be installed (`pip install numpy`).
