# BMI APP
# - Program using OOP, calculation on user input
# - Prompt user name, age, weight/kg, height/meters
# - Seperate classes for Adults and Child, inheriting from base class Person
# - Base class Person: calculate_bmi(), get_pmi_category(), print_info()
# - @property decorator te encapsulate weight and height attributes in the Person class
# - BMI = weightkg/heightm2 (adults) & BMI = weightkg/heightm2 *1.3 (kids)
# - BMIApp class: add_person(person), collect_user_data(), print_results(), run()
# - Underweight (below 18.5), Healthy Weight (18.5-24.9), Overweight (25.0-29.9), and Obesity
# (30.0 or greater)

class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be greater than zero")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be greater than zero")
        self._height = value

    def bmi(self):
        return self.weight / (self.height ** 2)

    def bmi_category(self):
        bmi = self.bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Healthy Weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

    def display(self):
        print(f"{self.name} (Age: {self.age} - BMI: {self.bmi():2f} {self.bmi_category()})")

class Adult(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)

class Child(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)

class BMIApp:
    def __init__(self):
        self.records = []
    def input_person(self):
        name = input("Name: ")
        age = int(input("Age: "))
        weight = float(input("Weight (kg): "))
        height = float(input("Height (m): "))
        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name, age, weight, height)
            self.records.append(person)

    def show_results(self):
        print("\nBMI Results: ")
        for person in self.records:
            person.display()

    def run(self):
        while True:
            self.input_person()
            if input("Add another person? (y/n): ").strip().lower() != "y":
                break
            self.show_results()

if __name__ == "__main__":
    BMIApp().run()







