# Hybrid Inheritance

# multiple type of inheritance
# such as single,
# multiple, and
# multilevel inheritance



class A:     # father
    def methodA(self):
        return "Method A"


class B(A):    # Pramod(Brother 1)
    def methodB(self):
        return "Method B"

class C(A):     # Lucky(Brother 2)
    def methodC(self):
        return "Method C"

class D(B, C):     #Sister   # Multiple, Multilevel
    def methodD(self):
        return "Method D"


d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())



