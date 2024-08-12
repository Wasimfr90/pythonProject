i =1
while i < 10:
    i += 1
    if i ==3:
        continue
    print(i)



print("*************************************")



fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)



for x in "banana" :
    print(x)


for x in range(2, 6):
    print(x)

print("*************************************")


for x in range(2,30,5):
    print(x)


print("*************************************")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

print("*************************************")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)