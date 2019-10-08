testfile = open("test.txt", "r")

for line in testfile:
    printline= line.strip().replace(" ", "")
    print(printline, end="")