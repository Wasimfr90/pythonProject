# How to write a file

# file = open("TestData.txt","a")    # same can be represented with "with ...as...."
with open("TestData.txt","a") as file:
    file.write("Hello, How are you?")

