##Armstrong number:
##An Armstrong number is an n-digit number that is
##equal to the sum of the nth powers of its digits
var1=int(input("please enter the Start no. "))
var2=int(input("please enter the End no. "))
def armstrong(a,b):
 for y in range(a,b):
    if y < 100:
        #print (y, "value is less than 100")
        #print ("")
        pass

    else:
        z = len(str(y))
        x = y
        sum = 0
        while y > 0:
            i = y % 10
            sum = sum + (i ** z)
            y = y // 10
        if x == sum:
            print (x, "is an armstrong No")
            
 
 
print (armstrong(var1,var2))

