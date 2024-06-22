
# write a python function to print first n lines of the following pattern:
# ***
# **
# *      - for n=3

def pattern(n):
    for i in range(n,0,-1):
        print("*"*i,)

     
n = int(input("Enter row num: "))
pattern(n)

# Using recursion
def pattern(n):
    if n > 0:
        print("*" * n)
        pattern(n - 1)

n = int(input("Enter row num: "))
pattern(n)













