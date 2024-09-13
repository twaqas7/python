name = "Tahir"

print(name[0:3])

print(
    name[-4:-1]
)  # these are same on upper line we used negative slicing and and in second line
# we used corresponding positive slicing

print(
    name[1:4]
)  # these are same on upper line we used negative slicing and and in second line
# we used corresponding positive slicing


print(name[:4])  # These two are same if nothing before colon then consider as 0
print(name[0:4])  # These two are same if nothing before colon then consider as 0

print(
    name[1:]
)  # These two are same if nothing after colon then consider as end or lenght of string
print(
    name[1:5]
)  # These two are same if nothing after colon then consider as end or lenght of string


word = "Amazing"
print(word[1:6:2])  # mzn

word = "Amazing"
print(word[:7])  # word [0:7] - Amazing

print(word[0:])  # word [0:7] - Amazing

