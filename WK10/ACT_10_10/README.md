# Part C: Convert to pytest

## Problem Statement

Install `pytest` and create `test_price_pytest.py`. Rewrite your Part B
tests as plain functions. Use `@pytest.mark.parametrize` for the valid
cases and for the invalid arguments, and `pytest.raises` for the
errors. Run `pytest -v` and compare how many tests are reported with
Part B.

## Requirements

1. `pytest` installed (`pip install pytest`).
2. Part B's six test methods rewritten as plain functions.
3. `@pytest.mark.parametrize` covering the valid-result cases and the
   invalid-argument cases.
4. `pytest.raises` for every case expected to raise `ValueError`.
5. A comparison between the test count `pytest -v` reports and Part B's
   `unittest` count.

## How It Works

- `test_calculate_price_valid` replaces 3 of Part B's methods (single
  item, several items, discount, rounding) with ONE parametrized
  function and 4 rows of `(price, quantity, discount, expected)`.
  pytest runs the function body once per row.
- `test_calculate_price_invalid_raises_value_error` replaces the other
  3 Part B methods (bad quantity, bad price, bad discount) with ONE
  parametrized function and 8 rows of `(price, quantity, discount)`
  that must each raise `ValueError`, checked with `pytest.raises`.
- This is pytest's answer to `subTest()`: instead of looping INSIDE one
  test method (where only failures get individually reported),
  `@pytest.mark.parametrize` turns every row into its own fully
  separate, separately-reported test - visible in `-v` output as
  `test_name[param-values]`.

## The Count Comparison

| | Test methods/functions written | Tests reported by `-v` |
|---|---|---|
| Part B (`unittest`, `subTest`) | 6 | 6 (`Ran 6 tests`) |
| Part C (`pytest`, `parametrize`) | 2 | **12** (4 + 8 parametrized rows) |

Even though Part C has FEWER functions (2 vs 6), it reports MORE
individual test results (12 vs 6), because `parametrize` gives every
row its own identity in the report, while `subTest` only shows
individual results for FAILURES - a fully passing `subTest` loop still
counts as just one test in the total.

## Running the Program

```bash
pip install pytest
python -m pytest -v
```

### Expected Output

```
test_price_pytest.py::test_calculate_price_valid[10-1-0.0-10] PASSED
test_price_pytest.py::test_calculate_price_valid[10-5-0.0-50] PASSED
test_price_pytest.py::test_calculate_price_valid[100-1-0.2-80] PASSED
test_price_pytest.py::test_calculate_price_valid[3.333-3-0.0-10.0] PASSED
test_price_pytest.py::test_calculate_price_invalid_raises_value_error[10-0-0.0] PASSED
test_price_pytest.py::test_calculate_price_invalid_raises_value_error[10--1-0.0] PASSED
test_price_pytest.py::test_calculate_price_invalid_raises_value_error[10--5-0.0] PASSED
test_price_pytest.py::test_calculate_price_invalid_raises_value_error[0-1-0.0] PASSED
test_price_pytest.py::test_calculate_price_invalid_raises_value_error[-1-1-0.0] PASSED
test_price_pytest.py::test_calculate_price_invalid_raises_value_error[-20-1-0.0] PASSED
test_price_pytest.py::test_calculate_price_invalid_raises_value_error[10-1-1.0] PASSED
test_price_pytest.py::test_calculate_price_invalid_raises_value_error[10-1--0.1] PASSED

============================== 12 passed in 0.0Xs ==============================
```

## Files

| File | Description |
|---|---|
| `shop.py` | Self-contained copy of `calculate_price()`/`Product`/`Inventory` |
| `test_price_pytest.py` | Part B's six tests, rewritten as 2 parametrized pytest functions (12 reported cases) |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
