# 5! = 1 x 2 x 3 x 4 x 5 => 120

user_input = int(input("Enter the number: "))
product = 1

for index in range(1, user_input + 1):
    product *= index

print(f"The factorial of {user_input} is {product}")
