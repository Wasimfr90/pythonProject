"""

def make_pizza(*toppings,base):
    print(toppings,base)

def make_pizza_2(base, *toppings):
    print(base,toppings)

make_pizza("masroom","tomato","cheese",base="thin crust")
#make_pizza_2("masroom","tomato","cheese",base="thin crust")
#make_pizza_2(base="crust","msss","fffff","hhhh")


"""



#Function scope

global_b = 12    # this works almost a like a global variable
def my_function():
    a = 10   #local variable within the function
    print(a)
    print(global_b)


def f1():
    print(global_b)
    #print(a)

#print(a)
my_function()
print(global_b)
f1()

