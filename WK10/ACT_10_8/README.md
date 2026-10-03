# Part A: Choose the Right Assertion

## Problem Statement

Use the files from Section 2 (`shop.py` and `tax.py`). For each
situation, write the `unittest` assertion and the `pytest` equivalent.

| # | Situation |
|---|---|
| 1 | result must be exactly 180 |
| 2 | 0.1 + 0.2 must be (nearly) 0.3 |
| 3 | `inventory.cheapest_in_stock()` must be `None` |
| 4 | `"Keyboard"` must appear in message |
| 5 | `calculate_price(60, 0)` must raise `ValueError` |
| 6 | `car1` and `car2` must be the same object |

## Requirements

1. `shop.py` - `calculate_price()`, `Product`, `Inventory` (the shared
   file this whole exercise set builds on).
2. `tax.py` - `get_tax_rate()`, `total_with_tax()` (used from Part E
   onwards).
3. One assertion per situation, written and actually run in both
   `unittest` (`test_part_a_unittest.py`) and `pytest`
   (`test_part_a_pytest.py`).

## The Assertion Table

| # | Situation | `unittest` | `pytest` |
|---|---|---|---|
| 1 | exact value | `self.assertEqual(calculate_price(60, 3), 180)` | `assert calculate_price(60, 3) == 180` |
| 2 | nearly-equal float | `self.assertAlmostEqual(0.1 + 0.2, 0.3)` | `assert 0.1 + 0.2 == pytest.approx(0.3)` |
| 3 | is `None` | `self.assertIsNone(inventory.cheapest_in_stock())` | `assert inventory.cheapest_in_stock() is None` |
| 4 | substring in message | `self.assertIn("Keyboard", str(context.exception))` | `assert "Keyboard" in str(excinfo.value)` |
| 5 | raises `ValueError` | `with self.assertRaises(ValueError): calculate_price(60, 0)` | `with pytest.raises(ValueError): calculate_price(60, 0)` |
| 6 | same object | `self.assertIs(car1, car2)` | `assert car1 is car2` |

## How It Works

- **#1 and #6 look similar but are not interchangeable.** `assertEqual`
  (and plain `==`) compares VALUE; `assertIs` (and plain `is`) compares
  IDENTITY - whether two names point at the exact same object in
  memory. Two equal-looking `Product` instances would pass `==` (if
  `Product` defined it) but fail `is` unless they are literally the
  same object, like `car2 = car1`.
- **#2 needs a tolerance, not exact equality**, because `0.1 + 0.2`
  is actually `0.30000000000000004` in binary floating point - never
  exactly `0.3`. `assertAlmostEqual` and `pytest.approx` both compare
  "close enough" instead of bit-for-bit identical.
- **#3 specifically checks for `None`**, not just "falsy" - an empty
  list or `0` would also be "falsy" but are not `None`. `assertIsNone`
  / `is None` is precise about which falsy value is expected.
- **#4 is a two-step check**: first capture the raised exception
  (`assertRaises`/`pytest.raises` as a context manager, `as context` /
  `as excinfo`), then check its message text with `assertIn` / `in`.
- **#5** is the same "did it raise?" idea as #4, but without needing to
  inspect the message - just whether `ValueError` happened at all.
- `unittest`'s assertions are **methods on `self`** (the `TestCase`
  instance), one per kind of check. `pytest` has **no such methods** -
  everything is a plain `assert`, and pytest's own import hook rewrites
  `assert` at test-collection time so a failure prints both sides of the
  comparison automatically. The two exceptions pytest *does* provide
  helpers for are floating-point tolerance (`pytest.approx`) and
  "expected to raise" (`pytest.raises`), because plain `assert` cannot
  express either of those on its own.

## Running the Program

```bash
python -m unittest -v test_part_a_unittest
python -m pytest -v test_part_a_pytest.py
```

### Expected Output

```
test_1_exact_value ... ok
test_2_nearly_equal_float ... ok
test_3_is_none ... ok
test_4_substring_in_message ... ok
test_5_raises_value_error ... ok
test_6_same_object ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.00Xs

OK
```

```
test_part_a_pytest.py::test_1_exact_value PASSED
test_part_a_pytest.py::test_2_nearly_equal_float PASSED
test_part_a_pytest.py::test_3_is_none PASSED
test_part_a_pytest.py::test_4_substring_in_message PASSED
test_part_a_pytest.py::test_5_raises_value_error PASSED
test_part_a_pytest.py::test_6_same_object PASSED

============================== 6 passed in 0.0Xs ==============================
```

## Files

| File | Description |
|---|---|
| `shop.py` | `calculate_price()`, `Product`, `Inventory` - the shared file used throughout Parts A-D and F |
| `tax.py` | `get_tax_rate()`, `total_with_tax()` - used from Part E onwards |
| `test_part_a_unittest.py` | The six situations as `unittest` assertions |
| `test_part_a_pytest.py` | The same six situations as `pytest` assertions |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
