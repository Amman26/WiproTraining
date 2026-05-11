'''11.Create and Use a Custom Package: Create a package called my_math with two 
modules: arithmetic.py and geometry.py. In arithmetic.py, define functions for addition, 
subtraction, multiplication, and division. In geometry.py, define functions to calculate 
the area of a circle and the area of a rectangle. Write a program that imports these 
functions from the my_math package and uses them to perform various calculations'''.

#arithmetic.py
def add(a,b):

 return a+b
def subtract(a,b):

 return a- b
def multiply(a,b):

 return a*b
def divide(a, b):

 return a / b
#geometry.py
def circle_area(radius):

 return 3.14*radius*radius
def rectangle_area(length, width):

 return length * width
#main operations
from operator import add
from arithmetic  import subtract, multiply,divide
from geometry import circle_area,rectangle_area
#arimetic operations
print('Addition:', add(10, 5))
print('Subtraction:', subtract(10,5))
print('Multiplication:', multiply(10, 5))
print('Division:', divide(10, 5))
#Geometry calculations
print('Circle Area:', circle_area(7))
print('Rectangle Area:', rectangle_area(4, 6))