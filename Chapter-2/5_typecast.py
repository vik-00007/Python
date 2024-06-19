
a = "31.2"
b = float(a) # a but the type should be float
t = type(b) 

print(t)





# Typecasting from one type to another

# Integer to float
x = 10
y = float(x)
print(f"Integer {x} converted to float: {y}")

# Float to integer
a = 5.7
b = int(a)
print(f"Float {a} converted to integer: {b}")

# Integer to string
num = 123
str_num = str(num)
print(f"Integer {num} converted to string: '{str_num}'")

# String to integer
str_num = "456"
num = int(str_num)
print(f"String '{str_num}' converted to integer: {num}")

# String to float
str_float = "3.14"
float_num = float(str_float)
print(f"String '{str_float}' converted to float: {float_num}")

# Boolean to integer
bool_var = True
int_var = int(bool_var)
print(f"Boolean {bool_var} converted to integer: {int_var}")

# Integer to boolean
num = 0
bool_var = bool(num)
print(f"Integer {num} converted to boolean: {bool_var}")

# NoneType to integer (results in ValueError)
# none_var = None
# int_var = int(none_var)
# print(f"NoneType {none_var} converted to integer: {int_var}")
