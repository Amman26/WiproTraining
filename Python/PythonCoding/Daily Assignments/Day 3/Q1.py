'''1.Do the following in a single program using built-in functions Take a list of numbers as
input and print the largest and smallest numbers in the list. Take a string as input and
print the length of the string. Take a list of names as input and print the list in
alphabetical order. Take a list of numbers as input and print the total sum of the
elements in the list. Takes a string as input and print the string in uppercase.'''

# Take numbers as input for largest and smallest
user_nums = input("Enter numbers separated by spaces: ")
# Convert the input string into a list of integers
nums = [int(x) for x in user_nums.split()]
print("Largest number:", max(nums))
print("Smallest number:", min(nums))
# Take string as input for length
text = input("\nEnter a string: ")
print("Length of string:", len(text))
# Take names as input for alphabetical sorting
user_names = input("\nEnter names separated by spaces: ")
names = user_names.split()
print("Sorted names:", sorted(names))
# Take numbers as input for total sum
user_sum_nums = input("\nEnter numbers to sum, separated by spaces: ")
nums_to_sum = [int(x) for x in user_sum_nums.split()]
print("Sum of list:", sum(nums_to_sum))
# Take string as input for uppercase
upper_text = input("\nEnter a string to cap: ")
print("Uppercase:", upper_text.upper())