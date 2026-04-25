'''2. Write a program that takes a year as input and checks if it is a leap year or not.
Print the result.'''

year = int(input('Enter the year : '))
if year % 400 == 0:
  print('It is a Leap Year')
elif year % 100 == 0:
  print('It is Not a Leap Year')
elif year % 4 == 0:
  print('It is a Leap Year')
else:
  print('It is a Not Leap Year ')