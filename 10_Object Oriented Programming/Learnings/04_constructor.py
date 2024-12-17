class Employee:
    language = "python" # This is a class attribute 
    salary = 120000000

    def __init__(self, name, salary, language): # As a dunder method which is automatically called.
      self.name = name
      self.salary = salary
      self.language = language
      print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet(): # It cant take self because @staticmethod.
        print("Good morning")

dharmendra = Employee("Dharmendra", 13000000, "JavaScript")
# dharmendra.name = "Dharmendra"

print(dharmendra.name, dharmendra.salary, dharmendra.language)

# dharmendra = Employee()
