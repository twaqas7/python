# 2. Write a python program using function to convert Celsius to Fahrenheit.


def f_to_c(fahrenheit):

    return 5 * (fahrenheit - 32) / 9


fahrenheit = int(input("Enter temperature in Fahrenheit: "))


print(f"The temperature in celsius is: {f_to_c(fahrenheit)}")
