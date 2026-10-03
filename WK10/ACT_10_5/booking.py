# ============================================================
# Part D: Custom Exceptions for Car Rental - the booking module
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. Four exception classes form a small hierarchy:
#          RentalError                 (base - catches "any booking problem")
#          +-- InvalidDateRangeError   (end date not after start date)
#          +-- CarNotFoundError        (car_id is not in the dictionary)
#          +-- CarUnavailableError     (car exists but is not available)
#      Each subclass IS A RentalError (through inheritance), so code
#      that only cares "did the booking fail, in general?" can catch
#      just RentalError and still catch all three specific errors.
#   2. create_booking(cars, car_id, start, end) checks things in an
#      order that matters:
#        a. Is car_id even in `cars`? If not, there is nothing else to
#           check - raise CarNotFoundError immediately.
#        b. Is the date range valid (end strictly after start)? Checked
#           before availability, because a booking with nonsense dates
#           is wrong regardless of whether the car happens to be free.
#        c. Is the car currently available? Only checked once the car
#           is known to exist and the dates make sense.
#        d. Only if all three checks pass does it calculate the number
#           of days and the total fee, and return a booking dictionary.
#   3. This module must NEVER call print() or input() - raising the
#      right exception (or returning the booking dictionary) is its
#      entire job. That is what lets main.py (the menu loop) decide how
#      to talk to the user, and what lets test_booking.py (Part E) test
#      it without anything being printed to the screen during tests.
# ============================================================


class RentalError(Exception):
    """Base exception for every car rental booking problem."""


class InvalidDateRangeError(RentalError):
    """Raised when the end date is not strictly after the start date."""


class CarNotFoundError(RentalError):
    """Raised when the requested car_id does not exist in `cars`."""


class CarUnavailableError(RentalError):
    """Raised when the requested car exists but is marked unavailable."""


def create_booking(cars, car_id, start, end):
    """Create a booking for `car_id` from `start` to `end` (datetime.date
    objects).

    `cars` is a dict mapping car_id -> {"make", "model", "daily_rate",
    "available"}.

    Returns {"car_id", "days", "total_fee"} on success.
    Raises CarNotFoundError, InvalidDateRangeError or CarUnavailableError
    on failure. Never prints or reads input.
    """
    if car_id not in cars:
        raise CarNotFoundError(f"No car found with ID '{car_id}'.")

    car = cars[car_id]

    if end <= start:
        raise InvalidDateRangeError(
            f"End date ({end}) must be after start date ({start})."
        )

    if not car.get("available", False):
        raise CarUnavailableError(f"{car['model']} is not available for booking.")

    days = (end - start).days
    total_fee = days * car["daily_rate"]

    return {"car_id": car_id, "days": days, "total_fee": total_fee}
