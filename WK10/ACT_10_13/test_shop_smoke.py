# ============================================================
# Part F: Coverage follow-up - the lines coverage found missing
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   `coverage report -m shop.py` after running test_shipping.py alone
#   showed shipping_cost() itself at 100% (every line and every branch
#   - flat rate, rounding up, the cap, invalid weight - is exercised by
#   test_shipping.py). The missing lines it reported all belonged to
#   calculate_price(), Product and Inventory - code that exists in
#   shop.py but that THIS folder's test file never calls at all, since
#   test_shipping.py only imports shipping_cost.
#
#   This file is the "write the missing test" step: enough smoke tests
#   for calculate_price() and Inventory to exercise every remaining
#   line in shop.py, so coverage on the whole file reaches 100% inside
#   this folder too.
# ============================================================

import pytest

from shop import Inventory, calculate_price


def test_calculate_price_smoke():
    assert calculate_price(10, 2) == 20
    with pytest.raises(ValueError):
        calculate_price(-1, 1)
    with pytest.raises(ValueError):
        calculate_price(1, 0)
    with pytest.raises(ValueError):
        calculate_price(1, 1, discount=1.0)


def test_inventory_smoke():
    inventory = Inventory()
    inventory.add_product("Widget", 10.0, 2)

    assert inventory.cheapest_in_stock().name == "Widget"

    with pytest.raises(ValueError):
        inventory.sell("Unknown", 1)  # no such product
    with pytest.raises(ValueError):
        inventory.sell("Widget", 5)  # more than the 2 in stock

    inventory.sell("Widget", 2)  # sell out the only product
    assert inventory.cheapest_in_stock() is None
