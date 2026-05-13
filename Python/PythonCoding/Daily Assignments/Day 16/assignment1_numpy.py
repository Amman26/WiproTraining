# Assignment 1: NumPy Array Surgery

import numpy as np

# Dataset
np.random.seed(42)
data_array = np.random.randint(1, 501, size=(10, 10))

print("Original Array:\n")
print(data_array)

# 1. Find global mean and replace values greater than mean with 0
global_mean = np.mean(data_array)

modified_array = np.where(data_array > global_mean, 0, data_array)

print("\nGlobal Mean:", global_mean)

print("\nModified Array:\n")
print(modified_array)

# 2. Sum of each column and standard deviation of each row
column_sum = np.sum(modified_array, axis=0)
row_std = np.std(modified_array, axis=1)

print("\nColumn Sum:\n", column_sum)

print("\nRow Standard Deviation:\n", row_std)

# 3. Extract center 4x4 sub-matrix and flatten to 1D
sub_matrix = modified_array[3:7, 3:7]

flat_array = sub_matrix.flatten()

print("\nCenter 4x4 Sub-Matrix:\n")
print(sub_matrix)

print("\nFlattened 1D Array:\n")
print(flat_array)