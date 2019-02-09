import numpy as np

# Create a Matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
# Return the max element
print(np.max(matrix))
# Return the min element
print(np.min(matrix))
# To find the max element in each column
print(np.max(matrix,axis=0))
# To find the max element in each row
print(np.max(matrix, axis=1))

