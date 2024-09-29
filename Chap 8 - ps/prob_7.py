# 7. Write a python function to remove a given word from a list and strip it at the same


def rem(l, word):
    n = []
    for item in l:
        if item != word: 
            n.append(item.strip(word))
    return n


l = ["tahir", "ali", "sami", "hamza", "ahsan", "ahmad", "an"]

print(rem(l, "an"))
