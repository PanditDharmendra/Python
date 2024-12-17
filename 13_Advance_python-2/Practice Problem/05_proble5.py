from functools import reduce
a = [1,5,10 ,17 , 19 , 20 , 15, 25, 943, 235]

def greater(a,b):
    if (a>b):
        return a
    return b

val = reduce(greater, a)
print(val)