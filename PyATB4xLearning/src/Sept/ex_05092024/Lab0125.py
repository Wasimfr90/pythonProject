class Parent:
    gold = "2kg"

    def BHK2(self):
        print("2BHK")


class Child(Parent):
    diamond = "Diamond"
    def BHK3(self):
        print("3BHK")


child_obj = Child()
print(child_obj.gold)
child_obj.BHK3()
child_obj.BHK2()


father_obj = Parent()
father_obj.BHK2()
#father_obj.BHK3()    -> not allowed
#print(father_obj.diamond)   -> not allowed
