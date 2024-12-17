
def divisible5(n):
    if(n%5 == 0):
        return True
    return False
a = [1,5,10 ,17 , 19 , 20 , 15, 25, 943, 235]


f = list(filter(divisible5, a))
print(f)