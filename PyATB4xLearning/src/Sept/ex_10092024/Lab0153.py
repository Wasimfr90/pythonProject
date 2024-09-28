# Exception
# try, except and finally


try:

    num1 = int(input("Please enter a number1"))
    num2 = int(input("Please enter a number2"))
    result = num1/num2

except ValueError as ve:
    print("Value Error, You have entered the string instead we want int")

except ZeroDivisionError as ze:
    print("Zero Div error, Don't use the num2 as 0")

else:
    print(f"Result is {result}")

finally:
    print("This code will be always executed.!")
