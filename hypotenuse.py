#!/usr/bin/python
import math
var1 = input("enter ther value of x1. ")
var2 = input("enter ther value of y1. ")

def hypotenuse(a, b):
               dsqroute = a**2 + b**2
               result = math.sqrt(dsqroute)
               return result

ans = hypotenuse(var1, var2)
print ans
