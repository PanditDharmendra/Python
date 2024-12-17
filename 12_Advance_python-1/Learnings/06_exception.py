# Exception handling in the program
try:
    a = int(input("Hey, Enter a number: "))

except ValueError as v:
    print("Hellow ")
    print(v)

except Exception as e:
    print(e)

    # It cant give chance to program to crash or distroy.

print("Thank you: ")