import os

# os -> Operating System -> file, path related to OS

# print(os.name) # nt - windows unix based system, in case mac -> posix
#
# if os.name == 'posix':
#     print(" You are using MAC")
# else:
#     print("Windows")

# print(os.getcwd())   # to get the current working directory
#
# os.chdir("downloads")  # to change directory(chdir) you need to use the full path
# print(os.getcwd())

# os.mkdir('new_directory')   # to create a new directory

# os.makedirs("parent/child/grandchild")  # makedirs -> to create a chain of directories

# print(os.listdir("."))   # listdir -> to list all the files inside the directories
#
# for file in os.listdir("."):
#     print(file)

# os.remove("file1.txt")          # to remove the existing file
# os.rmdir("new_directory")        # to remove the existing directory
#
# os.rename("old_name.txt", "new_name.txt")   # rename the file

# important one which we mostly going to use is below

#full_path = os.path.join('folder','file.txt')
full_path = os.path.join('D:\files\Python\Pycharm projects\Python Project\pythonProject\PyATB4xLearning\src\Sept\ex_10092024','file.txt')
print(full_path)

print(os.path.exists('file.txt'))

print(os.path.isfile('file.txt'))

print(os.path.isdir('directory_name'))
