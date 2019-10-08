#list_to_tuple function goes here
def list_to_tuple(a_list):
    a_tuple = ()
    try:
        for item in a_list:
            a_tuple += (int(item),)
        return a_tuple
    except ValueError:
        print("Error. Please enter only integers.")
        return ()

#Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)