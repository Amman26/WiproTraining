# accessing list element using index
numbers = [10, 20, 30, 40, 50]
print("\nList is:", numbers)

try:
    index = int(input("Enter index to access: "))
    print("Element at index:", numbers[index])
except IndexError:
    print("Invalid index, out of range")