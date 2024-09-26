import time

# FUNCTIONS WITH ARGUMENTS

name_str = ["Ali", "Sami", "Tahir", "Rehman", "Babar", "Zaib", "Hamza"]


def greet_message(name, ending):
    print(f"Good Evening {name} {ending}")
    return name_str  # for fun haha

# name_string use here for iteration of names

#     greet_message(name, "Thanks for coming") 
# for name in name_str: 
#     time.sleep(0.5)  # .5 second wait before greeting the next name

a = greet_message("Tahir", "Thanks for coming")

print(a)
