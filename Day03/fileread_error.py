file_name = input("Input the file name (XXX.txt):")

try:
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")


