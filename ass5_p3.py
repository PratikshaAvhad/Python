#Write a python program for parameterized constructor has multiple parameters along 
#with the self Keyword.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

s1 = Student("pratiksha", 20, "A")
s2 = Student("neha", 21, "B")


s1.display()
s2.display()
