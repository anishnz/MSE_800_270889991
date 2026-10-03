# ============================================================
# Part E: Mocking
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. total_with_tax() depends on get_tax_rate(), which in real life
#      would call an external service. A test must not actually call
#      that external service - it needs to CONTROL what get_tax_rate()
#      returns, so the test result depends only on total_with_tax()'s
#      own arithmetic, not on anything outside the test.
#   2. unittest.mock.patch("tax.get_tax_rate", return_value=0.10)
#      temporarily REPLACES the get_tax_rate name inside the tax
#      module with a fake that always returns 0.10, for the duration of
#      the `with` block only - afterwards the real function is back.
#   3. pytest's monkeypatch fixture does the same job a different way:
#      monkeypatch.setattr(tax, "get_tax_rate", lambda: 0.10) replaces
#      the attribute directly, and pytest automatically restores the
#      original after the test finishes - no `with` block needed.
#   4. Replacing get_tax_rate() with something that RAISES (instead of
#      returning a number) proves total_with_tax() does not catch or
#      hide that error anywhere - it should still reach the caller.
#   5. Calling the REAL, unpatched total_with_tax() shows exactly why
#      that would be a bad unit test: it always raises
#      NotImplementedError here, because the real get_tax_rate() is
#      left unimplemented (standing in for "this would call a live
#      external service").
# ============================================================

from unittest.mock import patch

import pytest

import tax
from tax import total_with_tax


def test_total_with_tax_fakes_rate_with_mock_patch():
    with patch("tax.get_tax_rate", return_value=0.10):
        assert total_with_tax(100, 2) == 220.0  # 100 * 2 * 1.10


def test_total_with_tax_fakes_rate_with_monkeypatch(monkeypatch):
    monkeypatch.setattr(tax, "get_tax_rate", lambda: 0.10)
    assert total_with_tax(100, 2) == 220.0  # 100 * 2 * 1.10


def test_total_with_tax_does_not_hide_a_get_tax_rate_error():
    # If get_tax_rate() itself fails, total_with_tax() must not swallow
    # that failure - it should still reach the caller as a RuntimeError.
    with patch("tax.get_tax_rate", side_effect=RuntimeError("tax service down")):
        with pytest.raises(RuntimeError):
            total_with_tax(100, 2)


def test_unpatched_total_with_tax_raises_not_implemented_error():
    # Part E.3: run the ORIGINAL, unpatched total_with_tax(60, 3) and
    # note the error - get_tax_rate() is genuinely unimplemented here,
    # standing in for a live external call. See QUESTION_AND_ANSWER.txt
    # for why depending on that in a real unit test would be bad.
    with pytest.raises(NotImplementedError):
        total_with_tax(60, 3)
