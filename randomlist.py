import random
var1 = input("enter a no,.  ")

def randomList(n):
    s = [0] * n
    for i in range(n):
        s[i] = random.random()
    return s
result = randomList(var1)
print result
