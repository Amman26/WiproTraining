# reading file to count details
print("Opening sample.txt...")

with open("sample.txt", "r") as file_obj:
    content = file_obj.read()

print("Calculating details...")

lines = content.split("\n")
words = content.split()
chars = len(content)

print("\nFile Analysis:")
print("Total Lines:", len(lines))
print("Total Words:", len(words))
print("Total Characters:", chars)
