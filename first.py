import numpy as np

# 1D Array
print("1D array")
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Shape and Data Type
print("Shape of arr:", arr.shape)
print("Data type:", arr.dtype)

# 2D Array
print("\n2D array")
arr2 = np.array([
    [1, 2, 3, 4, 5],
    [3, 4, 5, 6, 7]
])
print(arr2)
print("Type of arr2:", type(arr2))

# 3D Array
print("\n3D array")
arr3 = np.array([
    [
        [1, 2, 35],
        [2, 6, 3],
        [45, 78, 2]
    ]
])
print(arr3)

# Transpose of 3D array
print("\nTranspose of arr3")
print(arr3.transpose())

# Empty array
print("\nEmpty Array (4x4)")
empty_arr = np.empty((4, 4), dtype=int)
print(empty_arr)

# Ones array
print("\nOnes Array")
x = np.ones(6)
print(x)

# Zeros array (1D)
print("\nZeros Array (1D)")
y = np.zeros(6)
print(y)

# Zeros array (2D)
print("\nZeros Array (6x3)")
z = np.zeros((6, 3))
print(z)

# Integer zeros array
print("\nInteger Zeros Array (6x3)")
m = np.zeros((6, 3), dtype=int)
print(m)

# Arange
print("\nArange from 1 to 19")
a = np.arange(1, 20)
print(a)

# Odd numbers from 1 to 17 (9 elements)
print("\nOdd Numbers")
a = np.arange(1, 18, 2)
print(a)

# Reshape into 3x3
print("\nReshaped Array (3x3)")
a = a.reshape(3, 3)
print(a)

b = a.flatten()
print("\nFlattened Array")
print(b)

m = np.arange(1, 51).reshape(10,5)
print(m)

print(m[0])

print(m[1][1])

print(m[2])

print(m[2:5])

print(m[0:100])

print(m[:2])

print(m[2:5,4])

print(m[:,:])

print(m[:,2:5])
print(m[:,2:5].dtype)