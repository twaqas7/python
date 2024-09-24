marks_1 = int(input("Enter the first subject marks: "))

marks_2 = int(input("Enter the second subject marks: "))

marks_3 = int(input("Enter the third subject marks: "))

# CHECK FOR TOTAL PERCENTAGE

total_perecentage = int((marks_1 + marks_2 + marks_3) / 300 * 100)

if total_perecentage >= 40 and marks_1 >= 33 and marks_2 >= 33 and marks_3 >= 33:
    print(f"congrats! you have passed the exam: percentage is {total_perecentage}%")
else:
    print(f"Sorry! you have failed the exam: percentage is {total_perecentage}%")
