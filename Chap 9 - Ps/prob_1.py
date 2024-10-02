# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

f = open("poems.txt")
Content = f.read()
if"twinkle" in Content:
    print("Yes, the file contains the word 'twinkle'")
else:
    print("No, the file does not contain the word 'twinkle'")
f.close()
