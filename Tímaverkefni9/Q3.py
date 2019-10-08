filename = input("Enter filename: ")

words = open(filename, "r")

long_length = 0
long_word = ""

for word in words:
    if len(word.strip()) > long_length:
        long_length = len(word.strip())
        long_word = word.strip()

print("Longest word is " + "'"+ long_word +"'" + " of length", long_length)