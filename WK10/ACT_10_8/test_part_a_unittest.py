# ============================================================
# Part A: Choose the Right Assertion - unittest column
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   Six situations, each needing a DIFFERENT kind of assertion because
#   each is really asking a different question:
#     1. "is this exact value?"            -> assertEqual
#     2. "is this close enough?" (floats)   -> assertAlmostEqual
#     3. "is this specifically None?"       -> assertIsNone
#     4. "does this text contain that?"     -> assertIn
#     5. "does this raise an error?"        -> assertRaises
#     6. "are these the SAME object?"       -> assertIs
#   Using assertEqual for #2 would be fragile (0.1 + 0.2 is actually
#   0.30000000000000004 in floating point), and using assertEqual for
#   #6 would only check that the two objects look equal, not that they
#   are literally the same object in memory - which is why each
#   situation needs its own, specific assertion.
# ============================================================

import unittest

from shop import Inventory, Product, calculate_price


class TestPartAAssertions(unittest.TestCase):
    def test_1_exact_value(self):
        # result must be exactly 180
        self.assertEqual(calculate_price(60, 3), 180)

    def test_2_nearly_equal_float(self):
        # 0.1 + 0.2 must be (nearly) 0.3
        self.assertAlmostEqual(0.1 + 0.2, 0.3)

    def test_3_is_none(self):
        # inventory.cheapest_in_stock() must be None
        inventory = Inventory()  # empty - nothing in stock at all
        self.assertIsNone(inventory.cheapest_in_stock())

    def test_4_substring_in_message(self):
        # "Keyboard" must appear in message
        inventory = Inventory()
        inventory.add_product("Keyboard", 60.0, 3)
        with self.assertRaises(ValueError) as context:
            inventory.sell("Keyboard", 10)  # only 3 in stock
        self.assertIn("Keyboard", str(context.exception))

    def test_5_raises_value_error(self):
        # calculate_price(60, 0) must raise ValueError
        with self.assertRaises(ValueError):
            calculate_price(60, 0)

    def test_6_same_object(self):
        # car1 and car2 must be the same object
        car1 = Product("Car", 20000.0, 1)
        car2 = car1  # same reference, not a copy
        self.assertIs(car1, car2)


if __name__ == "__main__":
    unittest.main()
