### Task #5
#- Create a program that takes two numbers as input and prints
# whether the first number is greater than, less than, or equal to the second number.

num1 = float(input("Enter the first number-> "))
num2 = float(input("Enter the second number-> "))

if num1 > num2:
    print(f"{num1} is greater than {num2}.")

elif num1 < num2:
    print(f"{num1} is lesser than {num2}.")
else:
    print(f"{num1} is equals to {num2}.")