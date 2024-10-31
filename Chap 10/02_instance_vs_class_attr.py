class Employee:
    age = 21
    language = "Python"  # This is class attribute
    salary = 10000


first_employee = Employee()
first_employee.name = "TAHIR WAQAS"  # This is instance attribute
first_employee.language = "javscript"  # This is instance attribute

print(first_employee.name, first_employee.language, first_employee.salary)

# instance attribute gets preference over class attribute that's why language is javascript now
