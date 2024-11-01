# Collection in Python

# basic Data Structures
# List
# Dict
# set
# tuple
#
#
# Advanced Collection
# deque - Queue
# defaultDict
# Counter
# orderedDict
# chainMap
# nametuple

### deque -> double-ended queue  -> It is a class
# FIFO - First In First Out
#  A list-like sequence optimized for data access near its endpoint

from collections import deque

# create a deque

#d = deque()

d = deque([1,2,3])
print(d)

d.append(4)
print(d)

# add element to the left

d.appendleft(0)
print(d)

# Extend

d.extend([5,6])
print(d)

#print(d.pop())   -> from last
#print(d.popleft())  -> from front

d.reverse()
print(d)