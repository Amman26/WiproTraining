'''3.Write a user-defined function "find_largest(a, b, c)" that takes three numbers as
arguments and returns the largest of the three. Use the function in a program to find
and print the largest of three given numbers.'''

def find_largest(a, b, c):

   return max(a, b, c)
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
print("Largest number is:", find_largest(n1, n2, n3))