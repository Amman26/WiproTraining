# creating custom exception
class NegativeNumberError(Exception):
    pass

print("\nChecking for positive number...")

try:
    num = int(input("Enter a positive number: "))

    if num < 0:
        raise NegativeNumberError("Negative number entered!")

    print("Good! You entered:", num)

except NegativeNumberError as e:
    print(e)
