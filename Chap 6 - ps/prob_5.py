l = ["Tahir", "Ali", "Hassan", "Sami", "Waqas"]

name = input("Enter the name you want to search: ")

if name in l:
    print(f"Congrats! {name} is in the list")

else:
    print(f"Sorry {name} is not in the list.")
