#class Superclass:
    #Superclass attributes and methods

#class Subclass(Superclass):
    #Subclass attributes and methods

class Animal:
    def eat(self):
        print("It eats")
    def sleep(self):
        print("It sleeps")

class Bird(Animal):
    def fly(self):
        print("It flies...")
    def sting(self):
        print("It stings")