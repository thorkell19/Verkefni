def get_file():
    getfile = input("Enter filename: ")
    return getfile

def open_file(get_file):
    openfile = open(get_file, "r")
    return openfile

def sort_file(open_file):
    import string
    string_list = []
    sort_list = []
    
    for line in open_file:
        string_list += line.split()
    
    for word in string_list:
        if word.strip(string.punctuation) not in sort_list:
            sort_list.append(word.strip(string.punctuation))
    
    return sorted(sort_list)

getfile = get_file()
openfile = open_file(getfile)
print(sort_file(openfile))