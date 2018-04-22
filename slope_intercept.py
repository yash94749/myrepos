#!/usr/bin/python
var1 = input("enter the value of x?. ")
var2 = input("enter the value of y?. ")
var3 = input("enter the value of x1?. ")
var4 = input("enter the value of y1?. ")

def slope(x1, y1, x2, y2):
                  dy = y2 - y1
                  dx = x2 - x1
                  m = float(dy)/dx
                  print m
                  return m
def intercept(x1, y1, x2, y2):
                    a1 = x2 * slope(x1, y1, x2, y2)
                    b1 = y2 - a1
                    return b1

ans = intercept(var1, var2, var3, var4)
print ans
