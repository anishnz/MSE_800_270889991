# ============================================================
# Part D: Fixtures - conftest.py
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. conftest.py is a special, magic filename: pytest automatically
#      finds it and makes every fixture defined in it available to
#      every test file in the same folder (and subfolders), with no
#      import needed.
#   2. @pytest.fixture marks inventory() as a fixture. Any test
#      function that lists `inventory` as a parameter gets whatever
#      this function returns.
#   3. By default a fixture is FUNCTION-scoped: pytest calls
#      inventory() again, from scratch, for every single test that
#      asks for it. That is what guarantees test_inventory.py's four
#      tests can never see each other's sold stock - each one starts
#      from the same clean three products.
# ============================================================

import pytest

from shop import Inventory


@pytest.fixture
def inventory():
    """A fresh Inventory with three products, rebuilt for every test
    that uses it."""
    store = Inventory()
    store.add_product("Keyboard", 60.0, 3)
    store.add_product("Mouse", 15.0, 5)
    store.add_product("Monitor", 250.0, 2)
    return store
