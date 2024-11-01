# # Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?


class demo:
    a = 4


o = demo()
print(o.a)  # prints class attribute because instance attribute is not set yet
o.a = 0  # and here we are setting instance attribute
print(o.a)  # and here now o.a is instance attribute
print(demo.a, "demo.a is not changed that's means class attribute is not changed by setting instance attribute") 
