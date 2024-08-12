print("******TUPLE*******")

data = (100,200,100,400)
print(data)
print(type(data))

print(data[-1])


x = (11,22)
y = (33,44)

z = x+y
print(z)

z = x*4
print(z)

x = x*4
print(x)


data = (100,200,990,200,80,999,200,200,111,456)

c = data.count(200)
print(c)

i = data.index(999)
print(i)


x = 11,22,33
print(x)
print(type(x))


x = (11)
print(x)
print(type(x))



print("******SET*******")

data = {11,22,33}
print(data)
print(type(data))

data.add("Ajay")
print(data)

data.update({55:66,22:88,99:100})
print(data)
data.update("test")
print(data)

data.add("test")
print(data)

data.remove(99)
print(data)

data.clear()
print(data)

data = {11,22,33}
x = data.copy()
print(data)
print(x)

print("**set intersection**")

data1 = {11,22,33}
data2 = {22,99,44,33}

out = data1.intersection(data2)
print(out)


data1 = {11,22,33}
data2 = {99,44}

out = data1.intersection(data2)
print(out)

print("**set union**")

data1 = {11,22,33}
data2 = {22,99,44,33}
data3 = {100,200}

out = data1.union(data2)
print(out)

out2 = data1.union(data2).union(data3)
print(out2)

print("**set difference**")

data1 = {11,22,33,90}
data2 = {22,99,44,33}

out = data1.difference(data2)
print(out)

out = data2.difference(data1)
print(out)

out = data1.difference(data2).difference(data1)
print(out)


print("**set symmetric difference**")

data1 = {11,22,33,90}
data2 = {22,99,44,33}

out = data1.symmetric_difference(data2)
print(out)


print("**set issubset*")

data1 = {11,22}
data2 = {22,99,44,33,11}

out = data1.issubset(data2)
print(out)

print("**************")

data1 = {11,22,33}
data2 = {22,99,44,33}
data3 = {100,200}

out = data1 | data2
print("Union using another method -> ", out)