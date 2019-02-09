import numpy as np

# Create a Matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# Calculate the Eigenvalues and Eigenvectors of that Matrix
eigenvalues, eigenvectors=np.linalg.eig(matrix)
print(eigenvalues)
print(eigenvectors)
