def merge_lists(list1, list2):
    list3 = list1
    for item in list2:
        if item not in list3:
            list3.append(item)
    newlist = sorted(list3)
    return newlist

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
