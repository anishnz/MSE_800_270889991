# ============================================================
# Part C: Convert Part B to pytest
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   The same behaviour as Part B's TestCalculatePrice, but as plain
#   functions:
#     - The three "it calculates correctly" checks become ONE function,
#       parametrized over 4 (price, quantity, discount, expected)
#       cases via @pytest.mark.parametrize. pytest runs the function
#       body once per row and reports each row as its own test result.
#     - The three "it rejects bad input" checks become ONE function,
#       parametrized over 8 (price, quantity, discount) rows that must
#       each raise ValueError, checked with pytest.raises.
#   This is the pytest idiom that replaces unittest's subTest(): instead
#   of looping inside one test method, parametrize turns each case into
#   its own fully separate, separately-reported test.
# ============================================================

import pytest

from shop import calculate_price


@pytest.mark.parametrize(
    "price, quantity, discount, expected",
    [
        (10, 1, 0.0, 10),       # a single item
        (10, 5, 0.0, 50),       # several items
        (100, 1, 0.2, 80),      # a discount applied correctly
        (3.333, 3, 0.0, 10.0),  # 9.999 rounded to 2 decimals -> 10.0
    ],
)
def test_calculate_price_valid(price, quantity, discount, expected):
    assert calculate_price(price, quantity, discount) == expected


@pytest.mark.parametrize(
    "price, quantity, discount",
    [
        (10, 0, 0.0),    # zero quantity
        (10, -1, 0.0),   # negative quantity
        (10, -5, 0.0),   # negative quantity
        (0, 1, 0.0),     # zero price
        (-1, 1, 0.0),    # negative price
        (-20, 1, 0.0),   # negative price
        (10, 1, 1.0),    # 100% discount
        (10, 1, -0.1),   # negative discount
    ],
)
def test_calculate_price_invalid_raises_value_error(price, quantity, discount):
    with pytest.raises(ValueError):
        calculate_price(price, quantity, discount)
