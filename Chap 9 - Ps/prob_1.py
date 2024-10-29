# 1. Write a program to read the text from a given file ‘poems.txt’ and find out


f = open("poems.txt", "r")

content = f.read()

if "twinkle" in content:
    print("Twinkle is present in the file")
else:
    print("Twinkle is not present in the file")
f.close()
