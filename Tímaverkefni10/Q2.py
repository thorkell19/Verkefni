
# The main program starts here
the_string = input("Enter the string: ")

def split(the_string):
    if "," in the_string:
        return the_string.split(",")
    else:
        return the_string.split()
    
# call your function here
print(split(the_string))