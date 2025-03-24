# Calculator Program

logo = """ _____       _            _       _             
/  __ \\     | |          | |     | |            
| /  \\/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \\| '__|
| \\__/\\ (_| | | (__| |_| | | (_| | || (_) | |   
 \\____/\\__,_|_|\\___|\\__,_|_|\\__,_|\\__\\___/|_|   
 """
print(logo)
print("-------------------------------------------------------")

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operators = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,

}

def calculator():
    num1 = float(input("What is the first number?: "))

    cal_flag = True

    while cal_flag:

        for symbol in operators:
            print(symbol)
        cal_ops = input("Please pick one operation: ")

        num2 = float(input("What is the next number?: "))

        answer = operators[cal_ops](num1, num2)

        print(f"{num1} {cal_ops} {num2} = {answer}")

        continue_cal = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if continue_cal == 'y':
            num1 = answer
        else:
            cal_flag = False
            print("\n" * 20)
            calculator()


calculator()




