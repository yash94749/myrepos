#!/usr/bin/python

def functionA():
        print "x grether than y"

def functionB():
        print "x less than y"

def functionC():
        print "x equal to y"

def comapre(x, y):
        if (x > y):
           functionA()
        elif (x < y):
               functionB()
        else:
           functionC()

comapre(12, 12)
            
