# Part B: Safe Input

## Problem Statement

Write a function `read_int(prompt, minimum=None, maximum=None)` that
keeps asking the user until they enter a valid whole number.

- Non-numeric text must print "Please enter a whole number." and ask
  again.
- If a minimum or maximum is given, numbers outside that range must
  also be rejected with a clear message.
- The function must never crash, whatever the user types.

Test it with: `abc`, `0`, `99`, `5` and range 1 to 10.

## Requirements

1. `read_int(prompt, minimum=None, maximum=None)` loops until it has a
   value it can return.
2. Text that cannot convert with `int()` is rejected with
   "Please enter a whole number." and the loop asks again.
3. A number below `minimum` (when given) or above `maximum` (when
   given) is rejected with its own message, and the loop asks again.
4. `minimum` and `maximum` are optional - either (or both) can be left
   as `None`, in which case that side of the range is not checked.

## How It Works

- The `while True:` loop has exactly one way out: `return value`. Every
  other path through the function ends in `continue`, which jumps
  straight back to `input(prompt)`. That is what makes it impossible
  for the function to crash - there is no line of code that can raise
  and reach the caller.
- `int(text)` is the only place that can raise, and it is wrapped in
  its own `try`/`except ValueError`, so bad text is turned into a
  message rather than an exception.
- The range checks run only once `text` has already successfully become
  an `int`, and only when that side of the range (`minimum` /
  `maximum`) was actually supplied.

## Running the Program

```bash
python main.py
```

### Expected Output (entering `abc`, then `0`, then `99`, then `5`, with `minimum=1, maximum=10`)

```
Enter a whole number from 1 to 10: abc
Please enter a whole number.
Enter a whole number from 1 to 10: 0
Please enter a number that is at least 1.
Enter a whole number from 1 to 10: 99
Please enter a number that is at most 10.
Enter a whole number from 1 to 10: 5
You entered: 5
```

## Files

| File | Description |
|---|---|
| `main.py` | `read_int()` and a demonstration using the exercise's test sequence |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
