'''5.Combining Built-in and User-Defined Functions: Find the Average of a List: Write a
user-defined function average(numbers) that takes a list of numbers as an argument
and returns the average of the numbers. Call the function with a list of numbers and
print the average.'''

def average(numbers):
  return sum(numbers) / len(numbers)
num_str = input("Enter numbers separated by spaces: ").split()
nums = [float(x) for x in num_str]
print("Average is:", average(nums))