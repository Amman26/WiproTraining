# taking input from user
user_text = input("Enter some text: ")
print("Saving your text to file...")

# writing into file (will create file if not exists)
with open("output.txt", "w") as file_obj:
    file_obj.write(user_text)

print("File saved successfully!")
print("\nNow reading the file...")

# reading from file
with open("output.txt", "r") as file_obj:
    content = file_obj.read()

print("\nFile content is:")
print(content)
