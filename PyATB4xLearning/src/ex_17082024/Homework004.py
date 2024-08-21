### Task #4
# - Write a Python program to calculate the area of a circle
# given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

import math

radius = float(input("Enter the radius value -> "))

print("PI value can be represented as 1. math.pi or 2. 3.14")
pi = int(input("Enter your choice for PI value as 1 or 2 -> "))

"""
if pi != 1 or pi != 2 :
    print("Please enter PI value as either 1 or 2 as your input.!!!!")

else:
    print("Power value can be represented as 1. math.pow or **")
    pow = int(input("Enter your choice for power representation as 1 or 2 -> "))

    if pow != 1 or pow != 2:
        print("Please enter POW value as either 1 or 2 as your input.!!!!")

"""
if pi == 1 or pi == 2:
    print("Power value can be represented as 1. math.pow or 2. **")
    pow1 = int(input("Enter your choice for power representation as 1 or 2 -> "))

    if pi == 1 and pow1 == 1:
        area = math.pi * math.pow(radius, 2)
        print(f"11->Area of a circle is -> {area:.2f}")

    elif pi == 1 and pow1 == 2:
        area = math.pi * (radius ** 2)
        print(f"12->Area of a circle is -> {area:.2f}")

    elif pi == 2 and pow1 == 1:
        area = 3.14 * math.pow(radius, 2)
        print(f"21->Area of a circle is -> {area:.2f}")

    elif pi == 2 and pow1 == 2:
        area = 3.14 * (radius ** 2)
        print(f"22->Area of a circle is -> {area:.2f}")

    else:
        print("Please enter POW value as either 1 or 2 as your input.!!!!")

else:
    print("Please enter PI value as either 1 or 2 as your input.!!!!")












