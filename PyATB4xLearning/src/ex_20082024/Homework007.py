#Task #7
#✅ Leap Year Checker:
#img_1.png
#Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

year = int(input("Please enter the year -> "))

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print("Leap year!!!")
        else:
            print("Not a Leap year!")
    else:
        print("Leap year!!!")
else:
    print("Not a Leap year!")
