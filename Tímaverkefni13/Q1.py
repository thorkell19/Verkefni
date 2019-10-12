def get_name():
    name = input("Name: ")
    return name

def get_number():
    number = input("Number: ")
    return number

def more_data():
    more = input("More data (y/n)? ")
    if more == "Y" or more == "y":
        return True
    elif more == "N" or more == "n":
        return False

def make_list(name_dict, name_list):
    for name, number in name_dict.items():
        name_list.append((name, number))

# MAIN
name_dict = {}
name_list = []
more_data = True

while more_data:
    name = get_name()
    number = get_number()
    name_dict[name] = number

    more = input("More data (y/n)? ")
    if more == "Y" or more == "y":
        more_data = True
    else:
        more_data = False

make_list(name_dict, name_list)
the_list = sorted(name_list)

print(the_list)