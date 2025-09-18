from module_8.procedural_programming import perimeter


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle(2, 5)

area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")


#Example 2
class Student:
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage

    def show(self):
        print("Name is", self.name, "and Percentage is: ", self.percentage)

stud = Student("Jessa", 80)
stud.show()

#Example3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name}, and I am {self.age} years old")

person1 = Person("Alice", 15)
person2 = Person("Bob", 17)

person1.greet()
person2.greet()


#Class Variables & Instance Variables
class Student:
    school_name = "Digital School" #this is a class variable

    def __init__(self, name, age, course):
        #Initialize instance variables (attribute) for name, age and course
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Alice", 15, "Python")
student2 = Student("Bob", 16, "JavaScript")
print(student1.school_name)

print(student1.course)
print(student2.course)

