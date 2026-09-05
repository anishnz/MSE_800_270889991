# Create a Dictionary From Two Lists
# You are given two lists:
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]

# Create a dictionary by zipping the two lists together
my_dict = dict(zip(keys, values))
print(my_dict)  