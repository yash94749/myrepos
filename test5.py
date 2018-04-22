#!/usr/bin/python
prompt = ("enter the value?. ")
y = input(prompt)
def printParity(x):
            if (x % 2 == 0):
               print x, "is even."
            else:
               print x, "is odd."
printParity(y)
