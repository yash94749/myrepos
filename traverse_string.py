str=input("please enter string. ")
def traverse_string(str):
    x = len(str)
    for i in range(x):
        print(str[x-1-i])
    return ''
print(traverse_string(str))
