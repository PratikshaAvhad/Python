#Write a Python program to find the repeated items of a tuple.

a=(21,32,55,66,11,33,11,55)
t=set([r for r in a if a.count(r)>1])
print("Repeated iteams=")
print(t)
