'''11. Write a program that uses a for loop to count the number of vowels in a given
string. Print the count.'''

str = input('Enter :')
 count = 0

  for ch in str:
   if ch in 'a,e,i,o,u':
 count+=1

     print(count)