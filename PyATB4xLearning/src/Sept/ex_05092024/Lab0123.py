class Bank:

    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number


    def deposit(self, amount):
        self.balance = self.balance + amount


    def check_balance_account(self):
        print(self.balance)
        self.__internal_method()


    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not allowed")


    def __internal_method(self):       # Private method - It can access private variables and methods and normal var and mrthods as well.
        print("Private Method")
        print(self.__account_number)
        self.show_me_account_number()


icici = Bank(987654321, 100)
icici.deposit(100)
icici.check_balance_account()
icici.show_me_account_number(True)
#icici.__internal_method()   # Error

