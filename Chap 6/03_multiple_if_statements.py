a = int(input("Enter your age: "))

# if statement no 1

if (a % 2 == 0):
    print(f"you have entered an even number which is: {a}")

# end of the if statement no 1

# if statement no 2

if a >= 18:
    print("you are above the age of consent")
    print("you can vote")

elif (a < 0):
    print("you are entering invalid negative age")

else:
    print("you are below the age of consent")

# end of the if statement no 2

print("End of program")
