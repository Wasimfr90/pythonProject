# Multilevel Inheritance

class Grandfather:
    key = "2kg"

    def bhk1(self):
        print("1BKH")

class Father(Grandfather):
    diamond = "22 karat"

    def bhk2(self):
        print("2BHK")

class Son(Father):
    btc = "1BTC"

    def bkh3(self):
        print("3BHK")

s = Son()
f = Father()
gf = Grandfather()


