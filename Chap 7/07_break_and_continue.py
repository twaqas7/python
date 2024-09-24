# break and continue are used to control the flow of the loop

# break: It is used to exit the loop when a certain condition is met

for i in range(50):
    if i == 23:
        break # break the loop when i is 23 which means loop will not iterate further exit the loop when i is 23
    print(i)

# continue: It is used to skip the current iteration and continue with the next iteration

for i in range(50):
    if i == 23:
        continue # skip the current iteration and continue with the next iteration when i is 23
    print(i)