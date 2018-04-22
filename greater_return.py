#!/usr/bin/python
import math
#value = ("please enter the value?. ")
#value1 = ("please enter the value2?. ")
var1 = int(input("please enter the value?. "))
var2 = int(input(("please enter the value1?. ")))

def absoluteValue(x, y):
                  if (x < y):
                       return x - y
                  elif (x > y):
                       return y - x
                  else:
                     return x - y
       


ans = absoluteValue(var1, var2)
print (ans)





          
