##Factorial number program
##factorial of a number is the product of all the integers from 1 to that number.
x = int(input("enter first number. "))
factorial = 1
if x < 0:
        print ("Factorial does not exist for Negative integer")
elif x == 0:
        print ("Factorial of 0 is 1")
else:
        for i in range(1,x + 1):
                factorial = factorial * i
        print("Factorial of", x, "is" , factorial)   
##def factorial(n):
##    if n == 0:
##        return 1
##    else:
##        return n * factorial(n-1)
##result = factorial(x)
##print(result)
        
 





