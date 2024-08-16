# Task #2
#
# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# # Format your out with f{""}

num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))

m1 = max(num1,num2)
print(f"The max value is : {m1}")

p1 = pow(num1,num2)
print(f"The power of num1 is: {p1}")

print(f"Sum is: {num1+num2}")
print(f"Sub is: {num1-num2}")
print(f"Mul is: {num1*num2}")
print(f"Div is: {num1/num2}")