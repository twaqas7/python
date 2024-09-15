a = (1, 454, "TAHIR", "SAmi", "TAHIR", 3.45, "TAHIR", "TAHIR")
print(a)

counter = a.count("TAHIR")

print(counter)


index = a.index("TAHIR")
print(index)

# Concatenation (+):

# Combines two or more tuples to form a new tuple.

t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4)


# Repetition (*):

# Repeats a tuple multiple times.

t = (1, 2)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)


# Tuple slicing:

# Access a subset of the tuple using slicing.

t = (1, 2, 3, 4, 5)
print(t[1:4])  # Output: (2, 3, 4)


# Tuple unpacking:

# Extract values from a tuple into separate variables.

t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # Output: 1 2 3


# len():

# Returns the number of items in the tuple.

t = (1, 2, 3, 4)
print(len(t))  # Output: 4


# in and not in:

# Checks if an element exists in the tuple.

t = (1, 2, 3)
print(2 in t)  # Output: True
print(5 not in t)  # Output: True
