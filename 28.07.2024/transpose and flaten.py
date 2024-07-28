import numpy as np
rows,cols=map(int, input().strip().split())
matrix=np.array([list(map(int, input().strip().split())) for _ in range(rows)])
transpose_matrix=matrix.T
print(transpose_matrix)
flattened_matrix=matrix.flatten()
print(flattened_matrix)
