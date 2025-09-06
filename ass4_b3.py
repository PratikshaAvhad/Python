#Write a python script to accept decimal number and convert it to binary and octal number using 
#function

def convert(num):
    print("Binary:", bin(num))
    print("Octal :", oct(num))

n = int(input("Enter a decimal number: "))
convert(n)
