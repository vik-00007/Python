
# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "Buy now", "Subscribe this", "Click this."
# Write a program to detect these spams.
c1="Make a lot of money"
c2="buy now"
c3="subscribe this"
c4="cick this"

comment = input("Enter comment: ")

if ((c1 in comment) or (c2==comment) or (c3==comment) or (c4==comment)): #if ((c1 in comment) or (c2 in comment) or (c3 in comment) or (c4 in comment))
    print("Spam message")
else:
    print("Not spam message")
















