## Reverse No
##This program reverse the number entered by the user and
##then prints the reversed number on the screen.
var1 = int(input("enter the first number. "))
var2 = int(input("enter the second number. "))
for y in range(var1,var2):
 x = y
 reverse = 0
 while y > 0:
        i = y % 10
        reverse = reverse * 10 + i
        y = y // 10

 print("Reverse No of enter No is.", reverse)





