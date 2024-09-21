# s = {8, 7, 12, "Tahir", [1, 2]}

# no we can't use list as a key in set because list is mutable and mutable objects are not hashable.
# only immutable objects are hashable.
# so we can use tuple instead of list.


s = {8, 7, 12, "Tahir", (1, 2)}

# we cant update  directly the tuple in set so we have to remove it and then add it again.

s.remove((1, 2))
s.add((1, 3))

# we can't sort set directly so we convert it to list and then sort it.
sorted_list = sorted(s, key=lambda x: (str(type(x)), x))

print(sorted_list)  # sorted the set but as a list


print(s) # set after removing and adding tuple
