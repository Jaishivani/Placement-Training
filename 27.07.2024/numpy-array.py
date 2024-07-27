import numpy
def arrays(arr):
    float_arr = list(map(float, arr))
    reversed_array = float_arr[::-1]
    return reversed_array
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
