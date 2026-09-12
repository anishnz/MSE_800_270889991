"""
Week 5 - Activity 5.1: Flatten a matrix using a list comprehension.

DEFINITION: List Comprehension
-------------------------------
A list comprehension builds a new list in one line using the form:
    [expression for item in iterable]
Here it is used with a NESTED loop (a loop inside the comprehension's
own loop), with the INTENT of flattening a 2D matrix (a list/array of
rows) into a single flat 1D list of individual elements.

DEFINITION: Flattening
------------------------
Flattening means converting a multi-dimensional structure (e.g. a matrix
made of rows of numbers) into a single-dimensional list containing all
the same values, e.g. [[1,2,3],[4,5,6]] -> [1, 2, 3, 4, 5, 6].

IMPORTANT QUIRK in this specific script: because a numpy matrix always
stays 2D (even a single row is represented as a 1xN matrix, never a
plain 1D array), iterating over a row does NOT yield individual numbers
here -- it yields that same 1xN row again. So the actual result is a
list of the original rows (each still a matrix object), not a fully
flat list of plain numbers. See the printed output for what this
actually produces.
"""

# use list comprehension to flatten the matrix
#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

import numpy as np  # numpy provides the matrix data structure used below

# Build a 3x3 numpy matrix from a list of rows.
# NOTE: this reassigns the name "np.matrix" (normally numpy's matrix
# CLASS) to instead point at this specific matrix INSTANCE. This is
# unusual/shadowing, but it does not break anything here because
# np.matrix (the class) is not needed again later in this script.
np.matrix = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Nested list comprehension:
#   outer loop "for row in np.matrix" -> iterates over each row of the
#                                         matrix (there are 3 rows)
#   inner loop "for element in row"   -> intended to iterate over each
#                                         value inside that row, but since
#                                         a numpy matrix row is itself a
#                                         1xN matrix (still 2D), this inner
#                                         loop runs only ONCE per row and
#                                         yields the row itself again.
# Because of that quirk, the result is a list of 3 items, each being one
# of the original 1x3 matrix rows -- e.g.
#   [matrix([[1, 2, 3]]), matrix([[4, 5, 6]]), matrix([[7, 8, 9]])]
# rather than a fully flat list of 9 plain numbers.
flattened_matrix = [element for row in np.matrix for element in row]
print(flattened_matrix)   # prints the list described above
