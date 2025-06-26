try:
    result = 10/0

except ZeroDivisionError:
    print("You can't divide by zero")

# Example 2
fruits = {"apple":5, "banana":7, "orange": 3}

try:
    print(fruits["cherry"])
except KeyError:
    print("The key does not exist in the dictionary")

# Example 3
text = "This is not a number"

try:
    text_to_int = int(text)
except Exception as e:
    print("An error occured while parsing the data: ", e)

# Example 4
try:
    result = 10/2
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print("Division successfully. Result:", result)

# Example 5
try:
    result = 10/0
except ZeroDivisionError:
    print("You can't divide by zero")
finally:
    print("Finally block executed")

# Example 6
def divide_numbers(a,b):
    try:
        result = a/b
        print("Result of division: ",result)
    except ZeroDivisionError:
        print("You can't divide by zero")
    except TypeError:
        print("Invalid type for division")
    except Exception as e:
        print(f"Unexpected error:{e}")

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, '2')








