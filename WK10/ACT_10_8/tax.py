# ============================================================
# Part A support file: tax.py (the other "Section 2" file)
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. get_tax_rate() is meant to represent a call to some external tax
#      service (a government API, a config server, etc). It is left
#      UNIMPLEMENTED here, on purpose: a function like this should
#      always be mocked/patched in a test, never called for real, so
#      tests stay fast, offline and repeatable. Calling it for real
#      raises NotImplementedError to make that point obvious the moment
#      someone forgets to mock it (see Part E).
#   2. total_with_tax(price, quantity) asks get_tax_rate() for the
#      current rate and returns price * quantity * (1 + rate), rounded
#      to 2 decimals. It does NOT catch anything get_tax_rate() raises
#      - whatever happens there is passed straight through to the
#      caller, unchanged.
# ============================================================


def get_tax_rate():
    """Stand-in for a real call to an external tax-rate service.
    Intentionally unimplemented - tests must patch this function rather
    than depend on a live external call."""
    raise NotImplementedError(
        "get_tax_rate() represents an external service call and must be "
        "mocked in tests, not called for real."
    )


def total_with_tax(price, quantity):
    """Return price * quantity including the current tax rate, rounded
    to 2 decimals. Any exception from get_tax_rate() propagates as-is."""
    rate = get_tax_rate()
    return round(price * quantity * (1 + rate), 2)
