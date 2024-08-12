print("*************FUNCTIONS***************")

def jupiter():
    print("Too far")

jupiter()

print("*********************")

def jessi(mood='happy'):
    print(mood)
    if mood == 'happy':
        print("Arf arf")
    else:
        print("*whimper*")

print("First time")
jessi()

print("Second time")
jessi('sad')


print("*********************")
print("*********************")

def add_one(x):
    print(x+1)
    return x+1

y = add_one(5)
print(y)


print("*********************")
print("*********************")

def my_function(*kids):
    print(f"The youngest child is {kids[2]}")

my_function("Wasim","Firoj","Rahaman")



print()

def my_fun(c3,c1,c2):
    print(f"The youngest child is {c3}.")

my_fun(c1="Wa",c2="Fi",c3="Ra")

print()


def my_func2(**kid):
    print(f"His last name is {kid["lname"]}")

my_func2(fname="was",lname="raha")


print()



def my_func3(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_func3(fruits)