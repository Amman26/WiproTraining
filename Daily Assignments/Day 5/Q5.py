# taking number input and converting to integer
user_input = input("Enter a number: ")
print("Trying to convert...")

try:
    num = int(user_input)
    print("Conversion successful, value is:", num)
except ValueError:
    print("Oops! That was not a valid")