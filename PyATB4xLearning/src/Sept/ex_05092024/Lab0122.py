
class Myclass:

    # public var (Instance variable)  --> available for all
    public_var = "I am PUBLIC"
    balance = 0

    # private variable             --> not available for any
    __private_var = "I am PRIVATE"
    __password = "1234"

    # protected variable           --> Same package it is available, but not available for other package
    _protected_var = "I am PROTECTED"


object = Myclass()
print(object.public_var)
print(object.balance)
# print(object.__private_var)   # private can't be called it can only be used inside the class.
# print(object.__password)
print(object._protected_var)