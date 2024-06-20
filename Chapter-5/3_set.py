

e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5} 
#Output--> {32, 1, 5, 54}  *Set terms don't repeat

print(s)

a = {1, 5, 32, 54,5, 5, 5, "Harry"}

print(s, type(a))

s.add(566)
print(s, type(a))
s.remove(1)
print(s, type(a))

s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))













