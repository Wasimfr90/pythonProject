#
# class VWOLoginpage:
#     def __init__(self, email_arg, pass_arg):
#         self.email = email_arg
#         self.password = pass_arg
#
#
#     def login_confirm(self):
#         if self.email == "wasimfr90@gmail.com" and self.password == "was123":
#             print("Allowed to login")
#         else:
#             print("Not allowed to login")
#
#
# email = input("Please enter the email id : \n")
# password = input("Please enter the password : \n")
#
# vwo_obj = VWOLoginpage(email,password)
# vwo_obj.login_confirm()





class VWOloginpage:

    def __init__(self, user_arg, pass_arg):
        self.username = user_arg
        self.password = pass_arg


    def loginvalidation(self):
        if self.username == "wasimfr90@gmail.com" and self.password == "was123":
            print("Allowed to login.")
        else:
            print("not allowed to login!!!")


email = input("Please enter the email id: \n")
password = input("Please enter the password: \n")

login_obj = VWOloginpage(email, password)
login_obj.loginvalidation()