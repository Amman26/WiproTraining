# keep asking user until valid division happens
print("\nTry division until correct input is given")

while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 / num2
        print("Final result is:", result)
        break   # exit loop when successful

    except ValueError:
        print("Please enter numbers only")

    except ZeroDivisionError:
        print("Cannot divide by zero, try again")