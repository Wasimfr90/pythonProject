

t1 = ("Thetestingacadamy","for","TheTestingAcadamy")
t2 = ("Thetestingacadamy","for","Thetestingacadamy")

s1 = set(t1)
s2 = set(t2)
print(s1)
print(s2)

set1 = {1,2,3}
set2 = {4,5,6}

my_set = set1.union(set2)
print(my_set)


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

my_set2 = set1.intersection(set2)
print(my_set2)

my_set3 = set1.difference(set2)
print(my_set3)

my_set4 = set1.symmetric_difference(set2)
print(my_set4)

set1 = {1,2,3,4,5}
set2 = {2,3,8}

my_set5 = set1.issubset(set2)
print(my_set5)

