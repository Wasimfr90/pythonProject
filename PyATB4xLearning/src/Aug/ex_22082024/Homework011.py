# Task #11 -
# ✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13


# 0,1 | 0+1 = 1
# 1,1 | 1+1 = 2
# 1,2 | 1+2 = 3
# 2,3 | 2+3 = 5
# 3,5 | 3+5 = 8
num = int(input("Please enter the number -> "))

f1 = 0
f2 = 1
f3 = 0

print(f"Before value of f1 is -> {f1}")
print(f"Before value of f2 is -> {f2}")
print(f"Before value of f3 is -> {f3}")
print("\n")

while num != 0:
    f3 = f1 + f2

    print(f"After value of f1 is -> {f1}")
    print(f"After value of f2 is -> {f2}")
    print(f"Fibonaci value of f3 is {f1} + {f2} -> {f3}")

    f1 = f2
    f2 = f3

    num = num - 1











