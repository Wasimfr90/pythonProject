#Continue statement

# Continue statement skips the current iteration of a loop
# and move to new iteration

for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

# i | condition | o/p
# 0 | 0%2 == 0 -> True | continue - skip No o/p
# 1 | 1%2 == 0 -> False | 1
# 2 | 2%2 == 0 -> True |  continue - skip No o/p
# 3 | 3%2 == 0 -> False | 3

#pass -> will also do the same task as continue.
#pass -> it can be used in the statement, function, class and objects.
#pass is more advanced than continue, we will learn it later.

