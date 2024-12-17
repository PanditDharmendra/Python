# Input: Size of the pattern (n)
n = int(input("Enter the number: "))

# Loop through each row
for i in range(n):
    # For the first and last row, print all stars
    if i == 0 or i == n-1:
        print("* " * n)
    # For the middle row, print stars at the beginning and end, and spaces in between
    else:
        print("* " + "  " * (n-2) + "*")
