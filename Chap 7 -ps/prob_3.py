# prob_1 : Write a Python program to get the multiplication table of a number using a while loop.

# while loop

user_number = int(input("Enter a number to get its multiplication table: "))

index = 1

while index <= 10:
    print(f"{user_number} x {index} = {user_number * index}")
    index += 1
