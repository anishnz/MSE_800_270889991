# Part A: Predict the Output

## Problem Statement

Read each of four short snippets (A1-A4) and write down exactly what it
prints *before* running it. Then run it and compare. Each snippet uses
`try` / `except` / `else` / `finally` in a slightly different
combination.

## Requirements

1. A1: `try` / `except ValueError` / `finally`, where the `try` block
   raises.
2. A2: `try` / `finally` inside a function, where the `try` block
   returns.
3. A3: `try` / `except (IndexError, KeyError)` / `else`, where the
   `try` block raises.
4. A4: `try` / `except ZeroDivisionError` / `else`, where the `try`
   block succeeds.

## How It Works

- **A1** - `print("A")` runs, then `int("abc")` raises `ValueError`
  before `print("B")` is reached. The `except ValueError` block runs
  (`"C"`), and `finally` always runs last regardless of what happened
  above it (`"D"`).
- **A2** - `return "try"` does not exit the function immediately. Python
  runs any `finally` block first (printing `"cleanup"`), and only then
  does the function actually hand back `"try"` to `print(f())`.
- **A3** - `nums[5]` is out of range for a 3-item list, so `IndexError`
  is raised. It is one of the two types listed in
  `except (IndexError, KeyError) as e`, so `type(e).__name__` prints
  `"IndexError"`. `else` is skipped, because `else` only runs when the
  `try` block raised nothing at all.
- **A4** - `10 / 2` succeeds and prints `5.0` (division in Python always
  returns a float). No exception means `except` is skipped and `else`
  runs, printing `"ok"`.

## Running the Program

```bash
python main.py
```

### Expected Output

```
--- A1 ---
A
C
D

--- A2 ---
cleanup
try

--- A3 ---
IndexError

--- A4 ---
5.0
ok
```

## Files

| File | Description |
|---|---|
| `main.py` | The four snippets, each as its own function, with the predicted output written as a comment above it |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
