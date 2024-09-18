# Class Variable
# Method
#       public - Don't mention anything
#       protected - _
#       private - __
# Inheritance
# Polymorphism
# Abstraction
# Encapsulation
# Static method
# Variables



# Variables
# 1. Local variable (within the function / block)
# 2. Global variable
# 3. Instance variable (within the class)
# 4. Static variable (in future)



a = 10

class Person:
    b = 11    # Instance variable - belongs to class

    def print_info(self):
        # print(a)
        # print(self.b)

        global a    # Declare it as global variable
        a = "Hello"

#a = 10
object_ref = Person()
object_ref.print_info()
print(a)
#print(b)

a = 10
