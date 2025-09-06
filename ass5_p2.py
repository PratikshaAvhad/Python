#Write a python program for Counting the number of students using more objects of a class.

class Student:
    count = 0  
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1  

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("pratu", 20)
s2 = Student("prachi", 21)
s3 = Student("ramu", 19)

s1.display()
s2.display()
s3.display()


print("\nTotal number of students:", Student.count)
