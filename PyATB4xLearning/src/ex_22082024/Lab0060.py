user_type = input("Enter the user type, admin, manger, guest\n")

match user_type:
    case "admin" | "manager":
        print("Hello, sir")
    case "guest":
        print("Hello, guest")
    case _:
        print("Hello, There")
