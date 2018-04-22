##Armstrong number:
##An Armstrong number is an n-digit number that is
##equal to the sum of the nth powers of its digits
var1 = int(input("enter the start value. "))
var2 = int(input("enter the End value. "))
for y in range(var1,var2):
     if y < 100:
          print (y, "is less than three digit")
     else:
      z = len(str(y))
      x = y
      sum = 0
      while y > 0:
        i = y % 10
        sum = sum + (i ** z)
        y = y // 10

      if x == sum:
        print (x, "is an armstrong number")

     
