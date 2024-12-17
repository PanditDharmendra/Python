class Employee:  # The is a base class or parent class
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of Employee is {self.name} and the company is {self.company}")

class coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")


class Programmer(Employee, coder): # This is a  multiple inheritance class
    company = "ITC Infotech"
    def showlanguage(self):
         print(f"The name  is {self.name} and the language is {self.language}")


a = Employee()
b = Programmer()

b.show()
b.showlanguage()
b.printLanguage()