# Part D: Custom Exceptions for Car Rental

## Problem Statement

Using the car rental domain from the assessment:

1. Create a base exception `RentalError` and three subclasses:
   `InvalidDateRangeError`, `CarNotFoundError` and `CarUnavailableError`.
2. Write `create_booking(cars, car_id, start, end)` where `cars` is a
   dictionary mapping IDs to car dictionaries (`make`, `model`,
   `daily_rate`, `available`).
3. The function must raise the right custom exception for: unknown car
   ID, end date not after start date, and an unavailable car. It
   returns a booking dictionary with the number of days and total fee
   when everything is valid.
4. Write a small menu-style loop that asks for a car ID and dates, calls
   your function, and catches `RentalError` to print a friendly
   message. **The function itself must not use print or input.**

## Requirements

1. `booking.py` - the exception hierarchy and `create_booking()`, with
   no `print()`/`input()` anywhere in it.
2. `main.py` - the interactive menu loop: all user-facing text lives
   here, not in `booking.py`.
3. `create_booking()` checks, in order: does the car exist, is the date
   range valid, is the car available - then returns
   `{"car_id", "days", "total_fee"}`.

## How It Works

- The exception hierarchy:

  ```
  RentalError
  +-- InvalidDateRangeError
  +-- CarNotFoundError
  +-- CarUnavailableError
  ```

  Each subclass **is a** `RentalError` (through inheritance), so
  `except RentalError:` in `main.py` catches all three without needing
  three separate `except` clauses.
- `create_booking()` checks car existence first (nothing else can be
  checked about a car that isn't in the dictionary), then the date
  range (`end <= start` is invalid regardless of availability), then
  availability - only after both of those pass does it calculate
  `days = (end - start).days` and `total_fee = days * car["daily_rate"]`.
- `main.py` parses the typed dates with
  `datetime.strptime(text, "%Y-%m-%d")`. A badly formatted date raises
  `ValueError`, caught separately from `RentalError`, with its own
  message.
- Because `booking.py` never prints or reads input, it can be reused
  anywhere (a web form, a test suite - see Part E) without dragging a
  console interface along with it.

## Running the Program

```bash
python main.py
```

Type a car ID from `C001`, `C002`, `C003`, then a start and end date as
`YYYY-MM-DD`, or type `quit` as the car ID to stop.

### Sample Session

```
Car Rental Booking - available cars: C001, C002, C003
Type 'quit' as the car ID to stop.

Car ID: C999
Start date (YYYY-MM-DD): 2026-01-01
End date (YYYY-MM-DD): 2026-01-05
Booking failed: No car found with ID 'C999'.

Car ID: C001
Start date (YYYY-MM-DD): 2026-01-05
End date (YYYY-MM-DD): 2026-01-01
Booking failed: End date (2026-01-01) must be after start date (2026-01-05).

Car ID: C002
Start date (YYYY-MM-DD): 2026-01-01
End date (YYYY-MM-DD): 2026-01-05
Booking failed: Civic is not available for booking.

Car ID: C001
Start date (YYYY-MM-DD): 2026-01-01
End date (YYYY-MM-DD): 2026-01-05
Booking confirmed for C001: 4 day(s), total fee $180.00

Car ID: C003
Start date (YYYY-MM-DD): 2026-01-01
End date (YYYY-MM-DD): bad-date
Booking failed: dates must be in YYYY-MM-DD format.

Car ID: quit
```

## Files

| File | Description |
|---|---|
| `booking.py` | `RentalError` and its three subclasses, plus `create_booking()` - no print/input |
| `main.py` | The interactive menu loop |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |

`booking.py` is reused (imported, not copy-pasted) by the Part E tests
in `WK10/ACT_10_6/`.
