### Task #4
#- Write a Python program to calculate the area of a circle
# given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

#Step 1 Figure out the input and output
#input -> r -> data type -> float
#pi -> 3.14, math.pi
#power -> pow or ** -> any

#Step 2
#rough logic = area = 3.14 *pow(r,2)

#Step 3
#Write the logic

import math

radius = float(input("Enter the radius of the circule ->"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius,2)
area2 = 3.14 * (radius ** 2)

print("Area of the circle is -> ", area)
print(f"Area of the circle is ->{area:.2f}")
print(f"Area2 of the circle2 is ->{area2:.2f}")



print(3.14 * (float(input("Enter the radius here ->\n"))**2))