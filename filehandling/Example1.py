from os import path #This imports the path module from the os library, which contains functions for manipulating filesystem paths.

print("File Exists\t",path.exists("web.xml")) #This line checks if a file named web.xml exists in the current working directory and prints the result.
print("Directory Exists\t",path.exists("d:\\new")) #This line checks if a directory named new exists on the D: drive and prints the result.

