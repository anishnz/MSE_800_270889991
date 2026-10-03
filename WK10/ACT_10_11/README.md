# Part D: Fixtures

## Problem Statement

1. In `conftest.py` create an `inventory` fixture holding three
   products: Keyboard (60.0, stock 3), Mouse (15.0, stock 5) and
   Monitor (250.0, stock 2).
2. Write four tests that use it: the inventory starts with three
   products in stock; selling out the cheapest product leaves two in
   stock; after selling out the two cheapest products the cheapest in
   stock is the Monitor; when everything is sold out
   `cheapest_in_stock()` returns `None`.
3. Explain in one sentence why each test receives a new inventory.

## Requirements

1. `conftest.py` - an `inventory` fixture (`@pytest.fixture`), building
   the three products above.
2. `test_inventory.py` - four tests, each taking `inventory` as a
   parameter.
3. A one-sentence explanation of fixture freshness per test.

## How It Works

- `conftest.py` is a filename pytest recognises automatically: any
  fixture defined there is available to every test file in the same
  folder, with **no import needed**. `test_inventory.py` never writes
  `from conftest import inventory` - it just names `inventory` as a
  parameter, and pytest finds it.
- The three products, by price: **Mouse $15.00** (cheapest),
  **Keyboard $60.00** (middle), **Monitor $250.00** (priciest). Stock:
  Keyboard 3, Mouse 5, Monitor 2.
- Each test:
  1. `test_inventory_starts_with_three_products_in_stock` -
     `len(inventory.in_stock_products()) == 3` straight away.
  2. `test_selling_out_the_cheapest_leaves_two_in_stock` - sells all 5
     Mice, leaving Keyboard and Monitor (2 products).
  3. `test_after_selling_out_the_two_cheapest_cheapest_is_monitor` -
     sells out Mouse, then Keyboard; `cheapest_in_stock().name == "Monitor"`,
     the only one left.
  4. `test_everything_sold_out_cheapest_in_stock_is_none` - sells out
     all three; `cheapest_in_stock() is None`.
- **Why each test receives a new inventory, in one sentence:** pytest
  fixtures are function-scoped by default, so `conftest.py`'s
  `inventory()` runs fresh for every single test that asks for it -
  meaning one test selling out the Mouse can never leave a depleted
  inventory behind for the next test to accidentally inherit.

## Running the Program

```bash
python -m pytest -v
```

### Expected Output

```
test_inventory.py::test_inventory_starts_with_three_products_in_stock PASSED
test_inventory.py::test_selling_out_the_cheapest_leaves_two_in_stock PASSED
test_inventory.py::test_after_selling_out_the_two_cheapest_cheapest_is_monitor PASSED
test_inventory.py::test_everything_sold_out_cheapest_in_stock_is_none PASSED

============================== 4 passed in 0.0Xs ==============================
```

## Files

| File | Description |
|---|---|
| `shop.py` | Self-contained copy of `calculate_price()`/`Product`/`Inventory` |
| `conftest.py` | The `inventory` fixture - three products, rebuilt fresh per test |
| `test_inventory.py` | Four tests using the fixture |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
