# Write Python class to perform addition of two complex numbers using binary  + operator overloading.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


print("Enter first complex number:")
r1 = float(input("Real part: "))
i1 = float(input("Imaginary part: "))

print("Enter second complex number:")
r2 = float(input("Real part: "))
i2 = float(input("Imaginary part: "))

c1 = Complex(r1, i1)
c2 = Complex(r2, i2)

c3 = c1 + c2   

print("Result of addition:", c3)
