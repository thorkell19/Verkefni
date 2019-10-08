import string

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

word = "rassgat."
middle = wordmiddle(word)
print(middle)

def scramble(middle):
    scrambl = ""
    for pos, letter in enumerate(middle):
        if pos % 2 == 0 and pos < len(middle)-1:
            scrambl += middle[pos+1]
        elif pos % 2 == 1 and pos < len(middle):
            scrambl += middle[pos-1]
        else:
            scrambl += letter
    return scrambl

print(scramble(middle))