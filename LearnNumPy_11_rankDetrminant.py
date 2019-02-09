import numpy as np

# Create a Matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# Calculate the Determinant
print(np.linalg.det(matrix))

# Calculate the Rank
print(np.linalg.matrix_rank(matrix))
