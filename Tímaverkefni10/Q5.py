import string

# Implement a function here
def no_space_no_punct(sentence):
    sentence_clean = ""
    for letter in sentence:
        if letter != " " and letter not in string.punctuation:
            sentence_clean += letter
    return sentence_clean

def uniqueletters(sentence):
    unique_letters = []
    for letter in sentence:
        if letter in unique_letters:
            unique_letters = unique_letters
        else:    
            unique_letters.append(letter)
    return unique_letters

# Main starts here
sentence = input("Input a sentence: ")

# Call the function here
sentence = no_space_no_punct(sentence)
print("Unique letters:", uniqueletters(sentence))