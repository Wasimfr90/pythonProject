#User defined
#1. They can't return -> non return (none)
#2. They can return something
#3. They don't have parameters/arguments
#4. They have parameters


#1. They can't return -> non return (none)
# No return type with no arguments

def greet():
    print("Hello world")

result = greet()
print(result)


#2. They can return something
# No return type with arguments

def greet_by_name(name):
    print("Hello, ",name)

greet_by_name("Wasim")


#3. They don't have parameters/arguments
#No return type with Default argument -> If there is no argument passed then Default value will be printed.

def say_hello_to_default_arg(name="Rahaman"):
    print("Hello, ",name)

say_hello_to_default_arg("Amit")
say_hello_to_default_arg()
say_hello_to_default_arg(name="Pramod")  #positional argument


def multiple_arg(name1="Arpita", name2="Pramod", name3="Ajay"):
    print("Multiple arguments ", name1, name2, name3)

multiple_arg(name1="Ram", name2="Yonus", name3="Deepshikha")
multiple_arg()


#4. They have parameters
# Argument + return type

def sum_of_two_num(num1, num2):
    return num1+num2

result = sum_of_two_num(10, 34)
result = sum_of_two_num(num1=34, num2=24)
print(result)



def sum_of_two_num_with_default_val(num1=100, num2=200):
    return num1+num2

#result = sum_of_two_num(10, 34)
#result = sum_of_two_num(num1=34, num2=24)
result = sum_of_two_num_with_default_val()
print(result)

