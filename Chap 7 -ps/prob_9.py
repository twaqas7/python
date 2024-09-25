"""
Write a Python program to construct the following pattern

***
* *
***

"""

star = int(input("Enter the number of stars: "))

for index in range(1, star + 1):
    if index == 1 or index == star:
        print("*" * star)
    else:
        print("*" + " " * (star - 2) + "*")
