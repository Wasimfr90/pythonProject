#Understanding Decorator in Python

# - Decorators in Python are a way to modify the behavior of a function or class without changing its source code.
# - They are a powerful tool that allows you to wrap another function and extend its functionality,
# while keeping the original function's code unchanged.


def my_decorator(func):   # It will take another function as an argument ex - drive_bike()
    #two parts
    #wrapper and call

    def wrapper():             #wrapper()  -> can be used any name ex - wasim(), then return wasim()
        print("1. Before the functon is called.")
        print("2. Add Helmet, dashcam, gloves, knee guard")
        #drive_bike()
        func()         # this is calling -> drive_bike()
        print("3. After the functon is called.")
        print("4. Secure driving")

    return wrapper()


#defination

# @my_decorator
# # def drive_bike():
# #     print("I am driving")

#call to the function
# drive_bike()

@my_decorator
def drive_sccoty():
    print("Normal function")

#drive_sccoty()


