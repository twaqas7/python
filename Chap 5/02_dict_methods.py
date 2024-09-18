d = {}  # empty dictionary
print(d, type(d))

marks = {"Tahir": 89, "Waqas": 80, "Sami": 78, "Hadi": 73, "list": [89, 80, 78, 73]}


# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"Tahir": 88, "Arifeen": 85})

# print(marks)

print(marks.get("Tahir2"))  # prints none
# print(marks["Tahir2"])  # returns an error
