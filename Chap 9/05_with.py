f=open("file.txt")

print(f.read())

f.close()


# The same can be done with the with statement:

with open("file.txt") as f:
    print(f.read())

# you dont have to close the file when you use with statement
