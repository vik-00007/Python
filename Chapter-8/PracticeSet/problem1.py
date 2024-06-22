
# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    


a = int(input("Enter num1: "))
b = int(input("Enter num1: "))
c = int(input("Enter num1: "))
print(f"{greatest(a,b,c)} is greatest")

    



















