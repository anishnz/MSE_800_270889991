# use list comprehension to flatten the matrix
#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

import numpy as np

np.matrix = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
flattened_matrix = [element for row in np.matrix for element in row]   
print(flattened_matrix)   

