# Sparse matrices store only non zero elements and assume all other values will be zero,
# leading to significant computational savings.

import numpy as np

# create a Matrix
from scipy import sparse

matrix = np.array([[0, 0], [0, 1], [3, 0]])
print(matrix)

# create compressed Sparse Row (CSR)

matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)
