#Define a class named Rectangle which can be constructed by a length and width.
#The Rectangle class has a method which can compute the area and volume.

class Rectangle:
    def __init__(self, length, width, height=None):
        self.length = length
        self.width = width
        self.height = height  

    def area(self):
        return self.length * self.width

    def volume(self):
        if self.height is not None:
            return self.length * self.width * self.height
        else:
            return "Height not provided, volume cannot be calculated."


l = float(input("Enter length: "))
w = float(input("Enter width: "))
h = input("Enter height (press Enter if not needed): ")

if h.strip() == "":
    rect = Rectangle(l, w)
else:
    rect = Rectangle(l, w, float(h))

print("Area:", rect.area())
print("Volume:", rect.volume())
