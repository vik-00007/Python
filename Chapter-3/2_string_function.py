# capitalize(): Converts the first character to uppercase and the rest to lowercase.
s = "hello world"
print(s.capitalize())  # Output: "Hello world"

# lower(): Converts all characters to lowercase.
s = "Hello World"
print(s.lower())  # Output: "hello world"

# upper(): Converts all characters to uppercase.
s = "hello world"
print(s.upper())  # Output: "HELLO WORLD"

# title(): Converts the first character of each word to uppercase and the rest to lowercase.
s = "hello world"
print(s.title())  # Output: "Hello World"

# swapcase(): Swaps the case of each character.
s = "Hello World"
print(s.swapcase())  # Output: "hELLO wORLD"

# strip(): Removes leading and trailing whitespace.
s = "  hello world  "
print(s.strip())  # Output: "hello world"

# lstrip(): Removes leading whitespace.
s = "  hello world"
print(s.lstrip())  # Output: "hello world"

# rstrip(): Removes trailing whitespace.
s = "hello world  "
print(s.rstrip())  # Output: "hello world"

# split(): Splits the string into a list of substrings.
s = "hello world"
print(s.split())  # Output: ['hello', 'world']

# join(): Joins a list of strings into a single string with a specified delimiter.
words = ['hello', 'world']
print(" ".join(words))  # Output: "hello world"

# find(): Returns the lowest index of the substring.
s = "hello world"
print(s.find('world'))  # Output: 6

# rfind(): Returns the highest index of the substring.
s = "hello world world"
print(s.rfind('world'))  # Output: 12

# replace(): Replaces occurrences of a substring with another substring.
s = "hello world"
print(s.replace('world', 'Python'))  # Output: "hello Python"

# startswith(): Checks if the string starts with a specified substring.
s = "hello world"
print(s.startswith('hello'))  # Output: True

# endswith(): Checks if the string ends with a specified substring.
s = "hello world"
print(s.endswith('world'))  # Output: True

# count(): Returns the number of occurrences of a substring.
s = "hello world"
print(s.count('l'))  # Output: 3

# isalpha(): Checks if all characters are alphabetic.
s = "hello"
print(s.isalpha())  # Output: True

# isdigit(): Checks if all characters are digits.
s = "12345"
print(s.isdigit())  # Output: True

# isalnum(): Checks if all characters are alphanumeric.
s = "hello123"
print(s.isalnum())  # Output: True

# isspace(): Checks if all characters are whitespace.
s = "   "
print(s.isspace())  # Output: True

# format(): Formats the string using placeholders.
s = "Hello, {}. Welcome to {}!"
print(s.format("Alice", "Wonderland"))  # Output: "Hello, Alice. Welcome to Wonderland!"

# len(): Returns the length of the string.
s = "hello world"
print(len(s))  # Output: 11

# in Operator: Checks if a substring exists within the string.
s = "hello world"
print("world" in s)  # Output: True

# not in Operator: Checks if a substring does not exist within the string.
s = "hello world"
print("Python" not in s)  # Output: True

# index(): Returns the lowest index of the substring. Raises ValueError if not found.
s = "hello world"
print(s.index('world'))  # Output: 6

# rindex(): Returns the highest index of the substring. Raises ValueError if not found.
s = "hello world world"
print(s.rindex('world'))  # Output: 12

# partition(): Splits the string at the first occurrence of the separator into a tuple.
s = "hello world"
print(s.partition(' '))  # Output: ('hello', ' ', 'world')

# rpartition(): Splits the string at the last occurrence of the separator into a tuple.
s = "hello world world"
print(s.rpartition(' '))  # Output: ('hello world', ' ', 'world')

# splitlines(): Splits the string at line breaks into a list of lines.
s = "hello\nworld"
print(s.splitlines())  # Output: ['hello', 'world']

# zfill(): Pads the string on the left with zeros to fill a specified width.
s = "42"
print(s.zfill(5))  # Output: "00042"
