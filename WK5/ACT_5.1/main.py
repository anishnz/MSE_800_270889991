"""
Week 5 - Activity 5.1: Create a dictionary from two separate lists.

DEFINITION: zip()
-------------------
zip(list_a, list_b) pairs up elements from both lists by position, e.g.
zip(['a','b'], [1,2]) produces the pairs ('a', 1) and ('b', 2). If the
lists are different lengths, zip() stops as soon as the SHORTER list
runs out, so any extra items in the longer list are silently dropped.

DEFINITION: dict()
--------------------
dict() can build a dictionary directly from an iterable of (key, value)
pairs, such as the pairs produced by zip(). So dict(zip(keys, values))
is a common one-line way to turn two parallel lists into a dictionary.
"""

# Create a Dictionary From Two Lists
# You are given two lists:
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
# NOTE: keys has 4 items but values has only 3. zip() pairs them up and
# stops at the shorter list, so the last key 'd' has no matching value
# and is simply left out of the result (this is existing/expected
# behaviour of zip(), not a bug being fixed here).

# Create a dictionary by zipping the two lists together
my_dict = dict(zip(keys, values))
print(my_dict)  # prints {'a': 1, 'b': 2, 'c': 3} -- 'd' is dropped
