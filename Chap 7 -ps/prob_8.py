"""

for n = 5 print the following pattern:

*
**
***
****
*****

for n = 3 print the following pattern:

*
**
***

"""

star = int(input("Enter the number of stars: "))

for index in range(1, star + 1):
    print("*" * index)
