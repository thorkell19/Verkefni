listi1 = [["New", "Hampshire", "1900000"],["Pennsylvania", "1800000"]]

for sublist in listi1:
    joinlist = []
    for item in sublist:
        if item.isdigit()== False:
            joinlist.append(item)
            print(joinlist)