#Match Statement
#Switch in Java
#match the op and execute
# python > 3.10

#Write a program to ask the user which browser he wants to run the automation

browser_name = input("Enter the name of the browser \n")
browser_name = browser_name.lower()

match browser_name:
    case 'firefox':
        print("Execute the firefox code")
    case 'chrome':
        print("Execute the chrome code")
    case 'edge':
        print("Execute the edge code")
    case 'safari':
        print("Execute the safari code")
    case _:
        print("Browser not found!")
