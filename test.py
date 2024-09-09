# Write algorithm first
# 1. Read input files from user
# 2. for loop, folder -> list files
# 3. Identify module 
# 4. Print file
# 5. Handle every known error

# number = input("Please provide a number")
# print(number)

import os

# Ask user to provide folder names with spaces
# convert the string to list using split()
folder_paths = input("Please input folder names here seperated by space").split()

# Exception handling
    

# Use for loop for splitting folders and fetch files
for folder in folder_paths:
   try:
       files = os.listdir(folder)
   except FileNotFoundError:
       print("Error - Please provide a valid folder name" + folder + "is not valid")
       continue
   print("Prints files inside -"+ folder)
   
   for file in files:
       print(file)
