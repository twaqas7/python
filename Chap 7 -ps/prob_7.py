"""

for n = 3 print the following pattern:

  *
 ***
*****

"""

star = int(input("Enter the number of stars: "))

for index in range(1, star + 1):
    print(" " * (star - index) + "*" * (2 * index - 1))  
    # This is the same as the commented code below
   

# same as the code above

# print(" " * (star - index), end="")
# print("*" * (2 * index - 1), end="")
# print(" ")
