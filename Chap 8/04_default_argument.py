# DEFAULT PARAMETER VALUE


def goodDay(name, ending="Thank You"):
    print(f"Good Day,{name} {ending}")


# if we did not provide the second argument it will take the default value whose value is "Thank You" which is defined in the function ending parameter but if we provide the second argument it will take the value which we provide in the argument which is "Thanks" in this case. this is called default argument value concept.

goodDay("Tahir", "Thanks")


# here i did't provide the second argument so it will take the default value which is "Thank You"

goodDay("Waqas")

# OUTPUT: Good Day Tahir Thank You
