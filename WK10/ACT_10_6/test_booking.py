# ============================================================
# Part E: Test Your Exceptions
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. This file tests the create_booking() function from Part D
#      (WK10/ACT_10_5/booking.py) - it does not redefine it. The two
#      sys.path lines below add that folder to Python's import search
#      path, so `from booking import ...` finds the real module instead
#      of needing a copy-pasted duplicate here.
#   2. unittest.TestCase gives us self.assertEqual(), self.assertRaises()
#      and self.assertIn() to check results without writing our own
#      if/print checks.
#   3. self.assertRaises(SomeError) is a context manager: the code
#      inside the `with` block is expected to raise SomeError. If it
#      does, the test passes. If it raises a DIFFERENT exception, or no
#      exception at all, the test fails.
#   4. Six tests cover every rule from the exercise:
#        - a valid booking returns the correct total fee;
#        - an unknown car ID raises CarNotFoundError;
#        - an end date before (or equal to) the start date raises
#          InvalidDateRangeError;
#        - an unavailable car raises CarUnavailableError, and the
#          message contains the car's model;
#        - catching RentalError also catches each of the three specific
#          errors (because each one IS A RentalError).
# ============================================================

import os
import sys
import unittest
from datetime import date

# Make Part D's booking.py importable from this separate folder.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "ACT_10_5"))

from booking import (  # noqa: E402  (import must come after the sys.path fix above)
    CarNotFoundError,
    CarUnavailableError,
    InvalidDateRangeError,
    RentalError,
    create_booking,
)


class TestCreateBooking(unittest.TestCase):
    def setUp(self):
        # A fresh, known set of cars for every test, so one test can
        # never leak state into another.
        self.cars = {
            "C001": {"make": "Toyota", "model": "Corolla", "daily_rate": 45.0, "available": True},
            "C002": {"make": "Honda", "model": "Civic", "daily_rate": 50.0, "available": False},
        }

    def test_valid_booking_returns_correct_total_fee(self):
        booking = create_booking(self.cars, "C001", date(2026, 1, 1), date(2026, 1, 5))
        self.assertEqual(booking["days"], 4)
        self.assertEqual(booking["total_fee"], 180.0)  # 4 days * $45/day

    def test_unknown_car_id_raises_car_not_found_error(self):
        with self.assertRaises(CarNotFoundError):
            create_booking(self.cars, "C999", date(2026, 1, 1), date(2026, 1, 5))

    def test_end_date_before_start_raises_invalid_date_range_error(self):
        with self.assertRaises(InvalidDateRangeError):
            create_booking(self.cars, "C001", date(2026, 1, 5), date(2026, 1, 1))

    def test_end_date_equal_to_start_raises_invalid_date_range_error(self):
        # A zero-day booking is not a valid booking either.
        with self.assertRaises(InvalidDateRangeError):
            create_booking(self.cars, "C001", date(2026, 1, 1), date(2026, 1, 1))

    def test_unavailable_car_raises_car_unavailable_error_with_model_in_message(self):
        with self.assertRaises(CarUnavailableError) as context:
            create_booking(self.cars, "C002", date(2026, 1, 1), date(2026, 1, 5))
        self.assertIn("Civic", str(context.exception))

    def test_rental_error_catches_each_specific_subclass(self):
        cases = [
            ("C999", date(2026, 1, 1), date(2026, 1, 5)),  # CarNotFoundError
            ("C001", date(2026, 1, 5), date(2026, 1, 1)),  # InvalidDateRangeError
            ("C002", date(2026, 1, 1), date(2026, 1, 5)),  # CarUnavailableError
        ]
        for car_id, start, end in cases:
            with self.assertRaises(RentalError):
                create_booking(self.cars, car_id, start, end)


if __name__ == "__main__":
    unittest.main()
