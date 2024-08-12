print("********Disctionary********")

data ={2:"ramesh", 4:"kiren", 5:"ajay"}
print(data)
print(type(data))

data2 = {"rn1":"Wasim", "rn2":"Firoj", "rn3":"Rahaman"}
print(data2)

print(data2["rn2"])

v = data2["rn3"]
print(v)



data ={2:"ramesh", 4:"kiren", 5:"ajay"}

data[4] = "Sam"
print(data)

data[7] = "Kajol"
print(data)

data2 = {"rn1":"Wasim", "rn2":"Firoj", "rn3":"Rahaman"}
out = data2.keys()
print(out)
print(type(out))

out2 = data2.values()
print(out2)

out3 = data2.items()
print(out3)

print("**********************************")

data = {"rn1":"Wasim", "rn2":"Firoj", "rn3":"Rahaman", "rn4":"Sehnaj","rn5":"Parvin"}
v = data.get("rn4")
print(v)

v = data.get("rn7")
print(v)


v = data.setdefault("rn2")
print(v)

v = data.setdefault("rn6")
print(v)

print(data)

v = data.setdefault("rn7",[11,22,33])
print(v)
print(data)


v = data.pop("rn6")
print(v)
print(data)


data1 = {11:22, 33:44}
data2 = {55:66, 77:88}

print(data1)
data1.update(data2)

print(data1)
print(data2)
