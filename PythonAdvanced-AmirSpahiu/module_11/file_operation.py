# Open a file in 'read' mode
# file_path = "example.txt"
# file = open(file_path, "r")

# #Read the contents of the file
# content = file.read()
# print(content)
#
# #Close the file
# file.close()

file_path = "example.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)

# File Modes
# 'r': Read
# 'w': Write
# 'a': Append
# 'b': Binary mode
# 'x': Exclusive creation
import os

file_path = "example.txt"
with open(file_path, 'r') as file:
    content = file.read()
    line = file.readline()
    lines = file.readlines()

    print(content)
    print(line)
    print(lines)

# Writing to Files
with open('example.txt', 'w') as file:
    file.write('Welcome to Digital School')

lines = ["Hello, World!\n", 'Welcome to Python!\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)

# Moving the Cursor
with open("example.txt", 'r') as file:
    file.seek(0)
    data = file.read()
    print(data)

if os.path.exists("example.txt"):
    print("File exists!")

# Appending data
with open("example.txt", "a") as file:
    file.write("New data appended")

# Reading/Writting Binary Files
data = b'Ts is some binary data'
with open("example.bin", "wb") as file:
    file.write(data)

with open("binary_file.bin", "rb") as binary_file:
    data = binary_file.read()













