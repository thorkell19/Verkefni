def get_list():
    getlist = input("Enter elements of list separated by commas: ")
    return getlist

mylist = get_list().split(",")
joinstring = ""

for element in mylist:
    joinstring += element

if joinstring.isdecimal() == False:
    print("Error - please enter only integers.")
elif "88" in joinstring:
        print("True")
else:
        print("False")