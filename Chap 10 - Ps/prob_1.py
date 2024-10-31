# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


t = Programmer("TAHIR", 80000, 5234)
print(t.name, t.company, t.salary, t.pin)

r = Programmer("ALI", 90000, 5235)
print(r.name, r.company, r.salary, r.pin)

A = Programmer("AHMED", 100000, 5236)
print(A.name, A.company, A.salary, A.pin)

# output: TAHIR Microsoft 80000 5234
#         ALI Microsoft 90000 5235
#         AHMED Microsoft 100000 5236