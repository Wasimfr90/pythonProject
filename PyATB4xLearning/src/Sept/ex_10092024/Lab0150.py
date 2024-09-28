# Exception
# Exceptions are Class

print("----Start of the program----")

try:

    a = int(input("Please enter a number1"))
    b = int(input("Please enter a number2"))
    c = a/b         # 1. ZeroDivisionError: division by zero
                    # 2. ValueError: invalid literal for int() with base 10: 'was'

    print("Result Div is ",c)

except Exception as e:     # as -> alias   # Exception is a Class here
    print(e)
    print("Please check your inputs, it should not be a string or zero")

print("----End of the program----")




