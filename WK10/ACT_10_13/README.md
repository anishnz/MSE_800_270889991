# Part F: Test-Driven Challenge

## Problem Statement

A new business rule: shipping costs $5.00 for the first kilogram plus
$2.50 for every additional kilogram (part of a kilogram is rounded
up), and is capped at $25.00.

1. Write the tests first for a function `shipping_cost(weight_kg)`.
   Include the flat rate (1 kg or less), rounding up (for example 2.1
   kg), the cap, and invalid weights. Run them and check that they
   fail.
2. Implement `shipping_cost` in `shop.py` until all tests pass.
3. Run coverage on `shop.py`. Is any line missed? If so, write the
   missing test.

## Requirements

1. `test_shipping.py` written and run **before** `shipping_cost`
   exists in `shop.py`, and confirmed to fail.
2. `shipping_cost(weight_kg)` implemented until all of those tests
   pass.
3. `coverage` run against `shop.py`; any missed lines covered by an
   additional test.

## How It Works (TDD: Red, Green, Covered)

### 1. Red - write the tests, watch them fail

`test_shipping.py` was written against a `shop.py` that had no
`shipping_cost` function at all. Running `python -m pytest -v`
immediately failed at collection:

```
ImportError: cannot import name 'shipping_cost' from 'shop'
```

This is the expected TDD "red" step - the tests describe behaviour
that does not exist yet.

### 2. Green - implement until they pass

```python
def shipping_cost(weight_kg):
    if weight_kg <= 0:
        raise ValueError(f"Weight must be positive, got {weight_kg}.")
    if weight_kg <= 1:
        cost = 5.00
    else:
        extra_kg = math.ceil(weight_kg - 1)
        cost = 5.00 + extra_kg * 2.50
    return min(cost, 25.00)
```

- `weight_kg <= 1` → the flat `$5.00` (covers "1 kg or less").
- Otherwise, `math.ceil(weight_kg - 1)` rounds the weight **above** the
  first kilogram **up** to a whole number of extra kilograms (2.1 kg →
  1.1 kg extra → rounds up to 2), each costing `$2.50`.
- `min(cost, 25.00)` applies the cap - without it, a 15 kg parcel would
  cost `5.00 + 14 * 2.50 = 40.00`; with it, exactly `$25.00`.
- `weight_kg <= 0` is rejected as an invalid weight.

All 6 tests passed once this was in place.

### 3. Covered - run coverage, fill any gap

```
Name      Stmts   Miss  Cover   Missing
---------------------------------------
shop.py      42     24    43%   18-26, 31-33, 38, 41, 44-53, 56, 59-62
```

Every missing line belonged to `calculate_price()`, `Product` and
`Inventory` - `shipping_cost()` itself was already at 100%, because
`test_shipping.py` exercises its flat-rate branch, its rounding-up
branch, its cap, and its invalid-weight check. The gap existed simply
because this folder's test file never calls those older functions at
all.

`test_shop_smoke.py` was added with enough calls to exercise every
remaining line - a valid `calculate_price()` call plus its three
validation errors, and an `Inventory` flow that adds a product, fails
to sell an unknown product, fails to oversell, sells out successfully,
and then confirms `cheapest_in_stock()` returns `None`. Coverage on the
whole file reached:

```
Name      Stmts   Miss  Cover   Missing
---------------------------------------
shop.py      42      0   100%
```

## Running the Program

```bash
python -m pytest -v
python -m coverage run -m pytest -q
python -m coverage report -m shop.py
```

### Expected Output

```
test_shipping.py::test_flat_rate_up_to_one_kilogram PASSED
test_shipping.py::test_rounds_up_a_partial_extra_kilogram PASSED
test_shipping.py::test_capped_at_twenty_five PASSED
test_shipping.py::test_invalid_weight_raises_value_error[0] PASSED
test_shipping.py::test_invalid_weight_raises_value_error[-1] PASSED
test_shipping.py::test_invalid_weight_raises_value_error[-5] PASSED
test_shop_smoke.py::test_calculate_price_smoke PASSED
test_shop_smoke.py::test_inventory_smoke PASSED

============================== 8 passed in 0.0Xs ==============================
```

```
Name      Stmts   Miss  Cover   Missing
---------------------------------------
shop.py      42      0   100%
---------------------------------------
TOTAL        42      0   100%
```

## Files

| File | Description |
|---|---|
| `shop.py` | `calculate_price()`/`Product`/`Inventory` plus the new `shipping_cost()`, built test-first |
| `test_shipping.py` | The 6 tests written before `shipping_cost` existed, confirmed to fail, then to pass |
| `test_shop_smoke.py` | Added after the coverage run, to close the gap on `calculate_price()`/`Inventory` |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
