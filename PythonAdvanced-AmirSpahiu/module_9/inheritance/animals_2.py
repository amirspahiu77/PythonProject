class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some generic animal sound.")

    def descrription(self):
        print(f"This is an animal named {self.name}.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Woof! Woof!")

    def descrription(self):
        super().descrription()
        print(f"Breed: {self.breed}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Mew! Meow!")

    def description(self):
        super().descrription()
        print(f"Color: {self.color}")

#Example usage:
animal = Animal("Generic Animal")
animal.sound()
animal.descrription()

dog = Dog("Rex", "Golden Retriever")
dog.sound()
dog.descrription()

cat = Cat("Whiskers", "Black")
cat.sound()
cat.description()