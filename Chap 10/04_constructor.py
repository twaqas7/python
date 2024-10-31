class Employee:
    language = "Python"
    salary = "120k"

    # dunder method or magic method which is called automatically when object is created starts with __ and ends with __
    # and it is called constructor and usully __init__ is called automatically when object is created

    def __init__(
        self, name, language, salary
    ):  # __init__ is a constructor which can take multiple parameters
        self.name = name
        self.language = language
        self.salary = salary

        print("Constructor has been called here")

    def getinfo(self):
        print(
            f"The language is {self.language} and salary is {self.salary} and my name is {self.name}"
        )

    @staticmethod
    def greet():
        print("Good Evening!")


Tahir = Employee("TAHIR WAQAS", "Python", "200k")

# instead of this we passed these values in constructor as parameters

# Tahir.name = "TAHIR WAQAS"

print(Tahir.name, Tahir.language, Tahir.salary)

Tahir.getinfo()
Tahir.greet()
