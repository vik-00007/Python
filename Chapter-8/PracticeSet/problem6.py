
# Write a python function which converts inches to cms.


def inches_to_cm(inches):
    cm = inches * 2.54
    return cm

# Example usage
inches = float(input("Enter value in inches: "))
centimeters = inches_to_cm(inches)
print(f"{inches} inches is equal to {centimeters} centimeters.")











