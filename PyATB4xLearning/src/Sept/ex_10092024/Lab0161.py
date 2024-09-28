# FILE HANDLING
# How to read and write in a file
# open("file_name","mode")  <- syntax

# read a file:
# Reading entire content: content = file_object.read()
# For a single line: line = file_object.readline()
# For all line: line = file_object.readlines()
# Close the file


import os

full_path_file = os.path.join("D:\\files\Python\Pycharm projects\Python Project\pythonProject\PyATB4xLearning\src\Sept\ex_10092024\was", "wasim.txt")
file = open(full_path_file, "r")


#file = open("was/wasim.txt", "r")        # This can be done using absolute path

content = file.read()
print(content)



