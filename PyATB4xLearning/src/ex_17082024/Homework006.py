### Task #6
#- Develop a Python script that calculates the square and cube of a given number.

num = float(input("Enter the number -> "))

val = int(input("Make your choice for 1.Square and 2.Cube:"))

if val == 1:
    num1 = num ** 2
    print(f"Square value of {num} is-> {num1}.")
elif val == 2:
    num1 = num ** 3
    print(f"Cube value of {num} is-> {num1}.")
else:
    print("please make a valid choice!!!!")


