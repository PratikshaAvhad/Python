#Write a python class to accept a string and number n from user and display n 
#repetition of strings using by overloading * operator.

class MyString:
    def __init__(self, text):
        self.text = text

    
    def __mul__(self, n):
        if isinstance(n, int):   
            return self.text * n
        else:
            return "Multiplication only allowed with integers."



s = input("Enter a string: ")
n = int(input("Enter a number: "))

mystr = MyString(s)
result = mystr * n    

print("Result:", result)
