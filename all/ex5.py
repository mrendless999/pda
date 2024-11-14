import numpy as np
# 1. Create NumPy arrays from Python Data Structures
python_list = [1, 2, 3, 4, 5]
numpy_array_from_list = np.array(python_list)

python_tuple = (10, 20, 30, 40, 50)
numpy_array_from_tuple = np.array(python_tuple)

nested_list = [[1, 2, 3], [4, 5, 6]]
numpy_array_from_nested_list = np.array(nested_list)

# 2. Create NumPy arrays from intrinsic NumPy objects
numpy_array_arange = np.arange(0, 10, 2)  # Creates an array of evenly spaced values within a given range
numpy_array_linspace = np.linspace(0, 1, 5)  # Creates an array of 5 evenly spaced values between 0 and 1
numpy_array_ones = np.ones((3, 3))  # Creates a 3x3 array filled with ones
numpy_array_zeros = np.zeros((2, 4))  # Creates a 2x4 array filled with zeros
numpy_identity_matrix = np.eye(3)  # Creates a 3x3 identity matrix

# 3. Create NumPy arrays using random functions
numpy_random_uniform = np.random.rand(3, 3)  # Creates a 3x3 array with random values from a uniform distribution (0 to 1)
numpy_random_integers = np.random.randint(0, 10, size=(2, 3))  # Creates a 2x3 array with random integers between 0 and 9
numpy_random_normal = np.random.randn(4, 4)  # Creates a 4x4 array with random values from a normal distribution
numpy_random_sample = np.random.random_sample((2, 3))  # Creates a 2x3 array with random float values between 0 and 1

# Print results
print("NumPy array from list:", numpy_array_from_list)
print("NumPy array from tuple:", numpy_array_from_tuple)
print("NumPy array from nested list:\n", numpy_array_from_nested_list)
print("Array using arange:", numpy_array_arange)
print("Array using linspace:", numpy_array_linspace)
print("Array of ones:\n", numpy_array_ones)
print("Array of zeros:\n", numpy_array_zeros)
print("Identity matrix:\n", numpy_identity_matrix)
print("Random array (uniform distribution):\n", numpy_random_uniform)
print("Random array of integers:\n", numpy_random_integers)
print("Random array (normal distribution):\n", numpy_random_normal)
print("Random array (random_sample):\n", numpy_random_sample)
