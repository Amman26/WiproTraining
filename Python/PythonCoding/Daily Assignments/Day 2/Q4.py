'''4. Do the following in sequence and record the results in a single program
Create a dictionary with your name, age, and favorite hobby as keys, and provide
appropriate values. Print the dictionary.
Access and print the value associated with your name in the dictionary.
Add a new key-value pair for your favorite food, then update the value for your favorite
hobby. Print the updated dictionary.
Print all the keys and all the values in the dictionary separately.
Remove the age key-value pair from the dictionary. Print the dictionary to see the
change.'''

# Create dictionary
my_info = {"name": "Amman", "age": 23, "hobby": "gaming"}
print("Dictionary:", my_info)

# Access value of name
print("Name is:", my_info["name"])

# Add food, update hobby
my_info["food"] = "paneer butter masala"
my_info["hobby"] = "coding"
print("Updated dictionary:", my_info)

# Print keys and values separately
print("Keys:", my_info.keys())
print("Values:", my_info.values())

# Remove age
del my_info["age"]
print("After removing age:", my_info)