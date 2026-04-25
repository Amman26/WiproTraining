'''3. Do the following in sequence and record the results in a single program
Create a set of 5 unique colors. Print the set.
Add a new color to the set, then try removing an existing color. Print the updated set.
Create another set with 3 different colors. Find the intersection, union, and difference
between both sets.
Check if a specific color is in the set and print the result.
Convert a list of fruits (with some duplicates) into a set and print the unique fruits.'''

# Create a set of 5 colors
colors = {"red", "blue", "green", "yellow", "black"}
print("Original set:", colors)
# Add one, remove one
colors.add("white")
colors.remove("blue")
print("Updated set:", colors)
# Set operations
other_colors = {"green", "purple", "orange"}
print("Intersection:", colors.intersection(other_colors))
print("Union:", colors.union(other_colors))
print("Difference:", colors.difference(other_colors))
# Check if color is in set
print("Is red in colors?", "red" in colors)
# List with duplicates to set
fruit_list = ["apple", "apple", "banana", "kiwi", "banana"]
unique_fruits = set(fruit_list)
print("Unique fruits:", unique_fruits)