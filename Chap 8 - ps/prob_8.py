# 8. Write a python function to print multiplication table of a given number.


def get_table(user_input):
    for i in range(1, 11):
        print(f"{user_input} x {i} = {user_input * i}")
    


user_input = int(input("Enter a number to get its multiplication table: "))

(get_table(user_input))
