#Constructor
#Special function in Class.  __init__()
#It will be automatically called when we create an object


class Dog:
    name = None #Instance variables
    age = None

    # def __init__(self):    #Default Constructor
    #     print("DC | I will be automatically called when object is created")

    def __init__(self,name,age):
        print("Called object is created")
        self.name = name
        self.age = age


    def sleep(self):
        print("Sleeping")
        print("Who is sleeping -> ", self.name)


#dog1 = Dog()
dog1 = Dog("Chow",10)
print(dog1.name)
print(dog1.age)
dog1.sleep()
print(id(dog1))


dog2 = Dog("Mow",20)
print(dog2.name)
print(dog1.age)
dog2.sleep()
print(id(dog2))