a = 83 #It is global variable

def func():
    global a #Change 83 in 33 means change the global variable in func variable.
    print(a)
    a = 33 #func variable

func()
print(a)