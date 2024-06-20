# List and List Methods in Python

# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
# Output:
# Original list: [1, 2, 3, 4, 5]

# append(): Adds an element at the end of the list
my_list.append(6)
print("After append(6):", my_list)
# Output:
# After append(6): [1, 2, 3, 4, 5, 6]

# extend(): Adds all elements of a list (or any iterable) to the end of the list
my_list.extend([7, 8, 9])
print("After extend([7, 8, 9]):", my_list)
# Output:
# After extend([7, 8, 9]): [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert(): Inserts an element at a specified position
my_list.insert(0, 0)
print("After insert(0, 0):", my_list)
# Output:
# After insert(0, 0): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# remove(): Removes the first occurrence of an element
my_list.remove(0)
print("After remove(0):", my_list)
# Output:
# After remove(0): [1, 2, 3, 4, 5, 6, 7, 8, 9]

# pop(): Removes and returns the element at the specified position
popped_element = my_list.pop(0)
print("After pop(0):", my_list)
print("Popped element:", popped_element)
# Output:
# After pop(0): [2, 3, 4, 5, 6, 7, 8, 9]
# Popped element: 1

# clear(): Removes all elements from the list
my_list.clear()
print("After clear():", my_list)
# Output:
# After clear(): []

# Creating a new list for further methods
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# index(): Returns the index of the first occurrence of an element
index_of_5 = my_list.index(5)
print("Index of 5:", index_of_5)
# Output:
# Index of 5: 4

# count(): Returns the count of the number of occurrences of an element
count_of_3 = my_list.count(3)
print("Count of 3:", count_of_3)
# Output:
# Count of 3: 1

# sort(): Sorts the list in ascending order
my_list.sort()
print("After sort():", my_list)
# Output:
# After sort(): [1, 2, 3, 4, 5, 6, 7, 8, 9]

# reverse(): Reverses the elements of the list
my_list.reverse()
print("After reverse():", my_list)
# Output:
# After reverse(): [9, 8, 7, 6, 5, 4, 3, 2, 1]

# copy(): Returns a shallow copy of the list
copied_list = my_list.copy()
print("Copied list:", copied_list)
# Output:
# Copied list: [9, 8, 7, 6, 5, 4, 3, 2, 1]

# List comprehensions: A concise way to create lists
squared_list = [x**2 for x in range(1, 6)]
print("List comprehension (squared numbers):", squared_list)
# Output:
# List comprehension (squared numbers): [1, 4, 9, 16, 25]

# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list:", nested_list)
# Output:
# Nested list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a nested list
print("Element at [1][2]:", nested_list[1][2])
# Output:
# Element at [1][2]: 6

# List slicing
sliced_list = my_list[2:5]
print("Sliced list (my_list[2:5]):", sliced_list)
# Output:
# Sliced list (my_list[2:5]): [7, 6, 5]

# List length
list_length = len(my_list)
print("Length of my_list:", list_length)
# Output:
# Length of my_list: 9

# Check if an element exists in the list
element_exists = 5 in my_list
print("Does 5 exist in my_list?", element_exists)
# Output:
# Does 5 exist in my_list? True

# Concatenating lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)
# Output:
# Concatenated list: [1, 2, 3, 4, 5, 6]

# Repeating lists
repeated_list = list1 * 3
print("Repeated list:", repeated_list)
# Output:
# Repeated list: [1, 2, 3, 1, 2, 3, 1, 2, 3]
