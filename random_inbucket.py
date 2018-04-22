import random
var1 = input("enter a no,.  ")
var2 = input("enter a no,.  ")
def randomList(n):
    s = [0] * n
    for i in range(n):
        s[i] = random.random()
    return s
result = randomList(var1)
def inBucket(t, low, high):
  count = 0
  for num in t:
   if low < num < high:
    count = count + 1
  return count
def NoOfBuckets(m):
    buckets = [0] * m
    bucketWidth = 1.0 / m
    for i in range(m):
     low = i * bucketWidth
     high = low + bucketWidth
     buckets[i] = inBucket(result, low, high)
    return buckets
results=NoOfBuckets(var2)
print results
