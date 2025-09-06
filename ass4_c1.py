#Write a program to illustrate function duck typing.

def make_it_speak(animal):
    animal.speak()


class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")


d = Dog()
c = Cat()

make_it_speak(d)  
make_it_speak(c)  
