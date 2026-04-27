'''12.Create a Package for String Utilities: Create a package called string_utils with two
modules: string_operations.py and string_validations.py. In string_operations.py, define
functions for reversing a string, converting a string to uppercase, and finding the length
of a string. In string_validations.py, define functions to check if a string is a palindrome
and if it contains only alphabetic characters. Write a program that imports and uses
these functions from the string_utils package. '''

#string operations
def reverse_string(s):
 return s [::-1]
def to_uppercase(s):
 return s.upper()
def string_length(s):
 return len(s)
#stringvalid
def is_palindrome(s):
 return s == s[::-1]
def is_alpha(s):
 return s.isalpha()
#stringsmain
from stringoperations import reverse_string, to_uppercase, string_length
from stringvalid import is_alpha, is_palindrome
from Daily_assignments.DAY3.qn6 import is_palindrome
text = "madam"
  print('Original:', text)
  print('Reversed:', reverse_string(text))
  print('Uppercase:', to_uppercase(text))
  print('Length:', string_length(text))
  print('Is Palindrome:', is_palindrome(text))
  print('Is Alphabet Only:', is_alpha(text))