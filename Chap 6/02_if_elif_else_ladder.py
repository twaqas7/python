a = int(input("Enter your age: "))

# if elif else ladder

if a >= 18:
    print("you are above the age of consent")
    print("you can vote")

elif (a < 0):
    print("you are entering invalid negative age")

elif (a == 0):
    print("you are entering 0 which is not a valid age")

else:
    print("you are below the age of consent")

# end of the if elif else ladder

print("End of program")

# Output:

# Enter your age: 20 or if age is negative number like -1 or 0 then output will be "you are entered invalid age"

# you are above the age of consent

# you can vote

# End of program
