'''1.Do the following in sequence and record the results in a single program
Create a list with 5 different types of fruits. Print the list.
Add two more fruits to the list, then remove one fruit from it. Print the updated list.
Access the second and fourth fruits in the list. Print them.
Slice the list to get the first three fruits and print the result.
Find and print the length of your list.'''

# Create list of 5 fruits
fruits = ["apple", "banana", "mango", "orange", "grapes"]
print("Original list:", fruits)
# Add two, remove one
fruits.append("pineapple")
fruits.append("watermelon")
fruits.remove("banana")
print("Updated list:", fruits)
# Access second and fourth
print("Second fruit:", fruits[1])
print("Fourth fruit:", fruits[3])
# Slice first three
first_three = fruits[0:3]
print("First three fruits:", first_three)
# Find length
print("Length of list:", len(fruits))