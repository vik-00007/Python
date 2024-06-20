
#Write a program to calculate the grade of a student from his marks

marks=int(input("Enter your marks: "))
if(marks>=90 and 100>=marks):
    grade="Excellent"
elif(marks>=80):
    grade="A"
elif(marks>=70):
    grade="B"
elif(marks>=60):
    grade="c"
elif(marks>=40):
    grade="D"
else:
    grade="F" 

print("Your grade is:", grade)

















