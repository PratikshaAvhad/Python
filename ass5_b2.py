#Write a function named pt_in_circle that takes a circle and a point and returns
#true if point lies on the boundry of circle.

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


def pt_in_circle(circle, point):
    # Distance between point and center
    distance = math.sqrt((point.x - circle.center.x)**2 + (point.y - circle.center.y)**2)
    # Check if distance == radius 
    return math.isclose(distance, circle.radius)


x_c = float(input("Enter circle center x: "))
y_c = float(input("Enter circle center y: "))
r = float(input("Enter circle radius: "))

x_p = float(input("Enter point x: "))
y_p = float(input("Enter point y: "))

center = Point(x_c, y_c)
circle = Circle(center, r)
point = Point(x_p, y_p)

if pt_in_circle(circle, point):
    print("Point lies on the boundary of the circle.")
else:
    print("Point does NOT lie on the boundary of the circle.")
