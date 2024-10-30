# Write a program to find out the line number where python is present from ques 6.


with open("log.txt") as f:
    lines = f.readlines()

line_no = 1

for line in lines:
    if "pyhton" in line:
        print(f"python is present in line: {line_no}")
        break
    line_no += 1

else:
    print("python is not present in the log file")
