a = int(input("Enter the value of first: "))
b = int(input("Enter the value of second: "))
if (b == 0):
    raise ZeroDivisionError("Hay our program is not meant to divide by number zeros.")
else:
     print(f"The division a/b is: {a/b}")

     # It instruct developer to currect the error mainly zeroDifisionError crash the
     # the program sometime we want to crash the program to alert the user or developers
     