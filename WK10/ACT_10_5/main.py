# ============================================================
# Part D: Custom Exceptions for Car Rental - the menu loop
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. CARS is a small dictionary of sample cars (some available, some
#      not) that create_booking() in booking.py will check against.
#   2. The loop asks for a car ID and two dates as plain text, converts
#      the dates with datetime.strptime(), and calls create_booking().
#   3. create_booking() never prints anything itself - it only raises
#      one of the RentalError subclasses, or returns a booking
#      dictionary. ALL of the user-facing messages below belong to this
#      file, not to booking.py.
#   4. `except RentalError as error:` is enough to catch all three
#      specific errors (CarNotFoundError, InvalidDateRangeError,
#      CarUnavailableError), because each of them IS A RentalError. The
#      error message itself (str(error)) already says exactly what went
#      wrong, so one except block covers every booking failure.
#   5. A badly-typed date (e.g. "2026/01/05" instead of "2026-01-05")
#      makes strptime() raise ValueError, which is caught separately
#      with its own message, so a typo in the date never crashes the
#      program.
# ============================================================

from datetime import datetime

from booking import RentalError, create_booking

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
            print(f"Booking failed: {error}\n")
        except ValueError:
            print("Booking failed: dates must be in YYYY-MM-DD format.\n")
        else:
            print(
                f"Booking confirmed for {car_id}: {booking['days']} day(s), "
                f"total fee ${booking['total_fee']:.2f}\n"
            )


if __name__ == "__main__":
    main()
