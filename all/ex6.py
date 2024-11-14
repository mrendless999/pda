import numpy as np

# Creating a sample NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 1. Indexing8r
print("Element at row 2, column 3:", arr[1, 2])  # Indexing to get element at 2nd row, 3rd column (0-indexed)
print("First row:", arr[0])                      # Getting the entire first row
print("First column:", arr[:, 0])                # Getting the entire first column

# 2. Slicing
print("\nArray slice (first two rows and two columns):\n", arr[0:2, 0:2])  # Slicing to get a subarray (top left 2x2)
print("Last two elements of the second row:", arr[1, 1:])                  # Slicing the second row

# 3. Reshaping
reshaped_arr = arr.reshape(1, 9)  # Reshaping 3x3 array into a 1x9 array
print("\nReshaped array (3x3 to 1x9):\n", reshaped_arr)

reshaped_back = reshaped_arr.reshape(3, 3)  # Reshaping back to 3x3
print("\nReshaped back to 3x3:\n", reshaped_back)

# 4. Joining (Concatenation)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Joining along axis 0 (vertical stacking)
joined_vertically = np.vstack((arr1, arr2))
print("\nJoined vertically:\n", joined_vertically)

# Joining along axis 1 (horizontal stacking)
joined_horizontally = np.hstack((arr1, arr2))
print("\nJoined horizontally:\n", joined_horizontally)

# 5. Splitting
arr_split = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]])

# Splitting into two equal arrays along rows (axis 0)
split_arr = np.split(arr_split, 2, axis=0)
print("\nSplit along rows (axis 0):")
for part in split_arr:
    print(part)

# Splitting into three arrays along columns (axis 1)
split_arr_columns = np.split(arr_split, 3, axis=1)
print("\nSplit along columns (axis 1):")
for part in split_arr_columns:
    print(part)
