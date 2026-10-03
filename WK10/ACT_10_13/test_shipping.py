# ============================================================
# Part F: Test-Driven Challenge - tests written BEFORE shipping_cost()
# exists
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   The business rule: shipping costs $5.00 for the first kilogram,
#   plus $2.50 for every additional kilogram (any part of a kilogram
#   rounds UP), capped at $25.00 total. These tests describe that rule
#   in code BEFORE shop.py has a shipping_cost() function at all - this
#   is Test-Driven Development: write the test, watch it fail, then
#   write just enough code to make it pass.
#
#   1. test_flat_rate_up_to_one_kilogram - weight at or under 1 kg
#      always costs exactly the flat $5.00.
#   2. test_rounds_up_a_partial_extra_kilogram - 2.1 kg is "1 kg flat +
#      1.1 kg extra"; 1.1 kg rounds UP to 2 whole extra kilograms, so
#      cost = 5.00 + 2 * 2.50 = 10.00.
#   3. test_capped_at_twenty_five - a heavy parcel (15 kg) would
#      otherwise cost far more than $25.00 by the formula alone, but
#      the cap brings it back down to exactly $25.00.
#   4. test_invalid_weight_raises_value_error - zero or negative
#      weight makes no physical sense and must be rejected.
# ============================================================

import pytest

from shop import shipping_cost


def test_flat_rate_up_to_one_kilogram():
    assert shipping_cost(1) == 5.00
    assert shipping_cost(0.4) == 5.00


def test_rounds_up_a_partial_extra_kilogram():
    # 2.1 kg = 1 kg flat + 1.1 kg extra, rounded UP to 2 extra kg.
    assert shipping_cost(2.1) == 10.00  # 5.00 + 2 * 2.50


def test_capped_at_twenty_five():
    # Without the cap, 15 kg would be 5.00 + 14 * 2.50 = 40.00.
    assert shipping_cost(15) == 25.00


@pytest.mark.parametrize("weight_kg", [0, -1, -5])
def test_invalid_weight_raises_value_error(weight_kg):
    with pytest.raises(ValueError):
        shipping_cost(weight_kg)
