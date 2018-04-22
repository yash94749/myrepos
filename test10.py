#!/usr/bin/python
def newline(x, n):
          if x > n:
               print 
          else:
             x = x + 1
             print x
             newline(x, n)
              

newline(0, 27)

          
