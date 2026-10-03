# ============================================================
# Part A: Choose the Right Assertion - pytest column
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   The same six situations as test_part_a_unittest.py, but pytest has
#   no assertEqual/assertIsNone/assertIn/assertIs family of methods at
#   all - it uses plain `assert`, and its test runner rewrites `assert`
#   so a failure shows exactly what both sides of the comparison were.
#   The one real exception is floating point ("nearly equal"), where
#   pytest.approx(...) is used inside a plain assert, and "does this
#   raise?", where pytest.raises(...) is used as a context manager -
#   those two need a helper because a plain `==` or a bare statement
#   cannot express either idea on their own.
# ============================================================

import pytest

from shop import Inventory, Product, calculate_price


def test_1_exact_value():
    # result must be exactly 180
    assert calculate_price(60, 3) == 180


def test_2_nearly_equal_float():
    # 0.1 + 0.2 must be (nearly) 0.3
    assert 0.1 + 0.2 == pytest.approx(0.3)


def test_3_is_none():
    # inventory.cheapest_in_stock() must be None
    inventory = Inventory()  # empty - nothing in stock at all
    assert inventory.cheapest_in_stock() is None


def test_4_substring_in_message():
    # "Keyboard" must appear in message
    inventory = Inventory()
    inventory.add_product("Keyboard", 60.0, 3)
    with pytest.raises(ValueError) as excinfo:
        inventory.sell("Keyboard", 10)  # only 3 in stock
    assert "Keyboard" in str(excinfo.value)


def test_5_raises_value_error():
    # calculate_price(60, 0) must raise ValueError
    with pytest.raises(ValueError):
        calculate_price(60, 0)


def test_6_same_object():
    # car1 and car2 must be the same object
    car1 = Product("Car", 20000.0, 1)
    car2 = car1  # same reference, not a copy
    assert car1 is car2
