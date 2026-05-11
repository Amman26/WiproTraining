# appending new text to log file
new_text = input("Enter text to add in log file: ")
print("Adding text to log.txt...")

with open("log.txt", "a") as file_obj:
    file_obj.write(new_text + "\n")

print("\nUpdated log file content:")

with open("log.txt", "r") as file_obj:
    print(file_obj.read())
