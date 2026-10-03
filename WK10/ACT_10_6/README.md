# Part E: Test Your Exceptions

## Problem Statement

Write a `unittest` class for Part D with at least five tests:

- a valid booking returns the correct total fee;
- an unknown car ID raises `CarNotFoundError`;
- an end date before the start date raises `InvalidDateRangeError`;
- an unavailable car raises `CarUnavailableError`, and the message
  contains the car's model;
- catching `RentalError` also catches each of the three specific
  errors.

## Requirements

1. Test the real `create_booking()` from Part D
   (`WK10/ACT_10_5/booking.py`) - not a copy of it.
2. At least five `unittest.TestCase` methods, one per bullet point
   above.
3. Each test must be independent (no test should depend on another
   test having run first).

## How It Works

- `sys.path.insert(0, ...)` adds `WK10/ACT_10_5` to Python's import
  search path (computed from `__file__`, so it works no matter where
  the tests are run from), and `from booking import ...` then imports
  the actual Part D module - the one tested here is the one graded in
  Part D, not a second copy that could quietly drift out of sync.
- `setUp()` runs before every single test method and rebuilds
  `self.cars` from scratch, so no test can be affected by changes an
  earlier test might have made to a shared dictionary.
- `self.assertRaises(SomeError)` is a context manager: if the code
  inside the `with` block raises `SomeError` (or a subclass of it), the
  test passes; if it raises something else, or nothing, the test fails.
  `as context:` captures the exception object so its message can be
  checked too (`context.exception`).
- Six tests are included (the exercise asks for at least five):
  1. a valid booking's `days` and `total_fee` are correct;
  2. an unknown car ID raises `CarNotFoundError`;
  3. an end date before the start date raises `InvalidDateRangeError`;
  4. an end date equal to the start date also raises
     `InvalidDateRangeError` (a zero-day booking is not valid either -
     an edge case worth covering on top of the required five);
  5. an unavailable car raises `CarUnavailableError`, and `"Civic"`
     (the car's model) is inside the exception's message;
  6. all three specific errors are also caught by
     `except RentalError:`, proven by looping over all three failure
     cases inside one `assertRaises(RentalError)`.

## Running the Program

```bash
python -m unittest test_booking -v
```

### Expected Output

```
test_end_date_before_start_raises_invalid_date_range_error ... ok
test_end_date_equal_to_start_raises_invalid_date_range_error ... ok
test_rental_error_catches_each_specific_subclass ... ok
test_unavailable_car_raises_car_unavailable_error_with_model_in_message ... ok
test_unknown_car_id_raises_car_not_found_error ... ok
test_valid_booking_returns_correct_total_fee ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.00Xs

OK
```

## Files

| File | Description |
|---|---|
| `test_booking.py` | Six `unittest` tests against Part D's `create_booking()` |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |

This folder depends on `WK10/ACT_10_5/booking.py` and does not work if
that file is moved or renamed without updating the `sys.path` line here.
