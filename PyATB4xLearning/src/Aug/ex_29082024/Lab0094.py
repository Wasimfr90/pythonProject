#List

my_list = [1,2,3]
my_list2 = [1, True, "Pramod", 12.34]

print(my_list)
print(len(my_list))

print(my_list[0])

my_list[0] = "Wasim"

print(my_list)

for element in my_list:
    print(element)


print("------------------------------------------")

my_list = [1,2,3]

#append
my_list.append(4)
my_list.append(5)
my_list.append(6)

print(my_list)

#extend
my_list.extend(["Wasim","Firoj",10,3.14,True])
print(my_list)
print(len(my_list))

#insert
my_list.insert(1,"Hello")
print(my_list)
print(len(my_list))
my_list.insert(-1,"Lucky")
print(my_list)
print(len(my_list))

my_list[1] = "Banana"
print(my_list)
print(len(my_list))

my_list.remove("Lucky")
print(my_list)
print(len(my_list))

print("-----------------------------------------")

my_copy_list = my_list.copy()   # creating a copy in another list, even after deleting the first list(my_list)

print(my_list)
print(my_copy_list)

my_list.clear()

print(my_list)
print(my_copy_list)


my_copy_list.pop()
my_copy_list.pop()
my_copy_list.remove("Wasim")
my_copy_list.remove("Firoj")
my_copy_list.remove("Banana")
my_copy_list.insert(2,22)
my_copy_list.insert(4,100)


print(my_copy_list)

my_copy_list.sort()
print("Hello")
my_copy_list.sort(reverse=False)
print(my_copy_list)


my_copy_list.reverse()
print(my_copy_list)

print("--------------")

l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1+l2
print(l3)
