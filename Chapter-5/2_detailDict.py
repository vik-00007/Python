# Dictionaries and Dictionary Methods in Python

# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Original dictionary:", my_dict)
# Output:
# Original dictionary: {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing a value by key
name = my_dict['name']
print("Accessed value (name):", name)
# Output:
# Accessed value (name): John

# Adding a new key-value pair
my_dict['email'] = 'john@example.com'
print("After adding new key-value pair:", my_dict)
# Output:
# After adding new key-value pair: {'name': 'John', 'age': 25, 'city': 'New York', 'email': 'john@example.com'}

# Updating a value by key
my_dict['age'] = 26
print("After updating age:", my_dict)
# Output:
# After updating age: {'name': 'John', 'age': 26, 'city': 'New York', 'email': 'john@example.com'}

# Removing a key-value pair using pop()
email = my_dict.pop('email')
print("After popping email:", my_dict)
print("Popped value (email):", email)
# Output:
# After popping email: {'name': 'John', 'age': 26, 'city': 'New York'}
# Popped value (email): john@example.com

# Removing the last inserted key-value pair using popitem()
last_item = my_dict.popitem()
print("After popitem():", my_dict)
print("Popped item:", last_item)
# Output:
# After popitem(): {'name': 'John', 'age': 26}
# Popped item: ('city', 'New York')

# Getting a value by key using get()
age = my_dict.get('age')
print("Value obtained using get() (age):", age)
# Output:
# Value obtained using get() (age): 26

# Getting a value with a default using get()
email = my_dict.get('email', 'not provided')
print("Value obtained using get() with default (email):", email)
# Output:
# Value obtained using get() with default (email): not provided

# Checking if a key exists in the dictionary
is_name_key_present = 'name' in my_dict
print("Is 'name' key present?", is_name_key_present)
# Output:
# Is 'name' key present? True

# Getting all keys using keys()
keys = my_dict.keys()
print("Keys:", keys)
# Output:
# Keys: dict_keys(['name', 'age'])

# Getting all values using values()
values = my_dict.values()
print("Values:", values)
# Output:
# Values: dict_values(['John', 26])

# Getting all key-value pairs using items()
items = my_dict.items()
print("Items:", items)
# Output:
# Items: dict_items([('name', 'John'), ('age', 26)])

# Copying a dictionary using copy()
copied_dict = my_dict.copy()
print("Copied dictionary:", copied_dict)
# Output:
# Copied dictionary: {'name': 'John', 'age': 26}

# Updating a dictionary with another dictionary using update()
my_dict.update({'city': 'Los Angeles', 'email': 'john@example.com'})
print("After update():", my_dict)
# Output:
# After update(): {'name': 'John', 'age': 26, 'city': 'Los Angeles', 'email': 'john@example.com'}

# Clearing all items from the dictionary using clear()
my_dict.clear()
print("After clear():", my_dict)
# Output:
# After clear(): {}

# Creating a dictionary from keys with a common value using fromkeys()
keys = ['name', 'age', 'city']
common_value_dict = dict.fromkeys(keys, 'unknown')
print("Dictionary created using fromkeys():", common_value_dict)
# Output:
# Dictionary created using fromkeys(): {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

# Creating a nested dictionary
nested_dict = {'person1': {'name': 'John', 'age': 25}, 'person2': {'name': 'Jane', 'age': 22}}
print("Nested dictionary:", nested_dict)
# Output:
# Nested dictionary: {'person1': {'name': 'John', 'age': 25}, 'person2': {'name': 'Jane', 'age': 22}}

# Accessing elements in a nested dictionary
person1_name = nested_dict['person1']['name']
print("Name of person1:", person1_name)
# Output:
# Name of person1: John

# Using setdefault() to get a value and set it if not present
default_city = my_dict.setdefault('city', 'Unknown')
print("Default city:", default_city)
print("Dictionary after setdefault():", my_dict)
# Output:
# Default city: Unknown
# Dictionary after setdefault(): {'city': 'Unknown'}

# Example of using dictionaries for counting
count_dict = {}
for char in "hello":
    count_dict[char] = count_dict.get(char, 0) + 1
print("Character count dictionary:", count_dict)
# Output:
# Character count dictionary: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Example of a dictionary comprehension
squared_dict = {num: num**2 for num in range(1, 6)}
print("Squared dictionary:", squared_dict)
# Output:
# Squared dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Conclusion: Dictionaries are versatile and powerful data structures in Python, allowing for efficient storage and retrieval of key-value pairs. The methods provided offer extensive functionality for manipulating dictionary data, making them essential for any Python programmer.
