def print_arguments(*args):
    # *args -> multiple arguments with no limit -> list
    # print(args[0])
    for i in args:
        print(i)


print_arguments("Wasim", "Firoj", "Rahaman")
print_arguments("Firoj", "Rahaman")
print_arguments("Firoj", 10)
print_arguments("Firoj", 10, True)
print_arguments("Firoj", 10, True, False)
print_arguments("Firoj", 10, True, False, "HARSH")
print_arguments("Rahaman")
# print_arguments()
# minimum 1 argument is important
