def getfile():
    filename = input("Enter filename: ")
    return filename

def getyear():
    year = input("Enter year: ")
    return year

def checkyear(year, header):
    '''Checks if input year is in header of table'''
    try:
        if int(year) in header:
            return True
        else:
            return False
    except ValueError:
        return False

def openfile(getfile):
    try:
        workfile = open(getfile, "r")
        return workfile
    except FileNotFoundError:
        print("Filename {} not found!".format(getfile))
        return False

def makelist(workfile):
    '''Converts textfile to lists and sublists'''
    listmaker = []
    for line in workfile:
        splitline = line.split()
        listmaker.append(splitline)
    return listmaker

def make_cleantable(worklist):
    '''Changes strings in list to integers if they are numbers'''
    '''Also joins string objects in lists to make state names'''
    cleantable = []
    for sublist in worklist:
        wordlist = []
        numlist = []
        for item in sublist:
            if item.isalpha():
                wordlist.append(item)
            else:
                numlist.append(int(item))
        cleantable.append([' '.join(wordlist)] + numlist)
    return cleantable

def listcolumn(table, column):
    '''Makes a list out of values in a given column of a table'''
    column_list = []
    for line in table[1:]:
        column_list.append(line[column])
    return column_list

def findstate(table, column_list, value):
    '''Looks for the position of value in a given column'''
    '''and uses it to connect it to a state name from the table'''
    state = table[column_list.index(value)+1][0] 
        #Value from column 0, row number is the value's index +1, 
        #because row 0 (the header) wasn't included in column_list
    return (value, state)

#####  START OF MAIN #####
def main():
    workfile = openfile(getfile())
    if workfile:
        worktable = make_cleantable(makelist(workfile))
        header = worktable[0]
        
        year = getyear()
        while checkyear(year, header) == False:
            print("Invalid year!")
            year = getyear()
        
        column = header.index(int(year)) #The column that matches year from input
        column_list = listcolumn(worktable,column) #Simple list of only numbers from that column
        min_column = min(column_list)
        max_column = max(column_list)
                
        print("Minimum:", findstate(worktable, column_list, min_column))
        print("Maximum:", findstate(worktable, column_list, max_column))

main()