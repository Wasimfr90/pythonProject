
class Person:
    #Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None



    #Behaviour
    def talk(self):  #Arg with No Return tupe   #self - this. Self will be the first argument in every behaviour.
        print("I can talk")

    def sleep(self, name):              #Arg with No Return
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name):             #Arg with Return
        print("I am a Method!!")
        return None

    def walk(self):             #Arg with No Return
        print("I am a walking")

    def walk_return(self):             #No Arg with Return
        return "I am a walking"


#Create an object of the class
#ObjectRef = ClassName() -> Object

wasim = Person()
wasim.name = "Wasim"
print(wasim.name)
wasim.talk()

rajyalakshmi = Person()
rajyalakshmi.name = "Rajyalakshmi"
print(rajyalakshmi.name)
rajyalakshmi.talk()