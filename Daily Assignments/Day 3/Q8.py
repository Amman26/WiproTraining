'''8.Use the Random Module: Write a program that imports the random module and uses
it to: Generate and print a random integer between 1 and 100. Create a list of random
numbers and print the list. Shuffle a list of numbers and print the shuffled list.'''

import random
 print("Random integer 1-100:", random.randint(1, 100))
# Create and print list of 5 random numbers
  rand_list = []
for i in range(5):
  rand_list.append(random.randint(1, 50))
 print("List of random numbers:", rand_list)
# Shuffle list
my_list = [10, 20, 30, 40, 50]
random.shuffle(my_list)
 print("Shuffled list:", my_list)