
#string is a data type in python
#String is a sequence of character enclosed in quotes.
#We can primarily write a string in these three ways.

a='Souvik'
b="Souvik"
c= '''Souvik'''
print(a,b,c)

#STRING SLICING
#A string in python can be sliced for getting a part of the strings.

# sl=name[ind_start:ind_end]
 
name = "souvik"
s=name[0:3]
r=name[1:3]
print(s,r)
print(name[-6])#name[-6]==name[1]
print(name[-1]) # nmae[-1]==name[6]

#Slicing with skip value
#We can provide a skip value as a part of our slice 

word="amazing"

w=word[1:6:2]
x=word[:7]
y=word[0:]
print(w, x, y)




















