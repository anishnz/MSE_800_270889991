"""
Week 5 - Activity 5.1: Extract records matching a condition from a list of
dictionaries, using a list comprehension.

DEFINITION: List Comprehension with a Filter Condition
---------------------------------------------------------
The form [item for item in iterable if condition] loops over every item
in the iterable and keeps only the ones where "condition" evaluates to
True, building a new filtered list. Here each "item" is itself a
dictionary, and the condition checks one of its keys ("age").

Exercise goal:
    From a list of person dictionaries, keep only the people whose age is
    greater than 25.
"""

# extract information with age greater than 25 from the following list of dictionaries
data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]

# Using list comprehension to filter the data
# For each "person" dictionary in data, keep it only if person["age"] > 25.
# Alice (28) and Charlie (30) pass; Bob (24) is filtered out.
filtered_data = [person for person in data if person["age"] > 25]
# Print the filtered data
print(filtered_data)
