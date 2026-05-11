# demonstrating finally block
print("\nTrying to open sample.txt...")

try:
    file_obj = open("sample.txt", "r")
    print("\nFile content:")
    print(file_obj.read())

except FileNotFoundError:
    print("File not found!")

finally:
    print("Program execution completed (finally block)")