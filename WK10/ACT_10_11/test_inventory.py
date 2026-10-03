# ============================================================
# Part D: Fixtures - tests using the inventory fixture
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   Each test takes `inventory` as a parameter. pytest sees that name,
#   finds the `inventory` fixture in conftest.py, runs it, and passes
#   its return value in - automatically, with no import and no manual
#   setup/teardown code in this file at all.
#
#   Prices: Mouse $15.00 (cheapest), Keyboard $60.00 (middle),
#   Monitor $250.00 (priciest). stock: Keyboard 3, Mouse 5, Monitor 2.
# ============================================================


def test_inventory_starts_with_three_products_in_stock(inventory):
    assert len(inventory.in_stock_products()) == 3


def test_selling_out_the_cheapest_leaves_two_in_stock(inventory):
    inventory.sell("Mouse", 5)  # Mouse ($15.00) is the cheapest product
    assert len(inventory.in_stock_products()) == 2


def test_after_selling_out_the_two_cheapest_cheapest_is_monitor(inventory):
    inventory.sell("Mouse", 5)      # 1st cheapest, $15.00
    inventory.sell("Keyboard", 3)   # 2nd cheapest, $60.00
    cheapest = inventory.cheapest_in_stock()
    assert cheapest.name == "Monitor"


def test_everything_sold_out_cheapest_in_stock_is_none(inventory):
    inventory.sell("Mouse", 5)
    inventory.sell("Keyboard", 3)
    inventory.sell("Monitor", 2)
    assert inventory.cheapest_in_stock() is None


# ------------------------------------------------------------
# Why does each test above receive a NEW inventory?
# ------------------------------------------------------------
# Because pytest fixtures are FUNCTION-scoped by default, so
# conftest.py's inventory() function runs fresh for every single test
# that asks for it - one test selling out the Mouse can never leave a
# depleted inventory behind for the next test to accidentally inherit.
