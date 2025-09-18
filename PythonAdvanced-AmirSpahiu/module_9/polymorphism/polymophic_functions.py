def add (x, y):
    return x + y

def concatenate(x, y):
    return str(x) + str(y)

def operate (operation, x, y):
    return operation (x, y)

result_concatenate = operate(concatenate, "Hello", "World")
result_sum = operate(add, 3, 5)

print("Result of the sum: ", result_sum)
print("Result of the concatenate: ", result_concatenate)
