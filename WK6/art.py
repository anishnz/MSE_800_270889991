"""Blackjack ASCII art logo.

This module has no logic of its own - it only defines a single string
constant, `logo`, that holds an ASCII-art picture of a playing card next
to the word "Blackjack". It exists purely so the other Blackjack scripts
in this folder (`game.py` and `black_jack(2).py`) can do:

    from art import logo

and then `print(logo)` to show a banner when the game starts, instead of
cluttering the game files themselves with a large block of art text.
"""

# `r"""..."""` is a RAW triple-quoted string:
#   - triple quotes (""" ... """) let the string span multiple lines
#     exactly as typed, including the newlines between each row of art.
#   - the leading "r" makes it a "raw" string, so backslash characters
#     inside it (see the backticks/underscores below) are treated as
#     literal characters instead of Python escape sequences. This matters
#     here because the art below contains backslashes ( \ ) that are part
#     of the picture, not escape codes like \n or \t.
# The whole multi-line string is assigned to the module-level variable
# `logo`, which other files import and print as-is.
logo = r"""
.------.            _    _            _     _            _
|A_  _ |.          | |  | |          | |   (_)          | |
|( \/ ).-----.      | |__| | __ _  ___| | ___ _  __ _  ___| | __
| \  /|K Q J |      |  __  |/ _` |/ __| |/ / | |/ _` |/ __| |/ /
|  \/ | -/.  |      | |  | | (_| | (__|   <| | (_| | (__|   <
`-----'`----'       |_|  |_|\__,_|\___|_|\_\_|\__,_|\___|_|\_\
"""
