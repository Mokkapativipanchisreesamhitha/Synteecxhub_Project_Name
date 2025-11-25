import numpy as np
# creating various arrays 
# normal arrays
arr1 = np.array([1,2,3,4,5])
#range arrays
arr2 = np.arange(0,20,2)
#evenly spaced arrays
arr3 = np.linspace(0,1,5)
#random arrays
arr4 = np.random.randint(1,100,size=(3,3))

print("arr1 =",arr1)
print("arr2 =",arr2)
print("arr3 =",arr3)
print("arr4 =",arr4)


#sample numpy array

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("matrix =\n",matrix)

# indexing
print("Element at (0,0):",matrix[0,0])
print("Element at (1,2):",matrix[1,2])

#slicing
print("\n First row:",matrix[0,:])
print("First column:",matrix[:,0])
print("Submatrix (1:3,1:3):\n",matrix[1:3,1:3])

#axis-wise operations
print("\n row-wise sum:",matrix.sum(axis=1))
print("column-wise sum:",matrix.sum(axis=0))

print("row-wise mean:",matrix.mean(axis=1))
print("column-wise mean:",matrix.mean(axis=0))


# ---- RESHAPING ----
arr = np.arange(12)  # Create 1D array with 12 elements
print("Original Array:", arr)

reshaped_arr = arr.reshape(3, 4)  # Reshape into 3 rows, 4 columns
print("\nReshaped (3x4):\n", reshaped_arr)

# ---- BROADCASTING ----
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

add_vector = np.array([10, 20, 30])  # 1×3 vector

broadcast_result = matrix + add_vector  # Broadcasting happens here
print("\nBroadcasting Result:\n", broadcast_result)


# Creating a sample array
data = np.array([10, 20, 30, 40, 50])
print("Original Data:", data)

# ---- SAVING ARRAY ----
np.save("my_array.npy", data)
print("\nArray saved successfully as 'my_array.npy'")

# ---- LOADING ARRAY ----
loaded_data = np.load("my_array.npy")
print("\nLoaded Data:", loaded_data)

# ---- SAVING MULTIPLE ARRAYS ----
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.savez("multiple_arrays.npz", array1=a, array2=b)
print("\nMultiple arrays saved as 'multiple_arrays.npz'")

# ---- LOADING MULTIPLE ARRAYS ----
loaded_multi = np.load("multiple_arrays.npz")
print("\nLoaded array1:", loaded_multi["array1"])
print("Loaded array2:", loaded_multi["array2"])


import numpy as np
import time

# -------- Define python_list --------
python_list = list(range(1_000_000))  
# A list with 1 million numbers
# You can use smaller size if your laptop is slow

# -------- Define numpy_array --------
numpy_array = np.array(python_list)

# ---------- Python list timing ----------
start = time.time()
[x * 2 for x in python_list]    # multiply each element by 2
end = time.time()
print("Python list time:", end - start)

# ---------- NumPy array timing ----------
start = time.time()
numpy_array * 2                 # multiply whole array by 2
end = time.time()
print("NumPy array time:", end - start)