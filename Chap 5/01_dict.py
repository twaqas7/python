# marks = {"Hadi": 85, "Waqas": 90, "Sami": 100}

# # print(marks, type(marks))

marks = {"Hadi": 85, "Waqas": 90, "Sami": 100, "munir": 95}

while True:
    student_name = input("Enter the student's name (or type 'exit' to quit): ").title()

    if student_name.lower() == "exit":
        break

    if student_name in marks:
        print(f"{student_name}'s marks: {marks[student_name]}")
    else:
        print(f"No record found for {student_name}")
