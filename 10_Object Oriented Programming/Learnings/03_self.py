class Employee:
    language = "python" # This is a class attribute 
    salary = 120000000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet(): # It cant take self because @staticmethod.
        print("Good morning")

dharmendra = Employee()
dharmendra.language = "JavaScript"  # This is an object/instance attribute 
print(dharmendra.salary, dharmendra.language)

dharmendra.getInfo()
Employee.getInfo(dharmendra)
dharmendra.greet()

