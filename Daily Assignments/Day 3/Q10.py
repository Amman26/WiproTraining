'''10.Use the OS Module: Write a program that imports the os module and uses it to: 
Print the current working directory Create a new directory and verify its existence. List 
all files and directories in the current directory''' .

import os
#print working directory
print(os.getcwd())
#create new directory
os.mkdir('new_folders')
#checking
print(os.path.exists('new_folders'))
#list directory
print(os.listdir())
import os
#print working directory
print(os.getcwd())
#create new directory
os.mkdir('new_folders')
#checking
print(os.path.exists('new_folders'))
#list directory
print(os.listdir())