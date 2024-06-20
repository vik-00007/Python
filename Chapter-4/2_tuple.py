# Tuples and Tuple Methods in Python

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)
# Output:
# Original tuple: (1, 2, 3, 4, 5)

# Creating a tuple with mixed data types
mixed_tuple = (1, "hello", 3.14)
print("Mixed tuple:", mixed_tuple)
# Output:
# Mixed tuple: (1, 'hello', 3.14)

# Creating a nested tuple
nested_tuple = (1, (2, 3), (4, 5, 6))
print("Nested tuple:", nested_tuple)
# Output:
# Nested tuple: (1, (2, 3), (4, 5, 6))

# Accessing elements in a tuple
print("Element at index 1:", my_tuple[1])
# Output:
# Element at index 1: 2

# Slicing a tuple
sliced_tuple = my_tuple[1:4]
print("Sliced tuple (my_tuple[1:4]):", sliced_tuple)
# Output:
# Sliced tuple (my_tuple[1:4]): (2, 3, 4)

# Tuple concatenation
concatenated_tuple = my_tuple + (6, 7)
print("Concatenated tuple:", concatenated_tuple)
# Output:
# Concatenated tuple: (1, 2, 3, 4, 5, 6, 7)

# Tuple repetition
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)
# Output:
# Repeated tuple: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Checking if an element exists in a tuple
element_exists = 3 in my_tuple
print("Does 3 exist in my_tuple?", element_exists)
# Output:
# Does 3 exist in my_tuple? True

# Finding the length of a tuple
tuple_length = len(my_tuple)
print("Length of my_tuple:", tuple_length)
# Output:
# Length of my_tuple: 5

# Using the count() method to count occurrences of an element
count_of_3 = my_tuple.count(3)
print("Count of 3 in my_tuple:", count_of_3)
# Output:
# Count of 3 in my_tuple: 1

# Using the index() method to find the index of an element
index_of_4 = my_tuple.index(4)
print("Index of 4 in my_tuple:", index_of_4)
# Output:
# Index of 4 in my_tuple: 3

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)
# Output:
# Unpacked values: 1 2 3 4 5

# Nested tuple unpacking
nested_tuple = (1, (2, 3), 4)
x, (y, z), w = nested_tuple
print("Nested unpacked values:", x, y, z, w)
# Output:
# Nested unpacked values: 1 2 3 4

# Converting a list to a tuple
my_list = [1, 2, 3, 4, 5]
list_to_tuple = tuple(my_list)
print("Converted list to tuple:", list_to_tuple)
# Output:
# Converted list to tuple: (1, 2, 3, 4, 5)

# Converting a tuple to a list
tuple_to_list = list(my_tuple)
print("Converted tuple to list:", tuple_to_list)
# Output:
# Converted tuple to list: [1, 2, 3, 4, 5]

# Immutable nature of tuples
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)
# Output:
# Error: 'tuple' object does not support item assignment

# Advantages of using tuples:
# 1. Tuples are faster than lists for processing.
# 2. Tuples are immutable, meaning their content cannot be altered.
# 3. Tuples can be used as keys in dictionaries.
# 4. Tuples are useful for grouping related data.

# Example of using tuples as dictionary keys
my_dict = {('key1', 1): 'value1', ('key2', 2): 'value2'}
print("Dictionary with tuple keys:", my_dict)
# Output:
# Dictionary with tuple keys: {('key1', 1): 'value1', ('key2', 2): 'value2'}

# Example of a tuple for returning multiple values from a function
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 2, 3, 4, 5])
print("Min and Max values:", min_val, max_val)
# Output:
# Min and Max values: 1 5

# Conclusion: Tuples are an essential data structure in Python, providing immutability, faster processing, and the ability to be used as dictionary keys. They are particularly useful for grouping related data and returning multiple values from functions.
