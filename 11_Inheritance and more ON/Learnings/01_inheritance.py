class Employee:  # The is a base class or parent class
    company = "ITC"
    def show(self):
        print(f"The name of Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name  is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee): # This is a inheritance class
    company = "ITC Infotech"
    def show(self):
         print(f"The name  is {self.name} and the salary is {self.salary}")


a = Employee()
b = Programmer()

print(a.company, b.company)