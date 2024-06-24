
class Employee:
    language = "Python"
    salary = 2000000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
            print("Good morning")


souvik = Employee()
# souvik.language - "Javascript" # This is an instance attribute
Employee.greet()
souvik.getInfo()
#Employee.getInfo(souvik)



















