#Write a python script using function to calculate  XY

def power(x, y):
    return x ** y

x = float(input("Enter value of X: "))
y = int(input("Enter value of Y: "))

print(f"{x} raised to the power {y} is: {power(x, y)}")
