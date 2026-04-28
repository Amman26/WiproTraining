# opening file entered by user
file_name = input("\nEnter file name to read: ")

print("Opening file...")

try:
    with open(file_name, "r") as file_obj:
        print("\nFile content:")
        print(file_obj.read())
except FileNotFoundError:
    print("File not found, please check the name")
