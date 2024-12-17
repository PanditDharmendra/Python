a1 = int(input("Enter mark of physics: "))
a2 = int(input("Enter mark of Mathematics: "))
a3 = int(input("Enter mark of Chemistry: "))

# Chack for total percentage.
total_percentage = (100*(a1 + a2 + a3))/300
if(total_percentage>=40 and a1>=33 and a3>=33 and a2>=33):
    print("You are pass:",total_percentage)

else:
    print("You faild,try again next year:",total_percentage)

