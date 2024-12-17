
User = int(input("Enter the value: "))

table =[User*i for i in range(1,11)]
print(table)


with open ('Table.txt', 'a') as file:
    file.write(f"Table of {User}: {str(table)}\n")