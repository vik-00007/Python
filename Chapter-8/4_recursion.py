
# When a function call itself

# def fact(n):
#     if fact ==0 or fact == 1:
#      return 1
#     return  n * fact(n - 1)

# n = int(input("Enter a number: "))

# print(f"The factorial is {fact(n)}")


def fact(n):
    if n == 0 or n == 1:  # Correct condition to check if n is 0 or 1
        return 1
    return n * fact(n - 1)  # Recursive call with n - 1

n = int(input("Enter a number: "))
print(f"The factorial is {fact(n)}")
















