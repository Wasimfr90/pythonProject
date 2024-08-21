#Problem to find the max among three

#Logic building
#User input - num1, num2, num3 - int
#O/p - int or Str with max number

#Logic?
#if elif else

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))

if num1 > num2 and num1 > num3 :
    print(f"{num1} is greater.")

elif num2 > num1 and num2 > num3 :
    print(f"{num2} is greater.")

else:
    print(f"{num3} is greater.")


