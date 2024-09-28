# Static Methods
# A Static method is a method which belongs to a class
# rather belongs to the Instance of the class.
# If we make any method as @staticmethod then while calling no need to create any object reference.
# Directly we call using the class name.


class MathOperation:

    def div(self, a, b):
        return a / b

    def mul(self, a, b):
        return a * b

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


# Non Static Method - Object creation is mandatory
object_ref = MathOperation()
output = object_ref.div(10, 5)
output2 = object_ref.mul(10, 5)
print(output)
print(output2)

# Calling @staticmethod sum(), directly using the class name.
print(MathOperation.sum(3,5))
print(MathOperation.sub(5,3))