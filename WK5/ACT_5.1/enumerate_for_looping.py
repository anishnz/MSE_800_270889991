# use enumerate() for looping to add 5 extra point to each grade in the list, the 5th one add 10 
#grades = [88, 92, 78, 65, 50, 94]

grades = [88, 92, 78, 65, 50, 94]

for index, grade in enumerate(grades):
    if index == 4:       # 5th item because index starts from 0
        grades[index] = grade + 10
    else:
        grades[index] = grade + 5

print(grades) 