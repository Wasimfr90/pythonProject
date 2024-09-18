#lambda expression

# def triple_me(num):
#     return num ** 3
#
# op = triple_me(10)
# print(op)


op = lambda num: num ** 3
print(op(10))


#2nd exmple

# def add_10(n):
#     return n + 10
#
# op = add_10(100)
# print(op)

op = lambda n: n + 10
print(op(100))

#3rd exmple

# def mul(a,b):
#     return a * b
#
# oo = mul(2,3)
# print(oo)

oo = lambda a,b : a * b
print(oo(2,3))


# def sum_three_num(a,b,c):
#     return a+b+c

oo = lambda a,b,c : a+b+c
print(oo(2,3,4))

#