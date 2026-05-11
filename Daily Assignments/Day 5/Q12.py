# function to add two values
def add_values(a, b):
    try:
        print("Sum is:", a + b)
    except TypeError:
        print("Invalid input! Only numbers allowed")

print("\nTesting add function")

add_values(10, 20)      # valid
add_values(10, "abc")   # invalid test

