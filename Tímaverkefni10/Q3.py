outlist = []

# Your functions should appear here
def addtolist(invalue):
    while invalue != "exit":
        outlist.append(invalue)
        invalue = input("Enter value to be added to list: ")
    return outlist

def printletter(outlist):
    for value in outlist:
        print(value)

# Main program starts here
invalue = input("Enter value to be added to list: ")
outlist = addtolist(invalue)*3

# It should mostly be a sequence of function calls
printletter(outlist)