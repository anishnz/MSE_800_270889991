# ============================================================
# Part F: Challenge - logging failed bookings
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. logging.basicConfig() is set up once, at import time, so every
#      logging.error(...) call anywhere in this file writes a line to
#      errors.log instead of (or as well as) appearing on screen. The
#      format string includes %(asctime)s, which is the timestamp.
#   2. Each failing booking attempt is still shown to the user with
#      print() (same as Part D), but it is ALSO written to errors.log
#      inside the same except block, with logging.error(...). That
#      gives a permanent, timestamped record of every failure, even
#      ones the user never mentions later.
#   3. Why `except: pass` would be dangerous in the booking SAVE routine
#      (the part that actually writes a confirmed booking to disk or a
#      database), in two sentences:
#        `except: pass` silently swallows every error - including ones
#        that have nothing to do with the booking itself, such as the
#        disk being full or the database connection dropping - so a
#        booking the customer was charged for can simply vanish with no
#        record that saving it ever failed. Because nothing is logged
#        or re-raised, there is no way to notice the problem, show the
#        customer an honest error, or investigate later: the failure is
#        not handled, it is just hidden.
# ============================================================

import logging
from datetime import datetime

from booking import BookingInPastError, RentalError, create_booking

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
)

CARS = {
    "C001": {"make": "Toyota", "model": "Corolla", "daily_rate": 45.0, "available": True},
    "C002": {"make": "Honda", "model": "Civic", "daily_rate": 50.0, "available": False},
    "C003": {"make": "Mazda", "model": "CX-5", "daily_rate": 70.0, "available": True},
}


def parse_date(text):
    return datetime.strptime(text.strip(), "%Y-%m-%d").date()


def main():
    print("Car Rental Booking - available cars:", ", ".join(CARS))
    print("Type 'quit' as the car ID to stop.\n")

    while True:
        car_id = input("Car ID: ").strip()
        if car_id.lower() == "quit":
            break

        start_text = input("Start date (YYYY-MM-DD): ")
        end_text = input("End date (YYYY-MM-DD): ")

        try:
            start = parse_date(start_text)
            end = parse_date(end_text)
            booking = create_booking(CARS, car_id, start, end)
        except RentalError as error:
            # Permanent, timestamped record in errors.log, in addition
            # to the friendly message shown to the user right now.
            logging.error(
                "Booking failed for car %s (%s to %s): %s",
                car_id, start_text, end_text, error,
            )
            print(f"Booking failed: {error}\n")
        except ValueError:
            logging.error(
                "Booking failed for car %s: invalid date format (%s, %s)",
                car_id, start_text, end_text,
            )
            print("Booking failed: dates must be in YYYY-MM-DD format.\n")
        else:
            print(
                f"Booking confirmed for {car_id}: {booking['days']} day(s), "
                f"total fee ${booking['total_fee']:.2f}\n"
            )


if __name__ == "__main__":
    main()
