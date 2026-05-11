# division with error handling
print("\nLet's perform division")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result is:", result)

except ValueError:
    print("Please enter valid numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero, try again")
