# ============================================================
# Part B: unittest Tests for calculate_price
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   Six test methods, one per bullet point in the exercise. The two
#   "rejected" tests each check SEVERAL bad values using subTest(), so
#   one test method still reports which exact value failed if any of
#   them stop raising - without subTest, the first failure inside a
#   plain loop would stop the whole method and hide whether the OTHER
#   values were also broken.
# ============================================================

import unittest

from shop import calculate_price


class TestCalculatePrice(unittest.TestCase):
    def test_single_item_and_several_items(self):
        self.assertEqual(calculate_price(10, 1), 10)
        self.assertEqual(calculate_price(10, 5), 50)

    def test_discount_applied_correctly(self):
        # 100 * 1 item, 20% off -> 80
        self.assertEqual(calculate_price(100, 1, discount=0.2), 80)

    def test_result_rounded_to_two_decimal_places(self):
        # 3.333 * 3 = 9.999 exactly - must come back as 10.0, not 9.999
        self.assertEqual(calculate_price(3.333, 3), 10.0)

    def test_zero_and_negative_quantities_rejected(self):
        for quantity in (0, -1, -5):
            with self.subTest(quantity=quantity):
                with self.assertRaises(ValueError):
                    calculate_price(10, quantity)

    def test_zero_and_negative_prices_rejected(self):
        for price in (0, -1, -20):
            with self.subTest(price=price):
                with self.assertRaises(ValueError):
                    calculate_price(price, 1)

    def test_full_and_negative_discount_rejected(self):
        for discount in (1.0, -0.1):
            with self.subTest(discount=discount):
                with self.assertRaises(ValueError):
                    calculate_price(10, 1, discount=discount)


if __name__ == "__main__":
    unittest.main()
