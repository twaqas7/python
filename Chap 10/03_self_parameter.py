class Employee:
    language = "pyhton"  # This is class attribute
    salary = 10000

    def getinfo(self):
        # we have to pass a parameter with any name, it is a convention to pass self for getting instance attributes and to prevent from errors or avoid from positional arguments which usually passed in functions or methods as 0
        print(
            f"The language is {self.language} and salary is {self.salary} and my name is {self.name}"
        )

    @staticmethod  # This means that greet() is a static method which does not need any object (parameter to be passed)
    def greet():
        print("Good Evening!")


Tahir = Employee()
Tahir.name = "TAHIR WAQAS"  # This is instance attribute
Tahir.language = "javascript"  # This is instance attribute
Tahir.salary = 20000

Tahir.getinfo()  # as same as Employee.getinfo(Tahir)
# Employee.getinfo(Tahir)  # as same as Tahir.getinfo()

Tahir.greet()
