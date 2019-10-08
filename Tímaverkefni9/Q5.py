filename = input("Enter filename: ")

userfile = open("words.txt", "r")
writefile = open("sentences.txt", "w")

line = ""

print(userfile)

#for word in userfile:
#    while word != ".":
#        line += word
#    else:
#        line += word
#        print(line)