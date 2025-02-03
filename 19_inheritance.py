# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Derived class (Inheritance)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def student_info(self):
        return f"Student ID: {self.student_id}"

# Creating an instance of Student
s = Student("Bob", 22, "S1234")

# Using inherited and own methods
print(s.greet())  # Using method from Person class
print(s.student_info())  # Using method from Student class
