# keep asking user until valid integer is entered
print("\nPlease Enter a valid integer")

while True:
    try:
        user_num = int(input("Enter integer: "))
        print("You entered:", user_num)
        break

    except ValueError:
        print("Not an integer, try again")