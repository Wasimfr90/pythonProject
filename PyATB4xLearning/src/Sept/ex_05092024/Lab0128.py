# Multiple Inheritance

class Father:
    key = "ABC"
    __password = "private"

    def __show_password(self):      # this will call __password variable which is private -> up
        print(self.__password)

    def father_money(self):
        return 5

    def home(self):
        return "This is from the father"

    def show_everything(self):        # this will call __show_password() method which is private-> up
        self.__show_password()

class Mother:
    def mother_money(self):
        return 2

    def home(self):
        return "This is from the mother"



class Son(Mother, Father):  # MRO - Method Resolution Order
    pass

class Son2(Father, Mother):
    pass

s = Son()
print(s.father_money())
print(s.mother_money())
print(s.home())        # if both the class has same method, then during multilevel inheritance,
# whichever way child class has called the parent class that method will be called.
# This is called as Diamond problem in JAVA, which got resolved in Python.

print(s.key)
s.show_everything()

s2 = Son2()
print(s2.home())


