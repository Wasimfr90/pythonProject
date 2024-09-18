
class Dog:      #Class name will starts with Capital letter
    #A
    name = None
    breed = None
    color = None


    #B
    def sleep(self):
        print("Sleeping")

    def bark(self):
        print("Barking")

dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()

print("-------------------------------------")

dog2 = Dog()
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)
dog2.sleep()


dog3 = dog1    #storing dog1 object reference into dog3
