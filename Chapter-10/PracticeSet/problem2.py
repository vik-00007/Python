# Write a class "claculator" capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The square root is {self.n**1/2}")



a = Calculator(4)
a.square()
a.cube()
a.squareroot()







