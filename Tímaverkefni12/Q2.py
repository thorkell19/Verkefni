# sort_list() function goes here
def sort_list(a_list):
    a_list.sort()
    return None

# get_list() function goes here
def get_list():
    try:
        getlist = []
        while len(getlist)>= 0:
            getlist.append(int(input()))
    except ValueError:
        return getlist

# Do not modify this part
def main():
    a_list = get_list()
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    
main()