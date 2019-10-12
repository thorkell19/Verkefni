import string

def get_word_list(fstream):
    word_list = []
    for line in fstream:
        word_list = word_list + line.strip().split()
    clear_list = []
    for word in word_list:
        clear_list.append(word.strip(string.punctuation))
    return clear_list

def word_list_to_counts(wordlist):
    workdiction = {}
    for word in wordlist:
        if word.lower() in workdiction:
            workdiction[word.lower()] += 1
        else:
            workdiction[word.lower()] = 1
    return workdiction

def dict_to_tuple(work_dict):
    tuple_list = []
    for word, number in work_dict.items():
        tuple_list.append((word, number))
    return sorted(tuple_list)


def main():
    filename = input("Name of file: ")
    # Get a file stream
    fstream = open(filename)
    # Get a list of words from the stream
    word_list = get_word_list(fstream) 
    fstream.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()