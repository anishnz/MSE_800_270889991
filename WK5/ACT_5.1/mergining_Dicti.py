"""
Week 5 - Activity 5.1: Merging Dictionaries with Conditions.

DEFINITION: zip() + dict()
-----------------------------
dict(zip(keys, values)) pairs up two parallel lists by position and
turns the pairs into a dictionary, e.g. zip(['a','b'],[1,2]) -> dict
{'a': 1, 'b': 2}.

DEFINITION: Merging Dictionaries with **
-------------------------------------------
{**dict1, **dict2} unpacks all key/value pairs from dict1 and dict2 into
a single new dictionary. If both dictionaries share a key, the value
from the SECOND dictionary (dict2) wins, because it is unpacked last and
overwrites the earlier value for that key.

DEFINITION: Dictionary Comprehension with a Filter Condition
-----------------------------------------------------------------
{key: value for key, value in dict.items() if condition} loops over every
key/value pair and keeps only the pairs where "condition" is True,
building a new filtered dictionary.

Exercise goal:
    Build two dictionaries from parallel key/value lists, merge them
    (letting duplicate keys take the second dictionary's value), then
    keep only the entries whose value is an odd number.
"""

# Week 5 - Activity 2: Merging Dictionaries with Conditions
#Use the following lists as keys and values. Generate a dictionary output by selecting the key-value pairs where the value is an odd number.
#Key1:[a, b, c, d, f, g, h, e, a]
#Value1:[20, 3, 1, 88, 55, 92, 6, 90, 910]
#Key2:[u, b, o, x,  e, a]
#Value2:[200, 30, 10, 88, 55, 920]
#Share your code and the resulting output here with description.

Key1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'a']
Value1 = [20, 3, 1, 88, 55, 92, 6, 90, 910]

Key2 = ['u', 'b', 'o', 'x', 'e', 'a']
Value2 = [200, 30, 10, 88, 55, 920]

# Create dictionaries
# zip() pairs each key with its matching value by position; where a key
# repeats within the SAME list (e.g. 'a' appears twice in Key1), the
# later pair overwrites the earlier one once passed into dict().
dict1 = dict(zip(Key1, Value1))
dict2 = dict(zip(Key2, Value2))

# Merge the dictionaries
# {**dict1, **dict2} combines both dictionaries into one. Shared keys
# ('b', 'e', 'a') take dict2's value because dict2 is unpacked second.
merged_dict = {**dict1, **dict2}

# Select key-value pairs where the value is odd
# value % 2 != 0 is True only for odd numbers, so this dictionary
# comprehension keeps only the odd-valued entries from merged_dict.
result = {key: value for key, value in merged_dict.items() if value % 2 != 0}

print(result)
