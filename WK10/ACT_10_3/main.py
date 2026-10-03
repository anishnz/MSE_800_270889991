# ============================================================
# Part B: Safe Input
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. read_int() keeps asking in a `while True` loop. It only ever
#      leaves the loop with `return value` once a valid whole number
#      has actually been entered - there is no other way out, so the
#      function can never crash, no matter what the user types.
#   2. int(text) raises ValueError for anything that is not a whole
#      number (e.g. "abc", "3.5", ""). That is caught, a message is
#      printed, and `continue` jumps straight back to asking again.
#   3. Once the text does convert to an int, it is checked against
#      `minimum` and `maximum` (each optional - skipped if None). If it
#      is outside that range, a message is printed and the loop asks
#      again.
#   4. Only a number that both converts AND is in range ever reaches
#      `return value`.
# ============================================================


def read_int(prompt, minimum=None, maximum=None):
    """Keep asking until a valid whole number (optionally within a
    [minimum, maximum] range) is entered. Never raises - always returns
    an int."""
    while True:
        text = input(prompt)

        try:
            value = int(text)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"Please enter a number that is at least {minimum}.")
            continue

        if maximum is not None and value > maximum:
            print(f"Please enter a number that is at most {maximum}.")
            continue

        return value


if __name__ == "__main__":
    # Test sequence from the exercise: "abc", "0", "99", "5", range 1-10.
    #   "abc" -> not a whole number       -> rejected, asks again
    #   "0"   -> whole number, but < 1    -> rejected, asks again
    #   "99"  -> whole number, but > 10   -> rejected, asks again
    #   "5"   -> whole number and in range -> accepted, loop exits
    value = read_int("Enter a whole number from 1 to 10: ", minimum=1, maximum=10)
    print("You entered:", value)
