# Hierarchical Inheritance

class Father:
    def BHK1(self):
        print("1BHK")

class Wasim(Father):
    def BHK2(self):
        print("2BHK")

class Firoj(Father):
    def BHK3(self):
        print("3BHK")

class Rahaman(Father):
    def no_house(self):
        print("No house")

wa = Wasim()
wa.BHK1()
wa.BHK2()

fi = Firoj()
fi.BHK1()
fi.BHK3()
#fi.BHK2()   # not able to access the method as it is not inherited from Wasim class.
