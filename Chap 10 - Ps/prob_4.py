# 4. Add a static method in problem 2, to greet the user with hello.


class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num ** 2}")

    def cube(self):
        print(f"The cube of {self.num} is {self.num ** 3}")

    def sqrt(self):
        print(f"The square root(sqrt) of {self.num} is {round(self.num ** 0.5, 3)}")

    @staticmethod
    def greet_user():
        print("Hello there! Welcome to the calculator.")

    @staticmethod
    def get_number():
        while True:
            try:
                return int(input("Enter a number to calculate: "))
            except ValueError:
                print("Please enter a valid integer.")


number_to_calculate = Calculator(Calculator.get_number())
number_to_calculate.greet_user()
number_to_calculate.square()
number_to_calculate.cube()
number_to_calculate.sqrt()