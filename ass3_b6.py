#Write a Python program to check whether an element exists within a tuple.

a=(22,43,54,86,57)
n=int(input("enter no to search"))
if n in a:
    print("number found")
else:
    print("number not found")
