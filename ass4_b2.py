#Write python script using package to calculate area and volume of cylinder and cuboids.

import math

def cylinder_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def cuboid_area(length, width, height):
    return 2 * (length*width + width*height + height*length)

def cuboid_volume(length, width, height):
    return length * width * height


r = float(input("Enter radius of cylinder: "))
h = float(input("Enter height of cylinder: "))
print("Cylinder Area:", cylinder_area(r, h))
print("Cylinder Volume:", cylinder_volume(r, h))

l = float(input("\nEnter length of cuboid: "))
w = float(input("Enter width of cuboid: "))
h = float(input("Enter height of cuboid: "))
print("Cuboid Area:", cuboid_area(l, w, h))
print("Cuboid Volume:", cuboid_volume(l, w, h))
