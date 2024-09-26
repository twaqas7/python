"""
factorial(0) => 0! = 1 
factorial(1) => 1! = 1  
factorial(2) => 2! = 2 x 1  
factorial(3) => 3! = 3 x 2 x 1  
factorial(4) => 4! = 4 x 3 x 2 x 1  
factorial(5) => 5! = 5 x 4 x 3 x 2 x 1  

factorial(n) => n! = n x n-1 x ...... 3 x 2 x 1

we can say that:

factorial(n) => n! = n * factorial(n-1)

"""

# RECURSION

# Recursion is a function which calls itself.

# It is used to directly use a mathematical formula as function.


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


"""
This upper function works as follows:

Factorial(5)
↓
5 x Factorial(4)
↓
5 x 4 x Factorial(3)
↓
5 x 4 x 3 x Factorial(2)
↓
5 x 4 x 3 x 2 x Factorial(1)
↓
5 x 4 x 3 x 2 x 1

"""


user_input = int(input("Enter the number to get's factorial: "))

print(f"The factorial of this number is: {factorial(user_input)}")
