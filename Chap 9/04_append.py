st = "Hey Harry, your Python course is amazing!"

f = open("myfile.txt", "a")
st = "\nHey Harry, your Python course is amazing!"
f.write(st)
f.close()

f.write(st)

f.close()