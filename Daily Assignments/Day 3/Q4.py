'''4.Write a user-defined function greet(name) that takes a name as an argument and
prints a greeting message like "Hello, [name]!" Use the function to greet the user with
their name.'''

def greet(name):
 print("Hello, " + name + "!")
user_name = input("Enter your name: ")
greet(user_name)