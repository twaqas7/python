class Employee:
    age = 21
    language = "Python"  # This is class attribute
    salary = 10000


First_employee = Employee()
First_employee.name = "TAHIR WAQAS"  # This is instance attribute
print(First_employee.name, First_employee.language, First_employee.salary)
# Output: TAHIR WAQAS Python 10000

second_employee = Employee()
second_employee.name = "Ali Raza"
print(second_employee.name, second_employee.language, second_employee.salary)
# Output: Ali Raza Python 10000

# Here name is instance attribute and salary and language are class attributes as directly belong to class


