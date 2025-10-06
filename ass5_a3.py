
#Write a Python class which has two methods get_String and print_String. 
#get_String accept a string from the user and print_String print the string in upper 
#case. Further modify the program to reverse a string word by word and print it in lower case.

class StringClass:
    def __init__(self):
        self.my_string = ""

    
    def get_String(self):
        self.my_string = input("Enter a string: ")

   
    def print_String(self):
        print("Uppercase:", self.my_string.upper())

    
    def reverse_and_lower(self):
        words = self.my_string.split()        
        reversed_words = words[::-1]          
        result = " ".join(reversed_words)     
        print("Reversed Lowercase:", result.lower())



obj = StringClass()
obj.get_String()
obj.print_String()
obj.reverse_and_lower()
