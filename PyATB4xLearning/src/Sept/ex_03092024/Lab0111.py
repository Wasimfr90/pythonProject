class Calc:
    def __init__(self):
        print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


result = Calc()

x = int(input("Enter the value of x -> "))
y = int(input("Enter the value of y -> "))

output_sum = result.sum(x, y)
output_sub = result.sub(x, y)
output_mul = result.mul(x, y)
output_div = result.div(x, y)

# print(output_sum, output_sub, output_mul, output_div)
print(f"Sum value is {output_sum}")
print(f"Sub value is {output_sub}")
print(f"Mul value is {output_mul}")
print(f"Div value is {output_div}")
