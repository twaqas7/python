# 1. Write a program using functions to find greatest of three numbers.

a = 1
b = 2
c = 34


def greatest(a, b, c):
    if a > b and a > c:
        return "a", a
    elif b > a and b > c:
        return "b", b
    else:
        return "c", c


name, value = greatest(a, b, c)  # unpacking the tuple

print(f"The greatest number is {name} and its value is: {value}")
