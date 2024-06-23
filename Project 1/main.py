
import random

'''
1 for stone
-1 for scissor
0 for paper

'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choice (s-->Stone, p-->Paper, c--> Scissor): ")
youDict = {"s":1,"p":0,"c":-1}
reverseDict = {1:"Stone", 0:"Paper",-1:"Scissor"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer==you):
    print("Draw")
else:
    if(computer==1 and you==-1):
        print("You lose")

    elif(computer==1 and you==0):
        print("You win")
    
    
    elif(computer==-1 and you==0):
        print("You lose")
    
    elif(computer==-1 and you==1):
        print("You win")

    elif(computer==0 and you==1):
        print("You lose")
    
    elif(computer==0 and you==-1):
        print("You win")
    
    else:
        print("Something Wrong")










