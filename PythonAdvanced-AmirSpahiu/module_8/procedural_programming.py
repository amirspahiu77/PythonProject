def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return (length + width) * 2

length = 5
width = 3

area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")