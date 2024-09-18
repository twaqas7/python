s = {1, 3, 35, 2, 35, 1, "Tahir", "Waqas", "Sami", "Hadi"}

print(s, type(s))  # set doesn't allow duplicates

s.add("Arifeen")
print(s, type(s))

s.remove(35)  # will throw an error if the element is not found

s.remove("Waqas")

print(s, type(s))
