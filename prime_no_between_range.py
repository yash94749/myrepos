x = input("enter the lower number. ")
y = input("enter the higher number. ")

for num in range(x,y):
    i = 2
    counter = 0
    while i < num :
        if num % i == 0:
            counter = 1
            i = i + 1

        else:
            i = i + 1

    if counter == 0:
        print (str(num) + " " "is a prime number")

    else:
        counter = 0
        
