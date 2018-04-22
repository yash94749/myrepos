#!/usr/bin/python
import math
var1 = int(input("enter ther value of x1. "))
var2 = int(input("enter ther value of y1. "))
var3 = int(input("enter ther value of x2. "))
var4 = int(input("enter ther value of y2. "))

def distance(x1, y1, x2, y2):
                     dx = x2 - x1
                     dy = y2 - y1
                     dsqroute = dx**2 + dy**2
                     result = math.sqrt(dsqroute)
                     return result
                     print(result)
def area(rad):
       temp = math.pi * rad**2
       return temp

def area2(x1, y1, x2, y2):
           radius = distance(x1, y1, x2, y2)
           result = area(radius)
           return result
    
ans = area2(var1, var2, var3, var4)
print (ans)
