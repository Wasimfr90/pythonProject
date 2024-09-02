#Dict
#key and Value pair

student_info = {
    "name" : "Wasim",
    #"age" : 65,
    "age" : 67,
    "address" : "KA"

}

print(student_info)
print(student_info["name"])
print(student_info["age"])
print(student_info["address"])

student_info["age"] = 100
print(student_info)

#Different way to declare the Dict

student_info2 = dict(name = "Wasim", age = 67, address = "KA")

print(student_info2)

student_info3 = {
    "name" : "Wasim",
    #"age" : 65,
    "age" : 67,
    "address" : {

        "Home_address" : "WB",
        "Office_address" : "KA"
    }

}

print(student_info3)
print(student_info3["address"]["Office_address"])



print("------------------------------------------")

student_info4 = {
    "name" : "Wasim",
    #"age" : 65,
    "age" : 67,
    "address" : {

        "Home_address" : "WB",
        "Office_address" : "KA"
    }

}

student_info5 = {
    "name" : "Amit",
    #"age" : 65,
    "age" : 69,
    "address" : {

        "Home_address" : "GOA",
        "Office_address" : "KA"
    }

}


student_list = [student_info4, student_info5]

print(student_list)