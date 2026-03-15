from asyncio import exceptions

import numpy as np
# array1 = np.array([1,2,3])
# array2 = 2
# result = array1 * array2
# print(result)

# np.save('numpyarray.npy', array1)

# Indexing and slicing:
# array = np.array([10, 20, 30, 40, 50])
# print(array[4]) 

# file input output
# loaded_array = np.load('numpyarray.npy')
# print(loaded_array)

# Data type object
arr = np.array([[1.5, 2.5],[3,5]], dtype=np.float64)
# arr = np.array([1, "a"], dtype=np.float64) 
print(arr)
# print(arr.dtype)

# print(arr.shape) 
# print(arr.size)   
# print(arr.ndim)   

#modifying array
arr[0, 1] = 4.5
print(arr)

# copy
arr_copy = arr.copy()

# view
arr_view = arr.view()

#arange
# arr_arange = np.arange(0, 10, 2)
# print(arr_arange)

# matrix= np.ones((3, 3))
# print(matrix)
# matrix = np.zeros((2, 4))
# print(matrix)

# matrix =np.ones((3, 3))
# print(matrix)
# matrix+= np.array([1,2,3])
# print(matrix)

index = np.where(arr == 1.5)
print(index)

#Descriptive statistics
print(np.mean(arr))
print(np.std(arr))


# 4: NumPy Matrix Operations
# Q4: NumPy Matrix Operations
# 1. Create a 2x3 NumPy array with random integers between 1 and 50.
# 2. Perform the following operations:
# Calculate the sum of all elements.
# Find the maximum and minimum elements.
# Compute the mean of the elements.
# 3. Save the array and results to a file named 
# matrix_results.txt . Handle exceptions for file operations.

try:
    matrix = np.random.randint(1, 51, size=(2, 3))
    print("Matrix:\n", matrix)

    total_sum = np.sum(matrix)
    max_element = np.max(matrix)
    min_element = np.min(matrix)
    mean_value = np.mean(matrix)

    results = f"Sum: {total_sum}\nMax: {max_element}\nMin: {min_element}\nMean: {mean_value}\n"

    with open('matrix_results.txt', 'w') as file:
        file.write(results)
except Exception as e:
    print(f"An error occurred: {e}")