infile = input("Enter filename: ")

readfile = open(infile, "r")

line = ""

for word in readfile:
    if word.strip() != ".":
        line += word.strip() + " "
    elif word.strip() = ",":
        line = line.strip() + word.strip()
    else:
        line = line.strip() + word.strip()
        print(line)
        line = ""