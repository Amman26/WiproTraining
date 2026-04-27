'''2.Write a user-defined function factorial(n) that takes a positive integer n as an
argument and returns its factorial. Use the function in a program and print the factorial
of a given number.'''

# User-defined function
def factorial(n):
  ans = 1
  for i in range(1, n + 1):
   ans = ans * i

  return ans
# Taking input
num = int(input("Enter a positive number: "))
# Call the function and print the result
print("The factorial is:", factorial(num))