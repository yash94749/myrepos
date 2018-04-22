x = int(input("please enter lower value. "))
y = int(input("please enter higher value. "))
def table_in_horizental_formats(x,y):
    for num in range(x,y+1):
        for i in range(1,11):
            print('  ',num*i,end='\t')
            
        print('\n')
    return ''
result=table_in_horizental_formats(x,y)
print(result)
