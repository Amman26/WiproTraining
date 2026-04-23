#count how many times 'a' apperas using enumerate

text = input('Enter a String')
count = 0
for i, char in enumerate(text):
    if char == 'a':
        count += 1
print("Count of 'a' :", count)