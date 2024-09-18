
def add_before_ui_after_ui(func):   # It will take another function as an argument ex - drive_bike()
    #two parts
    #wrapper and call

    def wrapper():
        print("1. Before running UI TC.")
        print("2. Start the browser")
        func()         # this is calling -> test_ui()
        print("3. End running the UI TC.")
        print("4. Quit the browser")

    return wrapper()



@add_before_ui_after_ui
def test_ui():
    print("I will test the UI")

#test_ui()
