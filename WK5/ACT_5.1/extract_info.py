# extract information with age greater than 25 from the following list of dictionaries
data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]

# Using list comprehension to filter the data
filtered_data = [person for person in data if person["age"] > 25]   
# Print the filtered data   
print(filtered_data)   