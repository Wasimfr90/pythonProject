# Task #10 -
# ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

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







