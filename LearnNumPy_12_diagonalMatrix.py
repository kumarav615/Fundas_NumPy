import numpy as np

# Create a Matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# Print the Principal diagonal
print(matrix.diagonal())

# Print the diagonal one above the Principal diagonal
print(matrix.diagonal(offset=1))

# Print the diagonal one below Principal diagonal
print(matrix.diagonal(offset=-1))
