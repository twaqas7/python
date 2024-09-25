user_number = int(input("Enter a number: "))

for i in range(2, user_number):
    if (user_number % i) == 0:
        print("Number is not prime")
        break
    else:
        print("Number is prime")
        
