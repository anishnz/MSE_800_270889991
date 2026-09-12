"""
Week 5 - Activity 5.1: Filter elements by even index (placeholder file).

DEFINITION: enumerate()
------------------------
enumerate(iterable) yields (index, value) pairs while looping, so you can
know an item's position without maintaining a separate counter variable.

DEFINITION: List Comprehension with enumerate()
-------------------------------------------------
Combining the two lets you filter a list based on each element's index,
e.g. keeping only elements found at an even index (0, 2, 4, ...):

    [value for index, value in enumerate(data) if index % 2 == 0]

Status of this file
--------------------
Only the exercise brief was written down as comments below; no
implementation code was added in the original submission. Per the
documentation task, no new logic is being added here (only this
docstring), so the file's behaviour (doing nothing when run) is
unchanged from before.
"""

# filter out elements depend on their index:
# use list comprehension and enumerate() to get elements with even index
# data = [100, 200, 300, 400, 500]
