# Encapsulation, Inheritance, and Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclasses must implement speak method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Using polymorphism
animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")
