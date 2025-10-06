#Write a Python program that defines a class named circle with attributes radius 
#and center, where center is a point object and radius is number. Accept center and 
#radius from user. Instantiate a circle object that represents a circle with its center and radius as accepted input.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Circle:
    def __init__(self, center, radius):
        self.center = center  
        self.radius = radius  

    def __str__(self):
        return f"Circle with center at {self.center} and radius {self.radius}"


x = float(input("Enter x-coordinate of the center: "))
y = float(input("Enter y-coordinate of the center: "))
r = float(input("Enter the radius of the circle: "))

center_point = Point(x, y)
circle_obj = Circle(center_point, r)

print(circle_obj)
