data = [100,200,300, "Ramesh"]
print(data)
print(data[2])
print(data[-1])
print(data[1:])

data[1] = "Wasim"
print(data)

data2 = "wasim"
out = data2.replace("a","wow")
print(data2)
print(out)

"""
LIST methods - append, insert, pop, remove, index, count, reverse, extend,copy, clear
"""

data = [11,30,80,99]
data.append(111)
print(data)

data.insert(2,55)
print(data)

data.remove(99)
print(data)
data = [11, 30, 99, 55, 80, 99, 111, 99]
data.remove(99)
print(data)

data.pop(4)
print(data)

data.pop()
print(data)

data = [11, 30, 99, 55, 80, 99, 111, 99]

a = data.index(80)
print(a)

b = data.index(99)
print(b)

data = [11, 30, 99, 55, 80, 99, 111, 99]
c = data.count(99)
print(c)
print(data.count(111))

print(data)
data.reverse()
print(data)

data2 = [67,55,11,88,67,56,99,13,23,10,4]
print(data2)
data2.sort()
print(data2)

data.clear()
print(data)

data2 = [67,55,11,88,67,56,99,13,23,10,4]
out = data2[2:6].copy()
print(out)

out.extend([100,200,300])
print(out)


data = [10,20,30]
data2 = [40,50,60]

data.extend(data2)
print(data)
