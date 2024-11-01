# OrderedDict
# Dictionary that remembers insertion order.

from collections import OrderedDict, defaultdict

# d = {"name": "Wasim", "age" : 78, "address" : "KA", "id" : 123}    # in normal dict order is not maintained.
d = dict()
d["age"] = 78
d["name"] = "wasim"
d["address"] = "KA"
d["id"] = 123

print(d)

od = OrderedDict()
od['banana'] = 2
od['apple'] = 1
od['pear'] = 3

print(od)


dd = defaultdict(int)
print(dd)