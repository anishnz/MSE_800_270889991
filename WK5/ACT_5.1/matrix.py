"""
Week 5 - Activity 5.1: Matrix multiplication using numpy.

DEFINITION: Matrix Multiplication (Dot Product)
--------------------------------------------------
For two matrices A (of shape m x n) and B (of shape n x p), the matrix
product A . B is a new matrix of shape m x p, where each output element
is the sum of the element-wise products of a row from A and a column
from B. This requires A's number of COLUMNS to match B's number of ROWS.
numpy's np.dot() (or the @ operator) performs this calculation.
"""

import numpy as np  # numpy provides array creation and the dot() function

# m1 is a 3x5 matrix (3 rows, 5 columns)
m1 = np.array([[1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0]])

# m2 is a 5x2 matrix (5 rows, 2 columns)
m2 = np.array([[1, 0],
              [0, 1],
              [0, 0],
              [0, 0],
              [0, 0]])

# m1 has 5 columns and m2 has 5 rows, so they are compatible for matrix
# multiplication. The result of np.dot(m1, m2) is a 3x2 matrix.
print(np.dot(m1,m2))
