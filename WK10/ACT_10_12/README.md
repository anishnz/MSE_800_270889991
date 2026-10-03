# Part E: Mocking

## Problem Statement

1. Write a test for `total_with_tax(100, 2)` that fakes a tax rate of
   10% and checks the result. Do it twice: with `unittest.mock.patch`
   and with `monkeypatch`.
2. Write a second test proving that if `get_tax_rate` raises
   `RuntimeError`, the error is not hidden.
3. Run the original, unpatched `total_with_tax(60, 3)` and note the
   error. Why would this be a bad unit test?

## Requirements

1. `tax.py` - `get_tax_rate()` (deliberately unimplemented, standing in
   for a real external call) and `total_with_tax(price, quantity)`.
2. Two tests faking a 10% rate for `total_with_tax(100, 2)`: one with
   `unittest.mock.patch`, one with pytest's `monkeypatch`.
3. A test proving `get_tax_rate` raising `RuntimeError` is not
   swallowed by `total_with_tax`.
4. The real, unpatched call noted and explained.

## How It Works

- `get_tax_rate()` is intentionally left unimplemented - it always
  raises `NotImplementedError`. This stands in for a real call to an
  external tax service that a test must never actually make.
- `with patch("tax.get_tax_rate", return_value=0.10):` temporarily
  replaces the `get_tax_rate` name inside the `tax` module with a fake
  that always returns `0.10`, only for the duration of the `with`
  block - the real function is back immediately afterwards.
- `monkeypatch.setattr(tax, "get_tax_rate", lambda: 0.10)` does the
  same job a different way: it replaces the attribute directly on the
  `tax` module object, and pytest automatically restores the original
  once the test finishes - no `with` block needed.
- Both produce the same result: `total_with_tax(100, 2)` with a 10%
  rate = `100 * 2 * 1.10 = 220.0`.
- Faking `get_tax_rate` to **raise** `RuntimeError` instead of
  returning a number (`side_effect=RuntimeError(...)`), then wrapping
  the call in `pytest.raises(RuntimeError)`, proves `total_with_tax`
  has no `try`/`except` around its call to `get_tax_rate` - the error
  passes straight through, unhidden.
- Calling the real, **unpatched** `total_with_tax(60, 3)` always raises
  `NotImplementedError`, because the real `get_tax_rate()` is left
  unimplemented. See `QUESTION_AND_ANSWER.txt` for why depending on
  this in a genuine unit test (rather than deliberately testing for
  it, as this folder does) would be bad practice.

## Running the Program

```bash
python -m pytest -v
```

### Expected Output

```
test_tax.py::test_total_with_tax_fakes_rate_with_mock_patch PASSED
test_tax.py::test_total_with_tax_fakes_rate_with_monkeypatch PASSED
test_tax.py::test_total_with_tax_does_not_hide_a_get_tax_rate_error PASSED
test_tax.py::test_unpatched_total_with_tax_raises_not_implemented_error PASSED

============================== 4 passed in 0.0Xs ==============================
```

### The Real, Unpatched Call (Part E.3)

```bash
python -c "from tax import total_with_tax; total_with_tax(60, 3)"
```

```
Traceback (most recent call last):
  ...
  File "tax.py", line 23, in total_with_tax
    rate = get_tax_rate()
  File "tax.py", line 14, in get_tax_rate
    raise NotImplementedError(
NotImplementedError: get_tax_rate() represents an external service call and must be mocked in tests, not called for real.
```

## Files

| File | Description |
|---|---|
| `tax.py` | `get_tax_rate()` (unimplemented) and `total_with_tax()` |
| `test_tax.py` | Four tests: two fake a 10% rate (mock.patch / monkeypatch), one proves errors propagate, one runs the real unpatched call |
| `QUESTION_AND_ANSWER.txt` | The original exercise question and a written answer/explanation |
| `README.md` | This file |
