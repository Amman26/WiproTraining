'''3. Write a program that takes a number as input and checks if it is divisible by 5.
Print a message if it is divisible or not.'''

number = int(input('Enter a number: '))
if number % 5 == 0:
  print('Divisible by 5')
else:
  print('Not Divisible by 5')