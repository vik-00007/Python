# Escape Sequences in Python

# Newline
newline = "Hello,\nWorld!"
print(newline)
# Output:
# Hello,
# World!

# Backslash
backslash = "This is a backslash: \\"
print(backslash)
# Output:
# This is a backslash: \

# Single Quote
single_quote = 'It\'s a sunny day!'
print(single_quote)
# Output:
# It's a sunny day!

# Double Quote
double_quote = "He said, \"Python is awesome!\""
print(double_quote)
# Output:
# He said, "Python is awesome!"

# ASCII Bell
ascii_bell = "This will make a sound\a (if your system supports it)"
print(ascii_bell)
# Output:
# This will make a sound (if your system supports it)
# Note: The \a may not produce an audible bell on all systems.

# ASCII Backspace
ascii_backspace = "Hello\bWorld!"
print(ascii_backspace)
# Output:
# HellWorld!
# Note: The \b backspace character removes the character before it.

# ASCII Formfeed
ascii_formfeed = "Hello,\fWorld!"
print(ascii_formfeed)
# Output:
# Hello,
#       World!
# Note: The \f form feed character may not be visible in all output devices.

# ASCII Linefeed
ascii_linefeed = "Hello,\nWorld!"
print(ascii_linefeed)
# Output:
# Hello,
# World!

# ASCII Carriage Return
ascii_carriage_return = "Hello,\rWorld!"
print(ascii_carriage_return)
# Output:
# World!
# Note: The \r carriage return character moves the cursor to the beginning of the line.

# ASCII Horizontal Tab
ascii_horizontal_tab = "Hello,\tWorld!"
print(ascii_horizontal_tab)
# Output:
# Hello,  World!
# Note: The \t horizontal tab character adds a tab space.

# ASCII Vertical Tab
ascii_vertical_tab = "Hello,\vWorld!"
print(ascii_vertical_tab)
# Output:
# Hello,
#       World!
# Note: The \v vertical tab character may not be visible in all output devices.

# Character with octal value
octal_value = "\101\102\103"
print(octal_value)
# Output:
# ABC
# Note: \101, \102, \103 are octal representations of 'A', 'B', 'C' respectively.

# Character with hex value
hex_value = "\x41\x42\x43"
print(hex_value)
# Output:
# ABC
# Note: \x41, \x42, \x43 are hex representations of 'A', 'B', 'C' respectively.

# Unicode Character
unicode_char = "\u0041\u0042\u0043"
print(unicode_char)
# Output:
# ABC
# Note: \u0041, \u0042, \u0043 are Unicode representations of 'A', 'B', 'C' respectively.

# 32-bit Unicode Character
unicode_32bit_char = "\U00000041\U00000042\U00000043"
print(unicode_32bit_char)
# Output:
# ABC
# Note: \U00000041, \U00000042, \U00000043 are 32-bit Unicode representations of 'A', 'B', 'C' respectively.

# Raw String
raw_string = r"This is a raw string, no escape sequences will be processed: \n \t \\"
print(raw_string)
# Output:
# This is a raw string, no escape sequences will be processed: \n \t \\
