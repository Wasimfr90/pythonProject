# Method Overriding - Same name can have in parent and child class
# Child always override the parent function
# Super() can call my parent functions and attributes/variables
# self - me
# super() - parent, Super class, Father

class Grandfather:
    x = 30
    def home(self):
        print("Old home")
class Father(Grandfather):
    a = 10
    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)
        super().home()


class Son(Father):
    b = 20
    def home(self):
        super().home()
        print(super().a)
        print("No home")
        print(self.b)

s1 = Son()
s1.home()

print("---------------")
f1 = Father()
f1.home()