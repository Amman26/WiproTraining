'''7.Use the Math Module: Write a program that imports the math module and uses it to: 
Find the square root of a number. Calculate the sine of an angle . Find the greatest 
common divisor (GCD) of two numbers '''.

import math
num = float(input("Enter a number for square root: "))
  print("Square root:", math.sqrt(num))

 angle = float(input("Enter angle in radians: "))
  print("Sine:", math.sin(angle))

 n1 = int(input("Enter first number for GCD: "))
 n2 = int(input("Enter second number for GCD: "))
  print("GCD:", math.gcd(n1, n2))