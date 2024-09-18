# Class and Object Assignment
#
#
# Create a Employee Class
# A - name,age, phone, address, eid
# B - walk, talk, printdetails,
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions.


class Employee:
    #A:
    name = None
    age = None
    phone = None
    address = None
    eid = None

    #B
    def __init__(self,name,age,phone,address,eid):
        print("Constructor")
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    def walk(self):
        print("EMP is walking ->",self.name)

    def talk(self):
        print("EMP is talking - >",self.name)

    def printdetails(self):
        print("EMP Details:")
        print("Employee name: ",self.name)
        print("Employee age: ",self.age)
        print("Employee phone: ",self.phone)
        print("Employee address: ",self.address)
        print("Employee eid: ",self.eid)


emp1 = Employee("Wasim",65,123456789,"KA","wa123@gmail.com")
print(emp1.name)
print(emp1.age)
emp1.walk()
emp1.talk()
emp1.printdetails()


print("---------------------------------------------------------")

emp2 = Employee("Firoj",56,987654321,"WB","fij789@gmail.com")
print(emp2.name)
print(emp2.address)
emp2.walk()
emp2.talk()
emp2.printdetails()


