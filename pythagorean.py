#!/usr/bin/python
import math
var1 = input("enter ther value of x1. ")
var2 = input("enter ther value of y1. ")
var3 = input("enter ther value of x2. ")
var4 = input("enter ther value of y2. ")

def distance(x1, y1, x2, y2):
                     dx = x2 - x1
                     dy = y2 - y1
                     dsqroute = dx**2 + dy**2
                     result = math.sqrt(dsqroute)
                     return result

ans = distance (var1, var2, var3, var4)
print ans
