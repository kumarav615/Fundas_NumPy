import numpy as np

# Create a Matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# Reshape
print(matrix.reshape(9,1))

# Here -1 says as many columns as needed and 1 row
print(matrix.reshape(1,-1))

# If we provide only 1 value Reshape would return a 1-d array of that length
print(matrix.reshape(9))

# We can also use the Flatten method to convert a matrix to 1-d array
print(matrix.flatten())
