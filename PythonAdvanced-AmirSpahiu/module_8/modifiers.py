#public attributes/methods
class MyClass:
    def __init__(self):
        self.public_variable = "This is a public variable"

my_class = MyClass()

print(my_class.public_variable)

#protected attributes/methods
class MyProtectedClass():
    def __init__(self):
        self._protected_variable = "This is a protected variable"

    def _protected_method(self):
        print("This is a protected method")

my_class1 = MyProtectedClass()
print(my_class1._protected_variable)

print(my_class1._protected_method())

