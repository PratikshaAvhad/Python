# write a python program to add and remove operation on set.
a={33,43,78,55,99}
print(a)
a.add(100)
print(a)
a.remove(100)
print(a)

print("--------------------------------------------------------------------------------")

# write a python program to do iteration over sets.
a={21,10,3,5,96}
for num in a:
    print(num)

print("--------------------------------------------------------------------------------")    

# write a python program to find the length of a set.     
p={"pratu","prachi","ramu","shweta"}
print("lenght of set=",len(p))

print("--------------------------------------------------------------------------------")

# write a python program to creat a tuple with numbers and print one item.
s=(11,3,22,66,55)
print(s)

print("--------------------------------------------------------------------------------")

# write a python script to add a key to a dictionary.
#simple dictionary:{0:10,1:20}
#Expected dictionary:{0:10,1:20,2:30}
a={0:10,1:20}
a[2]=30
print(a)
print("--------------------------------------------------------------------------------")

# write a python program to create an intersection of sets.

a={32,44,55,76,88}
b={44,63,22,41}
c=a&b
c=a.intersection(b)
print(c)
print("--------------------------------------------------------------------------------")

# write a python program to create a union of sets.
a={32,44,55,76,88}
b={44,63,22,41}
c=a|b
c=a.union(b)
print(c)
print("--------------------------------------------------------------------------------")

# write a python script to check if a given key already in a dictionary.
s={"p","php","j","java","c","cpp","py","python"}
a=input("enter key")
if a in s:
    print("key found")
else:
    print("key not found")
print("--------------------------------------------------------------------------------")

# write a python program to find maximun and minimum value in a set.
a={"pratu","tanuja","neha","sayali"}
print(min(a))
print(max(a))
print("--------------------------------------------------------------------------------")

# write apython prigram to add an item in a tuple.
s=(22,33,55,11)
print(s)
s=list(s)
s[2]=99
s=tuple(s)
print(s)
print("--------------------------------------------------------------------------------")

# write a python program to convert a tuple to a string.
s=("p","r","a","t","u")
s1=''.join(s)
print(s1)
print("--------------------------------------------------------------------------------")

# write apython program to creat an intersectionn of sets.
a={11,22,44,33,55}
b={55,33,77,88,99}
c=a&b
c=a.intersection(b)
print(c)
print("--------------------------------------------------------------------------------")

# write a python program to create a union of sets.
a={32,44,55,76,88}
b={44,63,22,41}
c=a|b
c=a.union(b)
print(c)
print("--------------------------------------------------------------------------------")

#write a python program to create set difference and a symmetric.
a={3,2,5,4,7,8}
b={43,55,3,22,11}
d1=a-b
d2=a^b
print("first set=",a)
print("second set=",b)
print("difference=",d1)
print("symmetric diff=",d2)
print("--------------------------------------------------------------------------------")

#write a python program to create a list of a tuples with the first as the number and second
#element as the square of the nnumber
n=input("enter number")
a=[2,4,6,7,5,3,9]
b=list((n,n*n)for n in a)
print(b)
print("--------------------------------------------------------------------------------")

# write a python program to unpack a tuple in several variables.
s=("pratiksha",20,"BCA")
name,age,course=s
print("name=",name)
print("age=",age)
print("course=",course)
print("--------------------------------------------------------------------------------")

#write a pythopn program to get the 4th element from front and
#4th element from last of the tuple
a=(10,33,22,99,44,55,100,77)
if len(a)>=4:
    f=a[3]
    fe=a[-4]
    print("4th element from front=",f)
    print("4th element from end=",fe)
else:
    print("not found")
print("--------------------------------------------------------------------------------")

#write a python program to find the repeated iteam of a tuple.
a=(21,32,55,66,11,33,11,55)
t=set([r for r in a if a.count(r)>1])
print("Repeated iteams=")
print(t)
print("--------------------------------------------------------------------------------")

# write a python program to check whether an element exists within
a=(22,43,54,86,57)
n=int(input("enter no to search"))
if n in a:
    print("number found")
else:
    print("number not found")
print("--------------------------------------------------------------------------------")

#write a python program to print calender of specific month of input year using calender module
import calendar
import datetime
year=input("enter year")
month=input("enter month")
print(calendar.month(year,month))
print("--------------------------------------------------------------------------------")

#write an anonymous function to find area of circle
area=lambda r:3.14*r*r
print("area of circle=",area(2))
      

































    



    
    
    




