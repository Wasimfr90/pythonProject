# Custom Exception   -> user defined exception

# class BlancelowException(Exception):
#     def __init__(self,message):
#         self.message = message
#         super().__init__(message)
#
# balance = 100
# withdraw = int(input("Enter the amount you want to withdraw!!!"))
#
# if withdraw > balance:
#     raise BlancelowException("Balance is low!!!")
# else:
#     print("Remaining balance ", (balance - withdraw))



print("---------------------------")

class BalanceLowException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("Enter the amount you want to withdraw!!"))

if withdraw > balance:
    raise BalanceLowException("Balance is low!!")
else:
    print("Remaining balance: ",(balance - withdraw))





