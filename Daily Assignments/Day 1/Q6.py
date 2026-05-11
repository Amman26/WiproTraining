'''6. Write a program that takes a grade (A, B, C, D, F) as input and uses match-case
to print a message corresponding to the grade (e.g., "Excellent" for A, "Good" for
B, etc.).'''

marks = (input('Enter the Grade: '))
match marks:
  case 'A':
   print('Excellent')
  case 'B':
   print('Good')
  case 'C':
   print('Average')
  case 'D':
   print('Below Average')
  case 'F':
   print('Fail')
  case _:
   print('Invalid Grade')