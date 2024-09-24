p1 = "Make a lot of money"
p2 = "buy now"
p3 = "Subscribe this"
p4 = "click here"
p5 = "watch this"


message = input("Enter your comment: ")

if (
    (p1 in message)
    or (p2 in message)
    or (p3 in message)
    or (p4 in message)
    or (p5 in message)
):
    print("The comment is spam")

else:
    print("The comment is not spam")
