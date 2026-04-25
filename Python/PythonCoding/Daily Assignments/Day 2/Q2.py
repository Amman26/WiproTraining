'''2. Do the following in sequence and record the results in a single program
Create a tuple with the names of 3 different cities you’d like to visit. Print the tuple.:
Access and print the first and last elements of the tuple.:
Create another tuple with 2 more cities. Concatenate both tuples and print the result.
Try changing one element of the tuple. What happens?
Unpack the elements of the tuple into separate variables and print them.'''

# Create tuple of 3 cities
cities = ("Delhi", "Mumbai", "Chennai")
print("Cities tuple:", cities)
# Access first and last
print("First city:", cities[0])
print("Last city:", cities[-1])
# Create another tuple and concatenate
more_cities = ("Kolkata", "Bengaluru")
all_cities = cities + more_cities
print("All cities:", all_cities)
# Try changing one element
# Unpack elements
c1, c2, c3 = cities
print("Unpacked cities:", c1, c2, c3)