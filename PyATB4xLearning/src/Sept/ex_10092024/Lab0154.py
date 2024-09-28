# try, except and finally
# file
import os

try:

    full_path = os.getcwd()
    print(full_path)
    full_path_file = full_path+'/example.txt'
    print(full_path_file) 
    file = open(full_path_file)
    # file = open(full_path+'/example.txt')
    #file = open('example.txt','r')     # FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
    #file = open('D:\files\Python\Pycharm projects\Python Project\pythonProject\PyATB4xLearning\src\Sept\ex_10092024\example.txt','r')
    # If file is not present in same package then we can use the Absolute path(as above) of the file
    # which we need to use. [r-click -> copy path/ref -> Absolute path]

    print(file.read())

except FileNotFoundError as fnfe:
    print("File not found, fix the path or create a file")

finally:

    try:
        file.close()

    except NameError as ne:
        print(ne)




