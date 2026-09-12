# WK6

This folder holds a set of independent, unrelated WK6 exercises/mini-projects.
Each `.py` file below is self-contained (aside from the two Blackjack files
sharing `art.py` for their ASCII-art banner) and can be run on its own.

## Files

| File | Description |
|---|---|
| `art.py` | Defines a single ASCII-art "Blackjack" logo string, imported and printed by the two Blackjack game files below. |
| `black_jack(2).py` | An **unfinished** Blackjack exercise template: it still contains the original numbered "Hint" comments and has empty/missing function bodies, so it does not run/compile as-is. A completed version of the same game is `game.py`. |
| `employeeAccessMIS.py` | A small "Employee Access Management System" demo showing a login-gated decorator (`login_required`) that blocks access to employee functions (view salary, view personal details, download report) unless a `logged_in` flag is `True`. |
| `game.py` | A complete, playable console Blackjack game (player vs. computer), including dealing, hit/stand, scoring (with blackjack/bust handling) and a winner comparison. A pre-existing typo (`return 0y` instead of `return 0`) that broke the script has since been fixed. |
| `pyton.py` | An empty scratch/practice file (no code). |

`__pycache__/` (if present) is a Python build artifact and is not part of the
source - it is not documented or modified here.

## Running Each Script

From inside the `WK6` folder:

```bash
python art.py                 # defines the logo string; prints nothing on its own
python employeeAccessMIS.py   # runs immediately, no input needed
python game.py                # interactive Blackjack game (on a plain Windows console, the win/lose/draw messages contain emoji and may raise UnicodeEncodeError when printed - see note below)
python "black_jack(2).py"     # unfinished template - currently cannot run to completion (see note above)
python pyton.py               # empty file; does nothing
```

## Notes on Known Issues

- `game.py`: `calculate_score()` previously contained a typo, `return 0y`
  instead of `return 0`, which caused a `SyntaxError`. This has been fixed
  (only that single character was changed; no other logic was touched).
  Separately, the win/lose/draw messages returned by `compare()` contain
  emoji characters (e.g. `"Draw \U0001F643"`). These print fine on
  Linux/Mac terminals and on Windows Terminal set to UTF-8, but can raise
  `UnicodeEncodeError` on a plain Windows console using the legacy `cp1252`
  codepage. This has been left as-is (not modified).
- `black_jack(2).py`: this is an intentionally incomplete exercise template
  (`compare()` has no body at all, and `deal_card()`, `calculate_score()`
  and `play_game()` only contain docstrings/hint comments), so it currently
  raises an `IndentationError` when run or compiled. This is unchanged.
