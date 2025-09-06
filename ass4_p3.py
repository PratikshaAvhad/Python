#Write an anonymous function to find area of circle.

area_circle = lambda r: 3.14 * r * r

radius = float(input("Enter radius of the circle: "))
print("Area of the circle:", area_circle(radius))
