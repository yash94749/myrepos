##Armstrong number:
##An Armstrong number is an n-digit number that is
##equal to the sum of the nth powers of its digits
###changes in file
x = int(input("enter the number. "))
z = len(str(x))
y = x
sum = 0
if y < 10:
        print (x, "is less than three digit no")
else:
        while y > 0:
          i = y % 10
          sum = sum + (i ** z)
          y = y // 10

        if x == sum:
         print (x, "is an armstrong number")

        else:
         print (x, "is not armstrong number")
