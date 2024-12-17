# without return value.
def goodDay(name, ending):
    print("Good Day, " + name) 
    print(ending)

goodDay("Dharmendra", "Thank You") 
goodDay("Harry","Thank You")
goodDay("akash", "Thanks")


# with return value.
def goodDay(name, ending):
    print("Good Day, " + name) 
    print(ending)
    return "End"

a = goodDay("Dharmendra", "Thank You") 
print(a) # a will now contain "Good day Dharemendra, Thank You."


# Get output without used 'print()' Function.
def greet(name): 
    gr = "hello"+ name  
    return gr  
    a = greet ("harry") # a will now contain "hello harry" 

