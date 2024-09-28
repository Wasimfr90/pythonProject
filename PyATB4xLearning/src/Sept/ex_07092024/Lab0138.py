# Method Overloading
# Python doesn't support method overloading
# in the traditional sense
# Method Overloading - same method in same class.
# Method Overriding - same method in different class.


class MathUtils(object):  # IS-A object - Single inheritance
    # every class is by default inherit object class. Even if we don't declare it while writing code
    # Method overloading is not supported in Python !!

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

    def add(self, a, b, c=0, d=1):
        return a + b + c + d
# to use the method we need to provide the default value of other parameter
# so basically Method Overloading is fully supported in Python!!!

math = MathUtils()
print(math.add(1, 2))
