import numpy as np

# Create Matrix-1
matrix_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create Matrix-2
matrix_2 = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3]])

# Add the 2 Matrices
print(np.add(matrix_1,matrix_2))

# Subtraction
print(np.subtract(matrix_1,matrix_2))

# Multiplication(Element wise, not Dot Product)
print(matrix_1*matrix_2)
