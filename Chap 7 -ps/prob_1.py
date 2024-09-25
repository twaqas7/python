# Write a Python program to get the multiplication table of a number.

user_number = int(input("Enter a number to get its multiplication table: "))

for index in range(1, 11):
    print(f"{user_number} x {index} = {user_number * index}")

# Output: Enter a number: 5

# 5 x 1= 5
# 5 x 2= 10
# 5 x 3= 15
# 5 x 4= 20
# 5 x 5= 25
# 5 x 6= 30
# 5 x 7= 35
# 5 x 8= 40
# 5 x 9= 45
# 5 x 10= 50
