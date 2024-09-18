#Task #9
#✅ FizzBuzz Test: Write a program that prints numbers from 1 to 100.
# Loop For However, for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."

"""
num = 100
print(type(num))
#i = 1

for i in range(num):
    if i % 3 == 0 and i % 5 != 0 :
        print("Fizz")

    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")

    elif i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    else:
        print(i)

"""


for i in range(1, 101, 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)