import string

def openfile(filename):
#opens text file if it is found
    try:
        return open(filename, "r")
    except FileNotFoundError:
        print("File " + filename + " not found!")

def last_is_punct(line):
#checks if line ends with punctuation
    if line[-1] in (string.punctuation):
        return True
    else:
        return False

def wordmiddle(word):
#strips words of first and last letter 
    if last_is_punct(word):
        return word[1:-2]
    else:
        return word[1:-1]

def last_and_punct(word):
#returns last character of word and punctuation (if it exists)
    if last_is_punct(word):
        return word[-2:]
    else:
        return word[-1]

def scramble(word):
#scrambles a word
    scramble_string = ""
    for pos, letter in enumerate(word):
        if pos % 2 == 0 and pos < len(word)-1:
            scramble_string += word[pos+1]
        elif pos % 2 == 1 and pos < len(word):
            scramble_string += word[pos-1]
        else:
            scramble_string += letter
    return scramble_string

#MAIN STARTS HERE
filename = input("Enter name of file: ")
readfile = openfile(filename)

for line in readfile:
    word = str(line).strip()
    middle = wordmiddle(word)
    lastchar = last_and_punct(word)
    scrambled = scramble(middle)
    
    if len(word) == 1:
        print(word, end=" ")
        #Because there's only 1 letter, the next print function would print that letter twice.
    else:
        print(word[0] + scrambled + lastchar, end=" ")