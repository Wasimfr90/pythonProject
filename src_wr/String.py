person = "Today is Saterday"
print(person)
print(type(person))

_abc = "Hello"
print(_abc)

_="catastrophy"
print(_)

print("*********************************")

print("Ajay")
print("Vijay")

print("*********************************")

wasim = print
wasim("Let see if it works")

print("*********************************")

fname = "Wasim"
mname = "Firoj"

print(fname+" "+mname)

name = fname+mname

print(name)

print("*********************************")

name = "                   Wasim"
print(name)

name1 = "Firoj                    "
print(name1)

name2 = "         Rahaman           "
print(name2)
print(name2+".")

name3 = "                       "
print(":"+name3+":")


print("*********************************")

no = "ab"
out = no*5
print(out)

inp = "01" *25
print(inp)


print("*********************************")

name = "Wasim Firoj Rahaman"
print(name)
print(name[7])
print(name[2],name[10])

print(name[1+2])
print(name[2*2])

i = 3*2
print(name[i])

print(name[-1])
print(name[-4])
print(name[-7])


print(name[2:7])
print(name[3:11])
print(name[2:500])
print(name[3:])
print(name[:6])
print(name[:])
print(name[8:2])
print(name[-5:-1])
print(name[-11:])
print(name[:-1])
print(name[0:1])
print(name[0:0])


print("*********************************")

"""
Stirng methods - upper, lower, strip, lstrip, rstrip, replace, count, index, split, join, startswith, endswith,
isdight, isupper, islower, title, capitalize, swapcase
"""


name = "WASim fIrOj rAhaMan"
print(name)
print(name.upper())
print(name.lower())

out = name.upper()
print(out)

out2 = name[2:].upper()
print(out2)


number = "456789"
name = "Ajay Kumar"

out = name.replace('a',':h')
print(name)
print(out)

out2 = name.replace('Ajay','Shamol')
print(out2)


number = "34323837398763095347389"

out = number.replace('3',"")
print(number)
print(out)

name = "Ajay Kumar"
out = name[0:4].replace('a','m')
print(name)
print(out)

name = "Wasim Firoj Rahaman"
out = name.replace('a','b',2)
print(name)
print(out)

out = name.replace(name[6],'H')
print(out)

name = "Wasim Firoj Rahaman"
out = name.count('a')
print(out)
out = name.count("im")
print(out)
out = name.count("rk")
print(out)

name = "Ajay Kumar Kiran"
out = name.count("a")
print(out)

name = "Ajay Kumar Kiran"

i = name.index("a")
print(i)

i = name.index("mar")
print(i)

print("*****Strip*****")

name = "              Ajay Kumar\t\t\n\t\t"
print(":"+name+":")

name = name.strip()
print(name)
print(":"+name+":")

name = "              Ajay Kumar\t\t\n\t\t"
print(":"+name+":")

name = name.lstrip()
print(":"+name+":")


name = "              Ajay Kumar\t\t\n\t\t"
name  = name.rstrip()
print(":"+name+":")


report = "result.txt"
out = report.endswith(".txt")
print(out)
out = report.endswith(".py")
print(out)

out = report.startswith("re")
print(out)


num1 = "867533938682"
num2 = "ahshbds2343xkn"
num3 = "7699.98998"

out = num1.isdigit()
print(out)

out2 = num2.isdigit()
print(out2)

out3 = num3.isdigit()
print(out3)

name = "AJAY KUMAR !!!!!%%%%"
out = name.isupper()
print(out)

name = "AJAY KUMar!!!!!%%%@@@@"
out = name.isupper()
print(out)

tt = "aJAy kUMaR is hErE foR a rEAsoN"
out = tt.title()
print(out)
out2 = out.capitalize()
print(out2)

inp = tt.swapcase()
print(tt)
print(inp)

data = "Ajay, Kiran, Kumar, Ramesh, Vijay, Sachin"
print(data[19:24])

data = ["Ajay", "Kiran", "Kumar", "Ramesh", "Vijay", "Sachin"]
print(data[-2])

print("****SPLIT - Converting string into List****")

data = "100:200:300:400"
out = data.split(":")
print(data)
print(out)

data = "Ajay is a good boy"
out =data.split(" ")
print(data)
print(out)

data = "a\nb test abc\t dummy"
out = data.split()
print(data)
print(out)

data = "100@200:300::400@@abc"
out = data.split(":")
print(data)
print(out)

data = ["Ajay", "Kiran", "Kumar", "Ramesh", "Vijay", "Sachin"]
out = ":".join(data)
print(data)
print(out)



