# Task #10 -
# ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

"""
n = int(input("Please enter the number : "))
fact = 1
fact1 = 1

if n == 0:
    print("The factorial of 0 is 1")
elif n < 0:
    print("Factorial of negative number is not possible!")
else:
    for fact in range(n,1,-1):
        fact1 = fact1 * fact
    print(f"factorial value of {n} is -> {fact1}")

"""


num = int(input("Please enter the number : "))
fact = 1

if num == 0 and num == 1:
    fact = 1
    print(1)
else:
    # for i in range(1, num+1, 1):
    #     fact = fact * i

    i =1
    while (i<= num):
        fact = fact*i
        i =i+1

print(fact)





