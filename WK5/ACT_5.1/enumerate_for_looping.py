"""
Week 5 - Activity 5.1: Adjust list values using enumerate() in a for-loop.

DEFINITION: enumerate()
------------------------
enumerate(iterable) returns pairs of (index, value) while looping, e.g.
enumerate([88, 92]) yields (0, 88), then (1, 92). This lets a for-loop
know an item's position in the list without maintaining a separate
counter variable, and makes it possible to write back to that exact
position with iterable[index] = new_value.

Exercise goal:
    Add 5 bonus points to every grade in the list, except the 5th grade
    (index 4), which instead gets a bigger 10-point bonus.
"""

# use enumerate() for looping to add 5 extra point to each grade in the list, the 5th one add 10
#grades = [88, 92, 78, 65, 50, 94]

grades = [88, 92, 78, 65, 50, 94]  # starting list of grades to adjust

# enumerate(grades) gives (index, grade) for every item as we loop
for index, grade in enumerate(grades):
    if index == 4:       # 5th item because index starts from 0
        # 5th grade (index 4) gets a 10-point bonus instead of 5
        grades[index] = grade + 10
    else:
        # every other grade gets the standard 5-point bonus
        grades[index] = grade + 5

print(grades)  # prints the list after all bonuses have been applied
