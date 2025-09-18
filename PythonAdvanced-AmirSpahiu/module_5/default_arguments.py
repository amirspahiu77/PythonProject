def greet_person(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message

default_greeting = greet_person("Alice")

custom_greeting = greet_person("Bob", "Hi")

print(default_greeting)
print(custom_greeting)