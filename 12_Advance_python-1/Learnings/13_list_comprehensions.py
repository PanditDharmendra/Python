myList = [1, 2, 9, 5, 3, 7]

# squaredList = []
# for item in myList:
    # squaredList.append(item**2)

#This can simplyfied using  list comprehensions. 
squaredList = [i*i for i in myList]
print(squaredList)