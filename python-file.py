#!/usr/bin/python
var1 = raw_input("enter the oldfile, ")
var2 = raw_input("enter the new file, ")
def filterFile(oldFile, newFile):
 f1 = open(oldFile, "r")
 f2 = open(newFile, "w")
 while True:
  text = f1.readline()
  if text == "":
   break
  if text[0] == '#':
   continue
  f2.write(text)
 f1.close()
 f2.close()
 return
result = filterFile(var1, var2)
