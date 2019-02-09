import numpy as np

# create a vector as row
vector_row = np.array([1, 2, 3, 4, 5, 6])
print(vector_row)

# create a matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# Select 3rd element of vector
print(vector_row[2])

# select 2nd row 2nd column of matrix
print(matrix[1, 1])

# select all elements of a vector
print(vector_row[:])

# Select everything up to and including the 3rd element
print(vector_row[:3])

# Select the everything after the 3rd element
print(vector_row[3:])

# Select the last element
print(vector_row[-1])

# Select the first 2 rows and all the columns of the matrix
print(matrix[:2, :])

# Select all rows and the 2nd column of the matrix
print(matrix[:, 1:2])
