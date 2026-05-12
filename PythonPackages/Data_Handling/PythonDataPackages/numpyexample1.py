import numpy as np


arr = np.arange(2, 20, 2, dtype = np.int_)
arr1 = np.arange(10, 20, 2, dtype = np.int_)
arr2 = np.arange(0, 20, 3, dtype = np.int_)

print(arr)
print(arr1)
print(arr2)

s =slice(0,7,2)

print('Slice1', arr[s])
print('Slice2', arr1[s])
print('Slice3', arr2[s])