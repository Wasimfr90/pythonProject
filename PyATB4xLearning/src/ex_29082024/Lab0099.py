

a, b, c = (10, 11, 12)
print(a)
print(b)
print(c)

#Search in Tuple

cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities)
print("Kolkata" in cities)


t = (12,34,56)
#t.append(12) #'tuple' object has no attribute 'append'

my_list = list(t)
my_list.append(12)
t = tuple(my_list)
print(t)