# ============================================================
# Part E support file: tax.py (same as the Part A version)
# ============================================================
#
# See WK10/ACT_10_8/tax.py for the full explanation. Self-contained
# copy so this folder's tests don't depend on another folder.
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
