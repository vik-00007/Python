# Definition and Properties of Sets in Python

# Definition:
# A set is an unordered collection of unique elements.
# Sets are mutable, meaning that elements can be added or removed.
# Sets are defined using curly braces {} or the set() function.

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)
# Output:
# Original set: {1, 2, 3, 4, 5}

# Creating an empty set
empty_set = set()
print("Empty set:", empty_set)
# Output:
# Empty set: set()

# Properties of Sets:

# 1. Unordered:
# Sets do not maintain any order of elements.
unordered_set = {3, 1, 4, 2}
print("Unordered set:", unordered_set)
# Output:
# Unordered set: {1, 2, 3, 4}

# 2. Unique Elements:
# Sets automatically remove duplicate elements.
unique_set = {1, 2, 2, 3, 3, 3}
print("Set with unique elements:", unique_set)
# Output:
# Set with unique elements: {1, 2, 3}

# 3. Mutable:
# Elements can be added or removed from sets.
mutable_set = {1, 2, 3}
mutable_set.add(4)  # Adding an element
print("After adding an element:", mutable_set)
# Output:
# After adding an element: {1, 2, 3, 4}
mutable_set.remove(1)  # Removing an element
print("After removing an element:", mutable_set)
# Output:
# After removing an element: {2, 3, 4}

# 4. Unindexed:
# Sets do not support indexing, slicing, or other sequence-like behavior.
try:
    element = unordered_set[0]
except TypeError as e:
    print("Error:", e)
# Output:
# Error: 'set' object is not subscriptable

# 5. No Duplicates:
# Sets automatically filter out duplicate values.
no_duplicates_set = {1, 1, 2, 2, 3, 3}
print("Set with no duplicates:", no_duplicates_set)
# Output:
# Set with no duplicates: {1, 2, 3}

# 6. Can Contain Heterogeneous Types:
# Sets can contain different data types.
heterogeneous_set = {1, "hello", 3.14}
print("Heterogeneous set:", heterogeneous_set)
# Output:
# Heterogeneous set: {1, 'hello', 3.14}

# 7. Immutable Elements:
# Elements of a set must be immutable (e.g., numbers, strings, tuples).
# Mutable elements like lists or dictionaries cannot be included in a set.
try:
    invalid_set = {1, [2, 3]}
except TypeError as e:
    print("Error:", e)
# Output:
# Error: unhashable type: 'list'

# Examples of Common Set Operations:

# Union of sets (A | B)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
print("Union of set_a and set_b:", union_set)
# Output:
# Union of set_a and set_b: {1, 2, 3, 4, 5}

# Intersection of sets (A & B)
intersection_set = set_a & set_b
print("Intersection of set_a and set_b:", intersection_set)
# Output:
# Intersection of set_a and set_b: {3}

# Difference of sets (A - B)
difference_set = set_a - set_b
print("Difference of set_a and set_b:", difference_set)
# Output:
# Difference of set_a and set_b: {1, 2}

# Symmetric Difference of sets (A ^ B)
symmetric_difference_set = set_a ^ set_b
print("Symmetric difference of set_a and set_b:", symmetric_difference_set)
# Output:
# Symmetric difference of set_a and set_b: {1, 2, 4, 5}

# Checking if a set is a subset of another set (A <= B)
is_subset = {1, 2}.issubset(set_a)
print("Is {1, 2} a subset of set_a?", is_subset)
# Output:
# Is {1, 2} a subset of set_a? True

# Checking if a set is a superset of another set (A >= B)
is_superset = set_a.issuperset({1, 2})
print("Is set_a a superset of {1, 2}?", is_superset)
# Output:
# Is set_a a superset of {1, 2}? True

# Conclusion: Sets are a versatile and powerful data structure in Python,
# offering efficient membership tests, unique element storage, and 
# support for mathematical operations. They are particularly useful 
# for eliminating duplicates and performing set-based operations.
