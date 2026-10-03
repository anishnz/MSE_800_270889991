# ============================================================
# Part F: Challenge - extended booking module
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   This is Part D's booking.py (WK10/ACT_10_5/booking.py) plus one
#   extra rule and one extra exception class:
#     - BookingInPastError (a RentalError) is raised when `start` is
#       earlier than today's date - a car cannot be booked to start
#       yesterday.
#     - That check runs FIRST, before the date-range check, because
#       "is this date usable at all" (not in the past) matters before
#       "is the range the right way round".
#   Everything else (CarNotFoundError, InvalidDateRangeError,
#   CarUnavailableError, the fee calculation) is unchanged from Part D.
#   This module still never calls print() or input().
# ============================================================

from datetime import date


class RentalError(Exception):
    """Base exception for every car rental booking problem."""


class InvalidDateRangeError(RentalError):
    """Raised when the end date is not strictly after the start date."""


class CarNotFoundError(RentalError):
    """Raised when the requested car_id does not exist in `cars`."""


class CarUnavailableError(RentalError):
    """Raised when the requested car exists but is marked unavailable."""


class BookingInPastError(RentalError):
    """Raised when the booking's start date is earlier than today."""


def create_booking(cars, car_id, start, end, today=None):
    """Create a booking for `car_id` from `start` to `end` (datetime.date
    objects).

    `today` defaults to date.today() and exists as a parameter purely so
    tests can pass in a fixed date instead of depending on the real
    clock. Never prints or reads input.
    """
    if today is None:
        today = date.today()

    if car_id not in cars:
        raise CarNotFoundError(f"No car found with ID '{car_id}'.")

    car = cars[car_id]

    if start < today:
        raise BookingInPastError(
            f"Start date ({start}) is in the past; today is {today}."
        )

    if end <= start:
        raise InvalidDateRangeError(
            f"End date ({end}) must be after start date ({start})."
        )

    if not car.get("available", False):
        raise CarUnavailableError(f"{car['model']} is not available for booking.")

    days = (end - start).days
    total_fee = days * car["daily_rate"]

    return {"car_id": car_id, "days": days, "total_fee": total_fee}
