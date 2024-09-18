

class Person:
    # class variable
    #Instance Variable

    #name = "Amit"

    def __init__(self,name):
        self.name = name

    def walk(self):
        #print(self.name)
        return self.name

amit = Person("Amit")
pramod = Person("Pramod")
print(amit.name)
print(pramod.name)
print("Who is walking -> ",amit.walk())
