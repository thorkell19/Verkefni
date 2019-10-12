def menu_selection():
    print("Menu: ")
    selection = input("add(a), remove(r), find(f): ")
    return selection

def execute_selection(choice, a_dict):
    if choice == "a":
        add_to_dict(a_dict)
    if choice == "r":
        remove_from_dict(a_dict)
    if choice == "f":
        find_key(a_dict)

def add_to_dict(a_dict):
    new_key = input("Key: ")
    new_val = input("Value: ")
    if new_key in a_dict:
        print("Error. Key already exists.")
    else:
        a_dict[new_key] = new_val

def remove_from_dict(a_dict):
    rem_key = input("key to remove: ")
    if rem_key in a_dict:
        del a_dict[rem_key]
    else:
        print("Key not found.")

def find_key(a_dict):
    f_key = input("Key to locate: ")
    if f_key in a_dict:
        print("Value:", a_dict[f_key])
    else:
        print("Key not found.")

def dict_to_tuples(a_dict):
    dictlist = []
    for key, value in a_dict.items():
        dictlist.append((key, value))
    return dictlist


# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()