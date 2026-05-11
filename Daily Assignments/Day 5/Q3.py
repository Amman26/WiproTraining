# copying content from source to destination
print("Reading source file...")

with open("source.txt", "r") as src_file:
    data = src_file.read()

print("Writing to destination file...")

with open("destination.txt", "w") as dest_file:
    dest_file.write(data)

print("File copied successfully!")

