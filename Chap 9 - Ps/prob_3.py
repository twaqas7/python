#  Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.


def generateTable(n):
    # table = ""
    # for i in range(1, 11):
    #     table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/multiplicaton_table_of_{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n} X {i} = {n*i}\n")


for i in range(2, 21):
    generateTable(i)
