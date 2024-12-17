class Employee:
    language = "python" # This is a class attribute 
    salary = 120000000

dharmendra = Employee()
dharmendra.language = "JavaScript"  # This is an object/instance attribute 
print(dharmendra.salary, dharmendra.language)

