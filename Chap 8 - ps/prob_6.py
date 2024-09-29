# 6. Write a python function which converts inches to cms.


def inch_to_cms(inch):
    return inch * 2.54


user_input = int(input("Enter value in inches: "))

print(f"The corresponding value in cms is {inch_to_cms(user_input):.2f} cm")
