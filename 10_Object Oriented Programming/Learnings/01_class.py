class Employee:
    language = "python" # This is a class attribute 
    salary = 120000000

dharmendra = Employee()
dharmendra.name = "Dharmendra"  # This is an object/instance attribute 
print(dharmendra.salary, dharmendra.language)

rohan = Employee()
rohan.name = "rohan roro"
print(rohan.name, rohan.language, rohan.salary)

# Here name is object attribute and salary and language are class
#  attributes as they directily blong to the class