

year = int(input("Please enter, how many years you want to do investment:\n"))

current_amount = float(input("Please enter the amount where you want to start from:\n"))


percent = float(10/100)

new_amount = 0

for yr in range(year):
    new_amount = float(current_amount) * percent
    current_amount += new_amount
    print(f"For year {2025+yr} -> Rs:{current_amount}")



