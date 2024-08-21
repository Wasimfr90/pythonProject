#Task #8
#✅ Triangle Classifier:
#img.png
#Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

side1 = float(input("Please enter the side1 value of a triangle->"))
side2 = float(input("Please enter the side2 value of a triangle->"))
side3 = float(input("Please enter the side3 value of a triangle->"))

if side1 == side2 and side2 == side3 and side1 == side3 :
    print("It is a equilateral triangle as all sides are equal!!!")

elif side1 == side2 or side2 == side3 or side1 == side3 :
    print("It is a isosceles triangle as two sides are equal!!!")

else:
    print("It is scalene triangle as no sides are equal!!!")



