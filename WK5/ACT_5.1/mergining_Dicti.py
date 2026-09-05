# Week 5 - Activity 2: Merging Dictionaries with Conditions
#Use the following lists as keys and values. Generate a dictionary output by selecting the key–value pairs where the value is an odd number.
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
dict1 = dict(zip(Key1, Value1))
dict2 = dict(zip(Key2, Value2))

# Merge the dictionaries
merged_dict = {**dict1, **dict2}

# Select key-value pairs where the value is odd
result = {key: value for key, value in merged_dict.items() if value % 2 != 0}

print(result)         