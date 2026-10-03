# Part B: unittest Tests

## Problem Statement

Create `test_price_unittest.py` with a `TestCase` class for
`calculate_price` containing at least six tests:

- a single item and several items;
- a discount is applied correctly;
- the result is rounded to two decimal places;
- zero and negative quantities are rejected (use `subTest`);
- zero and negative prices are rejected (use `subTest`);
- a discount of 100% (1.0) and a negative discount are rejected.

Run with `python -m unittest -v test_price_unittest` and make sure
every test passes. Then temporarily break `calculate_price` (for
example change the discount formula) and confirm that your tests
notice.

## Requirements

1. Six (or more) test methods in one `TestCase` class, covering each
   bullet point above.
2. `subTest` used for the two "rejected" tests, since each checks
   several bad values.
3. All six pass against the real `calculate_price`.
4. A deliberately broken `calculate_price` makes the relevant tests
   fail.

## How It Works

- `test_single_item_and_several_items` checks `calculate_price(10, 1)`
  and `calculate_price(10, 5)` - one quantity of 1, one above 1.
- `test_discount_applied_correctly` checks
  `calculate_price(100, 1, discount=0.2) == 80`.
- `test_result_rounded_to_two_decimal_places` uses
  `calculate_price(3.333, 3)`, which is `9.999` before rounding -
  asserting the result is `10.0` proves `round(..., 2)` is actually
  being applied, not just that the formula is right.
- `test_zero_and_negative_quantities_rejected` and
  `test_zero_and_negative_prices_rejected` each loop over three bad
  values (`0, -1, -5` / `0, -1, -20`) inside
  `with self.subTest(...):`. Without `subTest`, the first failing
  value in a plain loop would stop the whole test method immediately,
  hiding whether the OTHER values were also broken; `subTest` lets
  every value be checked and reported independently within one test
  method.
- `test_full_and_negative_discount_rejected` does the same for
  `discount=1.0` (100% off - rejected, since the valid range excludes
  1.0) and `discount=-0.1` (negative - also rejected).

### Confirming the Tests Actually Notice a Bug

`shop.py`'s `calculate_price` was temporarily changed from:

```python
total = price * quantity * (1 - discount)
```

to a deliberately wrong:

```python
total = price * quantity * (1 - discount) + 1  # BUG for demonstration
```

Running the suite again immediately failed 3 of the 6 tests
(`test_single_item_and_several_items`, `test_discount_applied_correctly`,
`test_result_rounded_to_two_decimal_places` - the three that check
exact numeric results), each showing the actual (wrong, +1) value
versus the expected one. The other 3 tests (the "rejected" ones) still
passed, because the bug only affects the successful calculation, not
the input validation. The bug was then reverted and the full suite
passed again.

## Running the Program

```bash
python -m unittest -v test_price_unittest
```

### Expected Output

```
test_discount_applied_correctly ... ok
test_full_and_negative_discount_rejected ... ok
test_result_rounded_to_two_decimal_places ... ok
test_single_item_and_several_items ... ok
test_zero_and_negative_prices_rejected ... ok
test_zero_and_negative_quantities_rejected ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.00Xs

OK
```

## Files

| File | Description |
|---|---|
| `shop.py` | Self-contained copy of `calculate_price()`/`Product`/`Inventory` |
| `test_price_unittest.py` | Six `unittest` tests, two of them using `subTest` |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
