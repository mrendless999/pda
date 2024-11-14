# 1. Creation of Data Types

# String
str1 = "Hello"
str2 = "World"

# List
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']

# Tuple
tuple1 = (10, 20, 30)
tuple2 = ('x', 'y', 'z')

# Dictionary
dict1 = {1: 'one', 2: 'two'}
dict2 = {3: 'three', 4: 'four'}

# Set
set1 = {1, 2, 3}
set2 = {3, 4, 5}


# 2. Indexing and Slicing

# String
print("Indexing in String:", str1[1])  # Accessing the 2nd character (index 1)
print("Slicing in String:", str1[1:4])  # Slicing the string from index 1 to 3 (exclusive)

# List
print("Indexing in List:", list1[2])  # Accessing the 3rd element (index 2)
print("Slicing in List:", list1[1:3])  # Slicing the list from index 1 to 2 (exclusive)

# Tuple
print("Indexing in Tuple:", tuple1[0])  # Accessing the 1st element (index 0)
print("Slicing in Tuple:", tuple1[1:])  # Slicing the tuple from index 1 to the end

# Dictionary (indexing by key)
print("Accessing Dictionary by Key:", dict1[1])  # Accessing value associated with key 1

# Set (No indexing or slicing, but can be looped)
for item in set1:
    print("Item in Set:", item)


# 3. Concatenation

# String
concat_str = str1 + " " + str2
print("Concatenated String:", concat_str)

# List
concat_list = list1 + list2
print("Concatenated List:", concat_list)

# Tuple
concat_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concat_tuple)

# Dictionary
dict1.update(dict2)  # Merging dict2 into dict1
# Alternatively, in Python 3.9+, you can use dict3 = dict1 | dict2 for merging
print("Merged Dictionary:", dict1)

# Set
concat_set = set1 | set2  # Union of two sets
print("Union of Sets:", concat_set)


# 4. Repetition

# String
repeat_str = str1 * 3  # Repeats the string 3 times
print("Repeated String:", repeat_str)

# List
repeat_list = list1 * 2  # Repeats the list 2 times
print("Repeated List:", repeat_list)

# Tuple
repeat_tuple = tuple1 * 2  # Repeats the tuple 2 times
print("Repeated Tuple:", repeat_tuple)
