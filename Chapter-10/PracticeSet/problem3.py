
# # Create a class with a class attribute a, create an object from it and set 'a
# directly using object a=o. Does this change the class attribute?

class Demo:
    a = 5

o = Demo()
print(o.a)

o.a = 0
print(o.a)




