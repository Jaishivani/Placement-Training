import numpy as np
n, m, _=map(int, input().strip().split())
array_1=np.array([list(map(int, input().strip().split())) for _ in range(n)])
array_2=np.array([list(map(int, input().strip().split())) for _ in range(n)])
concatenated_array=np.concatenate((array_1, array_2), axis=0)
print(concatenated_array)
