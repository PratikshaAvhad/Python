#Write a Python Program to Accept, Delete and Display students details such as 
#Roll.No, Name, Marks in three subject, using Classes. Also display percentage of each student.

class Student:
    def __init__(self, roll_no, name, m1, m2, m3):
        self.roll_no = roll_no
        self.name = name
        self.marks = [m1, m2, m3]
    
    def percentage(self):
        return sum(self.marks) / 3
    
    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, "
              f"Marks: {self.marks}, Percentage: {self.percentage():.2f}%")

students = [] 

while True:
    print("\n1. Add Student")
    print("2. Delete Student")
    print("3. Display Students")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        r = int(input("Enter Roll No: "))
        n = input("Enter Name: ")
        m1 = int(input("Enter Marks in Subject 1: "))
        m2 = int(input("Enter Marks in Subject 2: "))
        m3 = int(input("Enter Marks in Subject 3: "))
        students.append(Student(r, n, m1, m2, m3))
        print("Student Added!")

    elif choice == 2:
        r = int(input("Enter Roll No to delete: "))
        found = False
        for s in students:
            if s.roll_no == r:
                students.remove(s)
                print("Student Deleted!")
                found = True
                break
        if not found:
            print("Student not found!")

    elif choice == 3:
        if not students:
            print("No students available!")
        else:
            print("\n--- Student Records ---")
            for s in students:
                s.display()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
