
# Create a class "programmer" for storing information of new programmers working at microsoft

class Programmer:
    company = " Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary= salary
        self.pin = pin
        pass

p =  Programmer("Souvik",2000000,743503)

print(p.name,p.salary,p.pin)

s = Programmer("Sneha",1200000,740001)

print(s.name,s.salary,s.pin)








